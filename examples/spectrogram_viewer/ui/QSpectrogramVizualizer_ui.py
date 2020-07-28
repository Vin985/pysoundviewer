# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'QSpectrogramVizualizer.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from pysoundplayer.gui.QSoundPlayer import QSoundPlayer
from pysoundplayer.gui.QImageOptions import QImageOptions
from pysoundplayer.gui.QSpectrogramViewer import QSpectrogramViewer
from pysoundplayer.gui.QSpectrogramOptions import QSpectrogramOptions


class Ui_QSpectrogramVizualizer(object):
    def setupUi(self, QSpectrogramVizualizer):
        if QSpectrogramVizualizer.objectName():
            QSpectrogramVizualizer.setObjectName(u"QSpectrogramVizualizer")
        QSpectrogramVizualizer.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(QSpectrogramVizualizer.sizePolicy().hasHeightForWidth())
        QSpectrogramVizualizer.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(QSpectrogramVizualizer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.spectrogram_viewer = QSpectrogramViewer(QSpectrogramVizualizer)
        self.spectrogram_viewer.setObjectName(u"spectrogram_viewer")
        sizePolicy.setHeightForWidth(self.spectrogram_viewer.sizePolicy().hasHeightForWidth())
        self.spectrogram_viewer.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.spectrogram_viewer)

        self.sound_player = QSoundPlayer(QSpectrogramVizualizer)
        self.sound_player.setObjectName(u"sound_player")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.sound_player.sizePolicy().hasHeightForWidth())
        self.sound_player.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.sound_player)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(QSpectrogramVizualizer)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.spectrogram_options = QSpectrogramOptions(self.groupBox)
        self.spectrogram_options.setObjectName(u"spectrogram_options")

        self.horizontalLayout_2.addWidget(self.spectrogram_options)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(QSpectrogramVizualizer)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.image_options = QImageOptions(self.groupBox_2)
        self.image_options.setObjectName(u"image_options")

        self.horizontalLayout_3.addWidget(self.image_options)


        self.horizontalLayout.addWidget(self.groupBox_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(QSpectrogramVizualizer)

        QMetaObject.connectSlotsByName(QSpectrogramVizualizer)
    # setupUi

    def retranslateUi(self, QSpectrogramVizualizer):
        QSpectrogramVizualizer.setWindowTitle(QCoreApplication.translate("QSpectrogramVizualizer", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("QSpectrogramVizualizer", u"Spectrogram", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("QSpectrogramVizualizer", u"Image", None))
    # retranslateUi

