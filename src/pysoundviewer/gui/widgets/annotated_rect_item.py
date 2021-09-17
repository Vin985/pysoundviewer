from PySide6 import QtCore, QtGui

from pyqtextra.graphics.info_rect_item import InfoRectItem


class AnnotatedRectItem(InfoRectItem):

    RESIZE_COLOR = "#32ffffff"
    SELECTED_COLOR = "#ffffffff"
    BG_SUFFIX = " (bg)"
    BG_COLOR = "#bbb4b4b4"
    FG_COLOR = "#00ffffff"
    DEFAULT_BORDER_COLOR = "#000000"
    # NOISE_RAIN = 1
    # NOISE_WIND = 2

    def __init__(self, opts, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.opts = opts
        self.id = opts.get("id", None)
        self._background = opts.get("background", False)
        self._selected = False
        self.overlap = []

        self.text_opts = {"fontsize": opts.get("text_fontsize", 12)}

        self.colors = {
            "border": opts.get(
                "border_color", opts.get("color", self.DEFAULT_BORDER_COLOR)
            ),
            "fill": opts.get("fill_color", opts.get("color", None)),
            "text": opts.get("text_color", opts.get("color", None)),
            "background": opts.get("background_color", self.BG_COLOR),
            "resize": opts.get("resize_color", self.RESIZE_COLOR),
        }

        self.setResizeBoxColor(self.colors["resize"])
        self.create_rect()

    @property
    def selected(self):
        return self._selected

    @selected.setter
    def selected(self, selected):
        self._selected = selected
        if selected:
            self.current_color = self.SELECTED_COLOR
        else:
            self.current_color = self.label_class.color
        self.setRectColor(self.current_color)

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, background):
        self._background = background
        # info_string = self.infoString
        if background:
            # info_string += self.BG_SUFFIX
            self.setBrush(QtGui.QBrush(self.BG_COLOR, QtCore.Qt.BDiagPattern))
        else:
            # info_string = info_string.replace(self.BG_SUFFIX, "")
            self.setBrush(QtGui.QBrush(self.FG_COLOR, QtCore.Qt.SolidPattern))
        # self.setInfoString(info_string)

    def create_rect(self):
        rect = self.rect()
        coords = self.opts.get("coords", None)
        if not coords:
            raise ValueError(
                "The opts argument should at least contain a coords key with the",
                "coordinates of the rectitem",
            )

        self.setInfoString(self.opts.get("text", ""))
        self.set_colors()
        # print(coords, self.opts.get("text", "event"))
        self.setRect(*coords)

    def update_infostring(self):
        info_string = ".".join([str(self.id), self.label])
        self.setInfoString(info_string)

    def set_colors(self):
        self.setRectColor(color=self.colors["border"])
        if self.colors["fill"]:
            self.setBrush(QtGui.QBrush(self.colors["fill"], QtCore.Qt.SolidPattern))
        self.setupInfoTextItem(
            fontSize=self.text_opts["fontsize"], color=self.colors["text"]
        )

    def duration(self):
        return round(self.end - self.start, 3)

    def update(self):
        self.update_infostring()
        self.update_color()

    def get_overlaps(self):
        intersects = self.collidingItems()
        overlaps = [
            str(item.id) for item in intersects if isinstance(item, self.__class__)
        ]
        return overlaps

    def getBoxCoordinates(self):
        """
        Function which parses coordinates of bounding boxes in .json files to
        x1, x2, y1, and y2 objects.
        Takes account of different methods of drawing bounding boxes,
        so that coordinates are correct regardless of how bounding boxes are drawn.
        Also takes account of boxes that are accidently drawn outside of the spectrogram.

        """

        r = [
            self.sceneBoundingRect().x(),
            self.sceneBoundingRect().y(),
            self.sceneBoundingRect().width(),
            self.sceneBoundingRect().height(),
        ]
        # Get x coordinates. r[2] is the width of the box
        if r[2] > 0:
            x1 = r[0]
            x2 = r[0] + r[2]
        else:
            x1 = r[0] + r[2]
            x2 = r[0]

        # Get y coordinates. r[3] is the height of the box
        if r[3] > 0:
            y1 = r[1]
            y2 = r[1] + r[3]
        else:
            y1 = r[1] + r[3]
            y2 = r[1]

        if x1 < 0:
            x1 = 0
        if y1 < 0:
            y1 = 0
        if y2 > self.spec_opts["height"]:
            y2 = self.spec_opts["height"]
        # Transform y coordinates
        # y1 = (y1 - SpecRows)#*-1
        # y2 = (y2 - SpecRows)#*-1

        return x1, x2, y1, y2
