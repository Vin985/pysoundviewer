# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spectrogram_options.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_SpectrogramOptions(object):
    def setupUi(self, SpectrogramOptions):
        if not SpectrogramOptions.objectName():
            SpectrogramOptions.setObjectName(u"SpectrogramOptions")
        SpectrogramOptions.resize(480, 161)
        self.gridLayout = QGridLayout(SpectrogramOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.cb_pcen = QCheckBox(SpectrogramOptions)
        self.cb_pcen.setObjectName(u"cb_pcen")

        self.gridLayout.addWidget(self.cb_pcen, 1, 0, 1, 1)

        self.combo_hop_length = QComboBox(SpectrogramOptions)
        self.combo_hop_length.setObjectName(u"combo_hop_length")

        self.gridLayout.addWidget(self.combo_hop_length, 10, 1, 1, 1)

        self.cb_follow_sound = QCheckBox(SpectrogramOptions)
        self.cb_follow_sound.setObjectName(u"cb_follow_sound")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_follow_sound.sizePolicy().hasHeightForWidth())
        self.cb_follow_sound.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.cb_follow_sound, 0, 0, 1, 1)

        self.combo_fft = QComboBox(SpectrogramOptions)
        self.combo_fft.setObjectName(u"combo_fft")

        self.gridLayout.addWidget(self.combo_fft, 6, 1, 1, 1)

        self.label_38 = QLabel(SpectrogramOptions)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout.addWidget(self.label_38, 10, 2, 1, 1)

        self.label_37 = QLabel(SpectrogramOptions)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout.addWidget(self.label_37, 6, 2, 1, 1)

        self.label_39 = QLabel(SpectrogramOptions)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout.addWidget(self.label_39, 10, 0, 1, 1)

        self.cb_todb = QCheckBox(SpectrogramOptions)
        self.cb_todb.setObjectName(u"cb_todb")

        self.gridLayout.addWidget(self.cb_todb, 1, 2, 1, 1)

        self.combo_scale = QComboBox(SpectrogramOptions)
        self.combo_scale.setObjectName(u"combo_scale")

        self.gridLayout.addWidget(self.combo_scale, 6, 3, 1, 1)

        self.cb_remove_noise = QCheckBox(SpectrogramOptions)
        self.cb_remove_noise.setObjectName(u"cb_remove_noise")

        self.gridLayout.addWidget(self.cb_remove_noise, 1, 1, 1, 1)

        self.label_40 = QLabel(SpectrogramOptions)
        self.label_40.setObjectName(u"label_40")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.label_40, 6, 0, 1, 1)

        self.label_41 = QLabel(SpectrogramOptions)
        self.label_41.setObjectName(u"label_41")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy2)
        self.label_41.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_41, 16, 0, 1, 1)

        self.combo_specType = QComboBox(SpectrogramOptions)
        self.combo_specType.addItem("")
        self.combo_specType.addItem("")
        self.combo_specType.setObjectName(u"combo_specType")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.combo_specType.sizePolicy().hasHeightForWidth())
        self.combo_specType.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.combo_specType, 16, 1, 1, 1)

        self.cb_normalize = QCheckBox(SpectrogramOptions)
        self.cb_normalize.setObjectName(u"cb_normalize")

        self.gridLayout.addWidget(self.cb_normalize, 1, 3, 1, 1)

        self.combo_window = QComboBox(SpectrogramOptions)
        self.combo_window.setObjectName(u"combo_window")

        self.gridLayout.addWidget(self.combo_window, 10, 3, 1, 1)


        self.retranslateUi(SpectrogramOptions)

        QMetaObject.connectSlotsByName(SpectrogramOptions)
    # setupUi

    def retranslateUi(self, SpectrogramOptions):
        SpectrogramOptions.setWindowTitle(QCoreApplication.translate("SpectrogramOptions", u"Form", None))
        self.cb_pcen.setText(QCoreApplication.translate("SpectrogramOptions", u"Use PCEN", None))
        self.cb_follow_sound.setText(QCoreApplication.translate("SpectrogramOptions", u"follow sound", None))
        self.label_38.setText(QCoreApplication.translate("SpectrogramOptions", u"Window type", None))
        self.label_37.setText(QCoreApplication.translate("SpectrogramOptions", u"Scale", None))
        self.label_39.setText(QCoreApplication.translate("SpectrogramOptions", u"hop length", None))
        self.cb_todb.setText(QCoreApplication.translate("SpectrogramOptions", u"To dB", None))
        self.cb_remove_noise.setText(QCoreApplication.translate("SpectrogramOptions", u"Remove noise", None))
        self.label_40.setText(QCoreApplication.translate("SpectrogramOptions", u"n_fft", None))
        self.label_41.setText(QCoreApplication.translate("SpectrogramOptions", u"spectrogram type:", None))
        self.combo_specType.setItemText(0, QCoreApplication.translate("SpectrogramOptions", u"audible range", None))
        self.combo_specType.setItemText(1, QCoreApplication.translate("SpectrogramOptions", u"ultra sonic range", None))

        self.cb_normalize.setText(QCoreApplication.translate("SpectrogramOptions", u"Normalize", None))
    # retranslateUi

