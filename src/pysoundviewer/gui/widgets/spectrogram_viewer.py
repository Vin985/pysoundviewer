from PIL import ImageQt
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QGraphicsPixmapItem, QGraphicsScene, QGraphicsTextItem

from ...image import ImageGenerator
from ...spectrogram import Spectrogram
from ..event_filters import SpectrogramMouseFilter
from .annotated_rect_item import AnnotatedRectItem
from .ui.spectrogram_viewer_ui import Ui_SpectrogramViewer


class SpectrogramViewer(QtWidgets.QWidget, Ui_SpectrogramViewer):

    seek = QtCore.Signal(float)
    spectrogram_drawn = QtCore.Signal()

    def __init__(self, parent=None, audio=None, settings=None):
        super().__init__(parent)
        self.setupUi(self)
        self.bg_image = None
        self.spectrogram_scene = QGraphicsScene(self)

        self._audio = None
        self._spectrogram = None
        self._image_generator = None

        self.sound_marker = None
        self.marker_position = 0
        self.yscale = 1

        self.settings = settings

        self.audio = audio
        self.setup_graphics_view()
        self.define_shortcuts()
        self.install_filters()

    def setup_graphics_view(self):
        self.spectrogram_view.setScene(self.spectrogram_scene)

    def define_shortcuts(self):
        QtWidgets.QShortcut(
            QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_Plus), self, self.zoom_in
        )
        QtWidgets.QShortcut(
            QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_Minus),
            self,
            self.zoom_out,
        )

    def install_filters(self):
        self.mouse_filter = SpectrogramMouseFilter(self)
        self.spectrogram_scene.installEventFilter(self.mouse_filter)

    @property
    def audio(self):
        return self._audio

    @audio.setter
    def audio(self, audio):
        if audio is not None:
            self._audio = audio
            self.spectrogram = Spectrogram(audio, self.spectrogram_options)
            self.marker_position = 0

    @property
    def spectrogram(self):
        return self._spectrogram

    @spectrogram.setter
    def spectrogram(self, spectrogram):
        self._spectrogram = spectrogram
        self.display_spectrogram()

    @property
    def image_options(self):
        return self.settings.image_options if self.settings else {}

    @property
    def spectrogram_options(self):
        return self.settings.spectrogram_options if self.settings else {}

    @property
    def image_generator(self):
        if self._image_generator is None:
            self._image_generator = ImageGenerator(self.image_options)
        return self._image_generator

    def display_spectrogram(self):
        # TODO: save image somewhere
        im = self.image_generator.spec2img(self.spectrogram)
        # TODO: change events when checkbox is checked
        # if self.checkbox_draw_events.isChecked():
        #     im = self.draw_events(im, max_duration)
        img = ImageQt.ImageQt(im)
        pixmap = QtGui.QPixmap.fromImage(img)

        # Change Qt array to a Qt graphic
        self.bg_image = QGraphicsPixmapItem(pixmap)
        self.spectrogram_scene.clear()
        self.spectrogram_scene.addItem(self.bg_image)
        # Ensure spectrogram graphic is displayed as background
        self.bg_image.setZValue(-100)
        self.bg_image.setPos(0, 0)
        self.sound_marker = None
        if self.marker_position:
            self.update_sound_marker(None)
        self.spectrogram_drawn.emit()

    def display_text(self, text):
        text_item = QGraphicsTextItem()
        text_item.setPos(150, 100)
        text_item.setPlainText(text)
        self.spectrogram_scene.clear()
        self.spectrogram_scene.addItem(text_item)

    def update_sound_marker(self, position_sec):
        # 100 # multiply by step-size in SpecGen()
        if position_sec is not None:
            self.marker_position = self.image_generator.sec2pixels(position_sec)
        line = QtCore.QLineF(
            self.marker_position,
            0,
            self.marker_position,
            self.image_generator["height"],
        )
        if not self.sound_marker:
            penCol = QtGui.QColor()
            penCol.setRgb(255, 0, 0)
            self.sound_marker = self.spectrogram_scene.addLine(line, QtGui.QPen(penCol))
        else:
            self.sound_marker.setLine(line)

        self.spectrogram_scene.update()

        if self.spectrogram_options["follow_sound"]:
            self.center_view()

    def center_view(self):
        self.spectrogram_view.centerOn(self.marker_position, self.get_center().y())

    def zoom(self, scale, scene_pos=None):
        self.yscale *= scale
        self.spectrogram_view.scale(scale, scale)
        if scene_pos:
            self.spectrogram_view.centerOn(scene_pos)

    def zoom_in(self):
        self.zoom(1.5)

    def zoom_out(self):
        self.zoom(0.75)

    def seek_sound(self, pos):
        self.seek.emit(self.image_generator.pixels2sec(pos))

    def update_spectrogram(self, option, redraw):
        if redraw:
            self.spectrogram = Spectrogram(self.audio, self.spectrogram_options)
            self.freq2pixels(6000)

    def update_image(self, option, redraw):
        if redraw:
            self.display_spectrogram()

    def get_center(self):
        return self.spectrogram_view.mapToScene(
            self.spectrogram_view.viewport().rect().center()
        )

    def clear_rects(self):
        items = self.spectrogram_scene.items()
        for item in items:
            if isinstance(item, AnnotatedRectItem):
                self.spectrogram_scene.removeItem(item)

    def freq2pixels(self, freq):
        res = 0
        if self.spectrogram["scale"] == "Linear":
            height = self.image_generator["height"]
            max_freq = self.audio.sr / 2
            freq_step = height / max_freq
            res = height - (freq * freq_step)
        else:
            print("Only linear scale is supported so far")

        return res

    def draw_annotation(self, opts):
        x1 = self.image_generator.sec2pixels(opts.get("start", 0))
        x2 = self.image_generator.sec2pixels(opts.get("end", 0))
        y1 = self.freq2pixels(opts.get("max_freq", 0))
        y2 = self.freq2pixels(opts.get("min_freq", 0))
        text = opts.get("text", "")
        buffer = opts.get("vertical_buffer", 1)
        top_offset = opts.get("top_offset", 0)
        bottom_offset = opts.get("bottom_offset", 0)

        if y2 - y1 <= 0:
            y1 = 0
            y2 = self.spectrogram_scene.height() - 2
            if buffer:
                v_offset = buffer * y2 / 100
                y1 += v_offset + top_offset
                y2 -= v_offset - bottom_offset
                if text:
                    font = QtGui.QFont(
                        opts.get("text_font", ""), opts.get("text_fontsize", 12)
                    )
                    font_height = QtGui.QFontMetrics(font).height()
                    y1 += font_height

        coords = (x1, y1, x2 - x1, y2 - y1)

        opts["coords"] = coords

        rect = AnnotatedRectItem(opts)

        self.spectrogram_scene.addItem(rect)

    def draw_rect(self, start, end, y=0, height=-1, color="#ffffff", fill="", buffer=1):
        x = self.image_generator.sec2pixels(start)
        width = self.image_generator.sec2pixels(end - start)
        if height == -1:
            height = self.spectrogram_scene.height() - 2
        rect = QtWidgets.QGraphicsRectItem()
        rect.setPen(QtGui.QPen(color))
        if fill is not None:
            if not fill:
                fill = color
            rect.setBrush(QtGui.QBrush(fill, QtCore.Qt.SolidPattern))
        if buffer:
            y += buffer * height / 100
            height -= buffer * height / 100
        rect.setRect(x, y, width, height)
        self.spectrogram_scene.addItem(rect)
