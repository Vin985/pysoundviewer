import ast
import logging

from PySide6.QtCore import QSettings
from ..spectrogram import SpectrogramOptions
from ..image import ImageOptions


class SoundPlayerSettings(QSettings):

    GROUP_SPECTROGRAM = SpectrogramOptions.TYPE
    GROUP_IMAGE = ImageOptions.TYPE

    def __init__(self):
        super().__init__()
        self.options = {
            self.GROUP_SPECTROGRAM: self.spectrogram_settings(),
            self.GROUP_IMAGE: self.image_settings(),
        }
        # self.all_settings()
        # self.save_group(self.GROUP_SPECTROGRAM, self.options["spectrogram"])
        # self.save_group(self.GROUP_IMAGE, self.options[self.GROUP_IMAGE])

    def all_settings(self):
        res = {}
        for key in self.allKeys():
            res[key] = self.value(key)
        return res

    @property
    def spectrogram_options(self):
        return self.options[self.GROUP_SPECTROGRAM]

    @property
    def image_options(self):
        return self.options[self.GROUP_IMAGE]

    def get(self, key, default):
        default = repr(default)
        tmp = self.value(key, default)
        if tmp is None:
            return tmp
        return ast.literal_eval(tmp)

    def save(self, key, value):
        self.setValue(key, value)
        self.sync()

    def save_group(self, group_name, values):
        self.beginGroup(group_name)
        for key, value in values.items():
            self.save(key, value)
        self.endGroup()
        self.sync()

    def setValue(self, key, value):
        valrepr = repr(value)
        try:
            assert value == ast.literal_eval(valrepr)
        except (ValueError, AssertionError, SyntaxError):
            raise ValueError(
                (
                    "Value too complex to store."
                    " Can only store values for which x == ast.literal_eval(repr(x))"
                )
            )
        super().setValue(key, valrepr)

    # def group_to_dict(self, group=""):
    #     opts = {}
    #     self.beginGroup(group)
    #     for key in self.childKeys():
    #         if key.startswith("__"):
    #             continue
    #         opts[key] = self.get(key, group)
    #     self.endGroup()
    #     return opts

    def get_spec_setting(self, key):
        return self.get(key, self.GROUP_SPECTROGRAM)

    def get_image_setting(self, key):
        return self.get(key, self.GROUP_IMAGE)

    def spectrogram_settings(self, context=""):
        print("spectrogram settings")
        group = self.GROUP_SPECTROGRAM
        res = SpectrogramOptions()
        if context:
            context = "/" + context
        self.beginGroup(group + context)
        if context and not self.childKeys():
            logging.info("No entries found for selected context, using default group")
            self.endGroup()
            self.beginGroup(group)
        for key in self.childKeys():
            res[key] = self.get(key, res.DEFAULT_OPTIONS[key])
        self.endGroup()
        res.add_missing_options()
        return res

    def image_settings(self):
        res = ImageOptions()
        self.beginGroup(self.GROUP_IMAGE)
        for key in self.childKeys():
            res[key] = self.get(key, res.DEFAULT_OPTIONS[key])
        self.endGroup()
        res.add_missing_options()
        return res
