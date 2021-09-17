from PySide6 import QtCore, QtWidgets


class OptionsWidget(QtWidgets.QWidget):

    option_updated = QtCore.Signal(str, bool)

    def __init__(self, parent, ui, options=None):
        super().__init__(parent)
        self.setupUi(ui)
        self.group = ""
        self._options = None
        if options:
            self.options = options
        self.update_ui = self.map_update_ui_functions()
        self.link_events()

    @property
    def options(self):
        if not self._options:
            try:
                settings = getattr(qApp, "settings")
                if settings:
                    self.options = settings.get_options(self.group)
            except Exception as e:
                print(e)
                raise AttributeError(
                    "No options found for "
                    + str(type(self))
                    + ". Please either set the options manually"
                    + " or make them available as an attribute in the"
                    + "main QApplication."
                )
        return self._options

    @options.setter
    def options(self, options):
        if options:
            self._options = options
            self.init_values()

    def map_update_ui_functions(self):
        return {}

    def update(self, option, value, checkbox=False, redraw=True):
        if checkbox:
            value = value == QtCore.Qt.CheckState.Checked
        self.options[option] = value
        self.option_updated.emit(option, redraw)

    @staticmethod
    def update_checkbox(checkbox, value):
        checkbox.setChecked(value)

    @staticmethod
    def update_spinbox(spinbox, value):
        spinbox.setValue(value)

    @staticmethod
    def update_slider(slider, value):
        slider.setValue(value)

    @staticmethod
    def update_combobox(combobox, choices, value):
        if combobox.count() == 0:
            combobox.insertItems(0, choices)
        combobox.setCurrentText(str(value))

    def init_values(self):
        for key, value in self.options.items():
            if key in self.update_ui:
                self.update_ui[key](value)
            else:
                print("Option not mapped: " + key)
