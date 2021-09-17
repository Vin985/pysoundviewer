# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spectrogram_viewer.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_SpectrogramViewer(object):
    def setupUi(self, SpectrogramViewer):
        if not SpectrogramViewer.objectName():
            SpectrogramViewer.setObjectName(u"SpectrogramViewer")
        SpectrogramViewer.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SpectrogramViewer.sizePolicy().hasHeightForWidth())
        SpectrogramViewer.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(SpectrogramViewer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.spectrogram_view = QGraphicsView(SpectrogramViewer)
        self.spectrogram_view.setObjectName(u"spectrogram_view")

        self.horizontalLayout.addWidget(self.spectrogram_view)


        self.retranslateUi(SpectrogramViewer)

        QMetaObject.connectSlotsByName(SpectrogramViewer)
    # setupUi

    def retranslateUi(self, SpectrogramViewer):
        SpectrogramViewer.setWindowTitle(QCoreApplication.translate("SpectrogramViewer", u"Form", None))
    # retranslateUi

