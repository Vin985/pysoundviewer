from PySide6 import QtCore


class SpectrogramMouseFilter(QtCore.QObject):  # And this one
    def __init__(self, parent):
        QtCore.QObject.__init__(self)
        self.parent = parent

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.GraphicsSceneMouseRelease:
            if event.button() == QtCore.Qt.MiddleButton:
                self.parent.seek_sound(event.scenePos().x())

        elif event.type() == QtCore.QEvent.GraphicsSceneWheel:
            if event.modifiers() == QtCore.Qt.ControlModifier:
                if event.delta() > 0:
                    self.parent.zoom(1.1, event.scenePos())
                else:
                    self.parent.zoom(0.9, event.scenePos())
                event.setAccepted(True)
                return True

        return False
