# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'image_options.ui'
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


class Ui_ImageOptions(object):
    def setupUi(self, ImageOptions):
        if not ImageOptions.objectName():
            ImageOptions.setObjectName(u"ImageOptions")
        ImageOptions.resize(400, 160)
        self.gridLayout = QGridLayout(ImageOptions)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_33 = QLabel(ImageOptions)
        self.label_33.setObjectName(u"label_33")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_33, 0, 0, 1, 1)

        self.combo_color_map = QComboBox(ImageOptions)
        self.combo_color_map.setObjectName(u"combo_color_map")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.combo_color_map.sizePolicy().hasHeightForWidth())
        self.combo_color_map.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.combo_color_map, 0, 1, 1, 1)

        self.label_36 = QLabel(ImageOptions)
        self.label_36.setObjectName(u"label_36")
        sizePolicy.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.label_36, 1, 0, 1, 1)

        self.slider_contrast = QSlider(ImageOptions)
        self.slider_contrast.setObjectName(u"slider_contrast")
        sizePolicy1.setHeightForWidth(self.slider_contrast.sizePolicy().hasHeightForWidth())
        self.slider_contrast.setSizePolicy(sizePolicy1)
        self.slider_contrast.setMinimum(0)
        self.slider_contrast.setMaximum(5)
        self.slider_contrast.setSingleStep(5)
        self.slider_contrast.setTracking(False)
        self.slider_contrast.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.slider_contrast, 1, 1, 1, 1)

        self.label_35 = QLabel(ImageOptions)
        self.label_35.setObjectName(u"label_35")
        sizePolicy.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy)
        self.label_35.setWordWrap(True)

        self.gridLayout.addWidget(self.label_35, 2, 0, 1, 1)

        self.spin_pix_in_sec = QSpinBox(ImageOptions)
        self.spin_pix_in_sec.setObjectName(u"spin_pix_in_sec")
        sizePolicy1.setHeightForWidth(self.spin_pix_in_sec.sizePolicy().hasHeightForWidth())
        self.spin_pix_in_sec.setSizePolicy(sizePolicy1)
        self.spin_pix_in_sec.setKeyboardTracking(False)
        self.spin_pix_in_sec.setMinimum(0)
        self.spin_pix_in_sec.setMaximum(999)

        self.gridLayout.addWidget(self.spin_pix_in_sec, 2, 1, 1, 1)

        self.label_34 = QLabel(ImageOptions)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout.addWidget(self.label_34, 3, 0, 1, 1)

        self.spin_height = QSpinBox(ImageOptions)
        self.spin_height.setObjectName(u"spin_height")
        sizePolicy1.setHeightForWidth(self.spin_height.sizePolicy().hasHeightForWidth())
        self.spin_height.setSizePolicy(sizePolicy1)
        self.spin_height.setKeyboardTracking(False)
        self.spin_height.setMaximum(999)

        self.gridLayout.addWidget(self.spin_height, 3, 1, 1, 1)

        self.cb_invert_colors = QCheckBox(ImageOptions)
        self.cb_invert_colors.setObjectName(u"cb_invert_colors")

        self.gridLayout.addWidget(self.cb_invert_colors, 4, 0, 1, 1)


        self.retranslateUi(ImageOptions)

        QMetaObject.connectSlotsByName(ImageOptions)
    # setupUi

    def retranslateUi(self, ImageOptions):
        ImageOptions.setWindowTitle(QCoreApplication.translate("ImageOptions", u"Form", None))
        self.label_33.setText(QCoreApplication.translate("ImageOptions", u"Color map", None))
        self.label_36.setText(QCoreApplication.translate("ImageOptions", u"Color contrast", None))
        self.label_35.setText(QCoreApplication.translate("ImageOptions", u"Number of pixels in a second", None))
        self.label_34.setText(QCoreApplication.translate("ImageOptions", u"Height", None))
        self.cb_invert_colors.setText(QCoreApplication.translate("ImageOptions", u"Invert colors", None))
    # retranslateUi

