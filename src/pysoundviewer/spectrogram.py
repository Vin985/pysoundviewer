import librosa
import numpy as np
from .options_object import OptionsObject


class SpectrogramOptions(OptionsObject):
    DEFAULT_OPTIONS = {
        "n_fft": 512,
        "to_db": True,
        "pcen": False,
        "remove_noise": False,
        "normalize": False,
        "hop_length": None,
        "window": "hann",
        "scale": "Linear",
        "nr_hist_rel_size": 2,
        "nr_N": 0.1,
        "nr_window_smoothing": 5,
        "follow_sound": False,
    }
    ACCEPTED_VALUES = {
        "n_fft": [str(2 ** x) for x in range(7, 12)],
        # "hop_length": [str(2 ** x) for x in range(6, 11)],
        "scale": ["Linear", "Mel"],
        "window": ["hann", "hamming", "boxcar", "bartlett"],
    }

    TYPE = "spectrogram"

    def __init__(self, spec_options=None):
        super().__init__(options=spec_options)


class Spectrogram:
    def __init__(self, audio, spec_options=None):
        self.options = spec_options
        self.audio = audio
        self.spec = self.create_spectrogram()

    def __getitem__(self, key):
        return self.options[key]

    @property
    def duration(self):
        return self.audio.duration

    def create_spectrogram(self):
        hop_length = self.options["hop_length"]
        if hop_length is not None:
            hop_length = int(hop_length)

        spectro = librosa.stft(
            self.audio.get_data(),
            int(self["n_fft"]),
            hop_length=hop_length,
            window=self["window"],
        )

        if self["scale"] == "Mel":
            spectro = librosa.feature.melspectrogram(
                S=spectro,
                n_mels=self.options._options.get(
                    "n_mels", 256
                ),  # y=self.audio.get_data(), sr=self.audio.sr
            )

        spec = np.abs(spectro)

        if self["pcen"]:
            # TODO: test this!!!
            return librosa.pcen(spec * (2 ** 31), bias=1, power=0.25)

        if self["remove_noise"]:
            # TODO: check SNR to remove noise?
            spec = self.remove_noise(
                spec,
                self["nr_N"],
                self["nr_hist_rel_size"],
                self["nr_window_smoothing"],
            )
            spec = spec.astype("float32")

        if self["normalize"]:
            spec = librosa.util.normalize(spec)

        if self["to_db"]:
            spec = librosa.amplitude_to_db(spec, ref=np.max)

        return spec

    def get_subspec(self, start, duration):
        fps = self.spec.shape[1] / self.audio.duration
        start_frame = int(start * fps)
        end_frame = int(start_frame + duration * fps)
        return self.spec[..., start_frame:end_frame]

    @staticmethod
    def remove_noise(spectro, N=0.1, hist_rel_size=2, window_smoothing=5):
        """
        Compute a new spectrogram which is "Noise Removed".

        spectro: spectrogram of the audio signal
        Options to be configured in conf file:
        histo_relative_size: ratio between the size of the spectrogram and
           the size of the histogram
        window_smoothing: number of points to apply a mean filtering on the
           histogram and on the background noise curve
        N: Parameter to set the threshold around the modal intensity

        Output:
            Noise removed spectrogram

        Ref: Towsey, Michael W. (2013) Noise removal from wave-forms and
           spectrograms derived from natural recordings of the environment.
           Queensland University of Technology, Brisbane.
        """

        # Min value for the new spectrogram (preferably slightly higher than 0)
        low_value = 1.0e-07

        len_spectro_e = spectro.shape[0]
        histo_size = int(len_spectro_e / hist_rel_size)

        background_noise = []
        for row in spectro:
            hist, bin_edges = np.histogram(row, bins=histo_size, density=False)

            ws = int(window_smoothing / 2)
            hist_smooth = [
                np.mean(hist[i - ws : i + ws]) for i in range(ws, len(hist) - ws)
            ]
            hist_smooth = np.concatenate((np.zeros(ws), hist_smooth, np.zeros(ws)))

            modal_intensity = int(
                np.min([np.argmax(hist_smooth), 95 * histo_size / 100])
            )  # test if modal intensity value is in the top 5%
            if N > 0:
                count_thresh = 68 * sum(hist_smooth) / 100
                count = hist_smooth[modal_intensity]
                index_bin = 1
                while count < count_thresh:
                    if modal_intensity + index_bin < len(hist_smooth):
                        count = count + hist_smooth[modal_intensity + index_bin]
                    if modal_intensity - index_bin >= 0:
                        count = count + hist_smooth[modal_intensity - index_bin]
                    index_bin += 1
                thresh = int(np.min((histo_size, modal_intensity + N * index_bin)))
                background_noise.append(bin_edges[thresh])
            elif N == 0:
                background_noise.append(bin_edges[modal_intensity])

        background_noise_smooth = [
            np.mean(background_noise[i - ws : i + ws])
            for i in range(ws, len(background_noise) - ws)
        ]
        # keep background noise at the end to avoid last row problem
        # (last bin with old microphones)
        background_noise_smooth = np.concatenate(
            (
                background_noise[0:(ws)],
                background_noise_smooth,
                background_noise[-(ws):],
            )
        )

        new_spec = np.array([col - background_noise_smooth for col in spectro.T]).T
        # replace negative values by value close to zero
        new_spec = new_spec.clip(min=low_value)

        return new_spec

    def __str__(self):
        string = "Spectrogram with fft: {0}, shape {1} and value \n {2}".format(
            self["n_fft"], self.spec.shape, self.spec
        )
        return string
