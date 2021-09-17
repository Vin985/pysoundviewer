from functools import partial

from PySide6 import QtCore

from .options_widget import OptionsWidget
from ...image import ImageOptions
from .ui.image_options_ui import Ui_ImageOptions


class ImageOptionsWidget(OptionsWidget, Ui_ImageOptions):
    def __init__(self, parent, options=None):
        super().__init__(parent, self, options)
        self.gridLayout.setAlignment(QtCore.Qt.AlignTop)
        self.group = ImageOptions.TYPE

    def link_events(self):
        self.cb_invert_colors.stateChanged.connect(
            partial(self.update, "invert_colors", checkbox=True)
        )
        self.spin_pix_in_sec.valueChanged.connect(partial(self.update, "pixels_in_sec"))
        self.spin_height.valueChanged.connect(partial(self.update, "height"))
        self.combo_color_map.currentTextChanged.connect(
            partial(self.update, "color_map")
        )
        self.slider_contrast.valueChanged.connect(partial(self.update, "contrast"))

    # associate a fonction to update a value from a specific ui element
    # Used for updating the ui from the settings
    def map_update_ui_functions(self):
        res = {
            "invert_colors": partial(self.update_checkbox, self.cb_invert_colors),
            "pixels_in_sec": partial(self.update_spinbox, self.spin_pix_in_sec),
            "height": partial(self.update_spinbox, self.spin_height),
            "color_map": partial(
                self.update_combobox,
                self.combo_color_map,
                ImageOptions.ACCEPTED_VALUES["color_map"],
            ),
            "contrast": partial(self.update_slider, self.slider_contrast),
        }
        return res
