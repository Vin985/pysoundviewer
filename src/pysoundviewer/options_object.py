class OptionsObject:

    DEFAULT_OPTIONS = {}

    def __init__(self, options=None):
        self._options = options or {}

    def __getitem__(self, index):
        return self._options.get(index, self.DEFAULT_OPTIONS[index])
        # if index in self._options:
        #     return self._options[index]
        # if index in self.DEFAULT_OPTIONS:
        #     return self.DEFAULT_OPTIONS[index]
        # raise KeyError(str(index) + " option does not exist")

    def __setitem__(self, index, value):
        self._options[index] = value

    def items(self):
        return self._options.items()

    def __str__(self):
        return str(self.__class__) + " with values: " + str(self._options)

    def add_missing_options(self):
        for key, value in self.DEFAULT_OPTIONS.items():
            if key not in self._options:
                self._options[key] = value
