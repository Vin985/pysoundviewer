from functools import partial

from PySide2 import QtCore

from .ui.spectrogram_options_ui import Ui_SpectrogramOptions
from ...spectrogram import SpectrogramOptions
from .options_widget import OptionsWidget


class SpectrogramOptionsWidget(OptionsWidget, Ui_SpectrogramOptions):
    def __init__(self, parent, options=None):
        super().__init__(parent, self, options)
        self.gridLayout.setAlignment(QtCore.Qt.AlignTop)
        self.group = SpectrogramOptions.TYPE

    def link_events(self):
        # Spectrogram
        self.cb_pcen.stateChanged.connect(self.use_pcen)
        self.cb_remove_noise.stateChanged.connect(
            partial(self.update, "remove_noise", checkbox=True)
        )
        self.cb_normalize.stateChanged.connect(
            partial(self.update, "normalize", checkbox=True)
        )
        self.cb_todb.stateChanged.connect(partial(self.update, "to_db", checkbox=True))
        self.combo_fft.currentTextChanged.connect(partial(self.update, "n_fft"))
        self.combo_scale.currentTextChanged.connect(partial(self.update, "scale"))
        # self.combo_hop_length.currentTextChanged.connect(
        #     partial(self.update, "hop_length")
        # )
        self.combo_window.currentTextChanged.connect(partial(self.update, "window"))
        self.cb_follow_sound.stateChanged.connect(
            partial(self.update, "follow_sound", checkbox=True, redraw=False)
        )

    # associate a fonction to update a value from a specific ui element
    # Used for updating the ui from the settings

    def map_update_ui_functions(self):
        res = {
            "to_db": partial(self.update_checkbox, self.cb_todb),
            "pcen": partial(self.update_checkbox, self.cb_pcen),
            "remove_noise": partial(self.update_checkbox, self.cb_remove_noise),
            "scale": partial(
                self.update_combobox,
                self.combo_scale,
                SpectrogramOptions.ACCEPTED_VALUES["scale"],
            ),
            # "hop_length": partial(
            #     self.update_combobox,
            #     self.combo_hop_length,
            #     SpectrogramOptions.ACCEPTED_VALUES["hop_length"],
            # ),
            "n_fft": partial(
                self.update_combobox,
                self.combo_fft,
                SpectrogramOptions.ACCEPTED_VALUES["n_fft"],
            ),
            "window": partial(
                self.update_combobox,
                self.combo_window,
                SpectrogramOptions.ACCEPTED_VALUES["window"],
            ),
        }
        return res

    def use_pcen(self, value):
        use_pcen = value == QtCore.Qt.CheckState.Checked
        self.cb_remove_noise.setEnabled(not use_pcen)
        self.update("pcen", use_pcen)
