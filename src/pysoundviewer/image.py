import functools
import itertools

import colorcet as cc
import numpy as np
import webcolors
from PIL import Image, ImageEnhance, ImageOps

from .options_object import OptionsObject


class ImageOptions(OptionsObject):
    DEFAULT_OPTIONS = {
        "color_masks_str": ["red", "lime", "blue"],
        "composite_ffts": [128, 512, 2048],
        "contrast": 0,
        "invert_colors": False,
        "height": 400,
        "pixels_per_sec": 200,
        "color_map": "rainbow",
    }

    ACCEPTED_VALUES = {
        "color_map": [key for key in cc.cm.keys() if len(key.split("_")) == 1]
    }

    TYPE = "image"

    def __init__(self, image_options=None):
        super().__init__(options=image_options)


class ImageGenerator:
    def __init__(self, image_options=None):
        self.options = image_options
        self._color_masks = None

    def __getitem__(self, key):
        return self.options[key]

    @property
    def color_masks(self):
        if self._color_masks is None:
            self._color_masks = [
                self.__get_color_rgb(col) for col in self["color_masks_str"]
            ]
        return self._color_masks

    def __get_color_rgb(self, color):
        if isinstance(color, tuple):
            return color
        elif isinstance(color, str):
            return webcolors.name_to_rgb(color)

    # Prepare spectrograms to generate image
    def __prepare_spectrogram(self, spec):
        # Make sure spectrogram is in float32 because pillow doesn't
        # support float64
        spec = spec.astype("float32")
        # Normalize spectrogram in [0:1]
        # TODO: use librosa normalize?
        spec_min = spec.min(axis=None)
        spec_max = spec.max(axis=None)
        spec -= spec_min
        spec /= spec_max - spec_min
        # spec = librosa.util.normalize(spec)
        if self["invert_colors"]:
            spec = 1 - spec
        spec = cc.cm[self["color_map"]](spec)
        # spec = cm.get_cmap("Reds")(spec)
        # spec = getColourMap()(spec)
        spec = spec * 255
        # flip upside down since writing image start from top left
        spec = np.flipud(spec)
        return np.uint8(spec)

    def spec2img(
        self, spectrogram, size=-1, resize_method=Image.BILINEAR, is_array=False
    ):

        if not is_array:
            spec = spectrogram.spec
        else:
            spec = spectrogram

        spec = self.__prepare_spectrogram(spec)

        img = Image.fromarray(spec)

        # enhance contrast
        if self["contrast"]:
            if self["contrast"] == -1:
                img = ImageOps.autocontrast(img)
            else:
                c_enh = ImageEnhance.Contrast(img)
                img = c_enh.enhance(self["contrast"])

        if size == -1:
            size = (self.sec2pixels(spectrogram.duration), self["height"])

        if size is not None:
            img = img.resize(size, resize_method)

        return img

    def create_composite_part(self, spec, color_mask):
        img = self.spec2img(spec, color_mask)
        return np.asarray(img)

    def generate_composite(self, sample):
        # TODO: more checks
        if len(self["composite_ffts"]) != 3:
            print(
                "3 spectrograms sizes must be provided in the "
                " composite_ffts option in the configuration file"
            )
            return ()
        specs = [
            sample.get_spectrogram({"n_fft": fft}) for fft in self["composite_ffts"]
        ]
        res = itertools.starmap(
            self.create_composite_part, zip(specs, self.color_masks)
        )
        res = functools.reduce(np.add, res)
        composite = Image.fromarray(res, mode="RGB")
        return composite

    def sec2pixels(self, sec, to_int=True):
        pix = self["pixels_per_sec"] * sec
        if to_int:
            return int(pix)
        return pix

    def pixels2sec(self, pixels):
        sec = pixels / self["pixels_per_sec"]
        return sec
