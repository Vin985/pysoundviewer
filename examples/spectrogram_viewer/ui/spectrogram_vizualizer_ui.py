# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spectrogram_vizualizer.ui'
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

from pysoundplayer.gui.QSpectrogramVizualizer import QSpectrogramVizualizer


class Ui_SpectrogramVizualizer(object):
    def setupUi(self, SpectrogramVizualizer):
        if SpectrogramVizualizer.objectName():
            SpectrogramVizualizer.setObjectName(u"SpectrogramVizualizer")
        SpectrogramVizualizer.resize(800, 600)
        self.centralwidget = QWidget(SpectrogramVizualizer)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.spectrogram_vizualizer = QSpectrogramVizualizer(self.centralwidget)
        self.spectrogram_vizualizer.setObjectName(u"spectrogram_vizualizer")

        self.verticalLayout.addWidget(self.spectrogram_vizualizer)

        SpectrogramVizualizer.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SpectrogramVizualizer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 23))
        SpectrogramVizualizer.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SpectrogramVizualizer)
        self.statusbar.setObjectName(u"statusbar")
        SpectrogramVizualizer.setStatusBar(self.statusbar)

        self.retranslateUi(SpectrogramVizualizer)

        QMetaObject.connectSlotsByName(SpectrogramVizualizer)
    # setupUi

    def retranslateUi(self, SpectrogramVizualizer):
        SpectrogramVizualizer.setWindowTitle(QCoreApplication.translate("SpectrogramVizualizer", u"MainWindow", None))
    # retranslateUi

