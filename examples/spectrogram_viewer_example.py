import sys

from PySide2.QtWidgets import QApplication, QMainWindow

from pysoundviewer.gui.settings import SoundPlayerSettings

from spectrogram_viewer_example_ui import Ui_SpectrogramViewerExample


class SpectrogramViewerExample(QMainWindow, Ui_SpectrogramViewerExample):
    def __init__(self):
        super().__init__()

        # Usual setup stuff. Set up the user interface from Designer
        self.setupUi(self)

        self.settings = SoundPlayerSettings()
        self.share_settings()

        self.link_events()

    def load_file(self, path):
        audio = self.sound_player.load_file(file_path=path)
        self.spectrogram_viewer.audio = audio
        return audio

    def share_settings(self):
        self.spectrogram_viewer.settings = self.settings
        self.spectrogram_options.options = self.settings.spectrogram_options
        self.image_options.options = self.settings.image_options

    def link_events(self):
        self.sound_player.update_position.connect(
            self.spectrogram_viewer.update_sound_marker
        )
        self.spectrogram_viewer.seek.connect(self.sound_player.seek)
        self.image_options.option_updated.connect(self.spectrogram_viewer.update_image)
        self.spectrogram_options.option_updated.connect(
            self.spectrogram_viewer.update_spectrogram
        )

    def show_text(self, text):
        self.spectrogram_viewer.display_text(text)

    def draw_rect(self, *args, **kwargs):
        self.spectrogram_viewer.draw_rect(*args, **kwargs)

    def clear_rects(self):
        self.spectrogram_viewer.clear_rects()


def main():
    app = QApplication(sys.argv)
    app.setOrganizationName("ecosongs")
    app.setOrganizationDomain("https://github.com/vin985/pysoundplayer")
    app.setApplicationName("pysoundplayer")
    example = SpectrogramViewerExample()
    example.load_file("example.wav")

    tag1 = {
        "start": 1.5,
        "end": 3,
        "text": "this is a test",
        "border_color": "#ff0000",
        "fill_color": "#00ff00",
        "text_fontsize": 24,
    }

    tag2 = {
        "start": 10,
        "end": 20,
        "min_freq": 1000,
        "max_freq": 5000,
        "text": "frequency test",
        # "text_color": "#000000",
        "color": "#ff00ff",
    }

    example.spectrogram_viewer.draw_annotation(tag1)
    example.spectrogram_viewer.draw_annotation(tag2)

    example.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
