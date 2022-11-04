# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spectrogram_viewer_example.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QMainWindow,
    QMenuBar, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

from pysoundplayer.widget.sound_player_widget import SoundPlayerWidget
from pysoundviewer.gui.widgets.image_options_widget import ImageOptionsWidget
from pysoundviewer.gui.widgets.spectrogram_options_widget import SpectrogramOptionsWidget
from pysoundviewer.gui.widgets.spectrogram_viewer import SpectrogramViewer

class Ui_SpectrogramViewerExample(object):
    def setupUi(self, SpectrogramViewerExample):
        if not SpectrogramViewerExample.objectName():
            SpectrogramViewerExample.setObjectName(u"SpectrogramViewerExample")
        SpectrogramViewerExample.resize(800, 600)
        self.centralwidget = QWidget(SpectrogramViewerExample)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.spectrogram_viewer = SpectrogramViewer(self.centralwidget)
        self.spectrogram_viewer.setObjectName(u"spectrogram_viewer")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spectrogram_viewer.sizePolicy().hasHeightForWidth())
        self.spectrogram_viewer.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.spectrogram_viewer)

        self.sound_player = SoundPlayerWidget(self.centralwidget)
        self.sound_player.setObjectName(u"sound_player")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sound_player.sizePolicy().hasHeightForWidth())
        self.sound_player.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.sound_player)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.spectrogram_options = SpectrogramOptionsWidget(self.groupBox)
        self.spectrogram_options.setObjectName(u"spectrogram_options")

        self.horizontalLayout_2.addWidget(self.spectrogram_options)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.image_options = ImageOptionsWidget(self.groupBox_2)
        self.image_options.setObjectName(u"image_options")

        self.horizontalLayout_3.addWidget(self.image_options)


        self.horizontalLayout.addWidget(self.groupBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        SpectrogramViewerExample.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SpectrogramViewerExample)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        SpectrogramViewerExample.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SpectrogramViewerExample)
        self.statusbar.setObjectName(u"statusbar")
        SpectrogramViewerExample.setStatusBar(self.statusbar)

        self.retranslateUi(SpectrogramViewerExample)

        QMetaObject.connectSlotsByName(SpectrogramViewerExample)
    # setupUi

    def retranslateUi(self, SpectrogramViewerExample):
        SpectrogramViewerExample.setWindowTitle(QCoreApplication.translate("SpectrogramViewerExample", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("SpectrogramViewerExample", u"Spectrogram", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("SpectrogramViewerExample", u"Image", None))
    # retranslateUi

