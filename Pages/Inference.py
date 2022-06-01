# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Inference.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QLabel, QPushButton, QSizePolicy,
    QSplitter, QTabWidget, QWidget)
import assets_rc

class Ui_Inference(object):
    def setupUi(self, Inference):
        if not Inference.objectName():
            Inference.setObjectName(u"Inference")
        Inference.resize(720, 599)
        self.gridLayout = QGridLayout(Inference)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter_2 = QSplitter(Inference)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.splitter_2.setOpaqueResize(True)
        self.label = QLabel(self.splitter_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        font.setPointSize(12)
        self.label.setFont(font)
        self.splitter_2.addWidget(self.label)
        self.InferenceModels = QComboBox(self.splitter_2)
        self.InferenceModels.setObjectName(u"InferenceModels")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(12)
        self.InferenceModels.setFont(font1)
        self.splitter_2.addWidget(self.InferenceModels)
        self.SelectInferenceModel = QPushButton(self.splitter_2)
        self.SelectInferenceModel.setObjectName(u"SelectInferenceModel")
        self.SelectInferenceModel.setFont(font)
        self.splitter_2.addWidget(self.SelectInferenceModel)

        self.gridLayout.addWidget(self.splitter_2, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(Inference)
        self.tabWidget.setObjectName(u"tabWidget")
        font2 = QFont()
        font2.setFamilies([u"\u9ed1\u4f53"])
        font2.setPointSize(10)
        self.tabWidget.setFont(font2)
        self.Image = QWidget()
        self.Image.setObjectName(u"Image")
        self.gridLayout_4 = QGridLayout(self.Image)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.splitter_4 = QSplitter(self.Image)
        self.splitter_4.setObjectName(u"splitter_4")
        font3 = QFont()
        font3.setFamilies([u"\u9ed1\u4f53"])
        font3.setPointSize(1)
        self.splitter_4.setFont(font3)
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.splitter_4.setOpaqueResize(True)
        self.splitter_4.setHandleWidth(0)
        self.groupBox = QGroupBox(self.splitter_4)
        self.groupBox.setObjectName(u"groupBox")
        font4 = QFont()
        font4.setFamilies([u"\u9ed1\u4f53"])
        font4.setPointSize(13)
        self.groupBox.setFont(font4)
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.splitter_5 = QSplitter(self.groupBox)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setFont(font4)
        self.splitter_5.setOrientation(Qt.Vertical)
        self.splitter_5.setOpaqueResize(True)
        self.splitter_5.setHandleWidth(0)
        self.splitter = QSplitter(self.splitter_5)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(0)
        self.label_2 = QLabel(self.splitter)
        self.label_2.setObjectName(u"label_2")
        font5 = QFont()
        font5.setFamilies([u"\u9ed1\u4f53"])
        font5.setPointSize(11)
        self.label_2.setFont(font5)
        self.splitter.addWidget(self.label_2)
        self.CurrentImage = QLabel(self.splitter)
        self.CurrentImage.setObjectName(u"CurrentImage")
        font6 = QFont()
        font6.setFamilies([u"Times New Roman"])
        font6.setPointSize(11)
        self.CurrentImage.setFont(font6)
        self.splitter.addWidget(self.CurrentImage)
        self.splitter_5.addWidget(self.splitter)
        self.ShowSelectedImage = QLabel(self.splitter_5)
        self.ShowSelectedImage.setObjectName(u"ShowSelectedImage")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ShowSelectedImage.sizePolicy().hasHeightForWidth())
        self.ShowSelectedImage.setSizePolicy(sizePolicy)
        self.ShowSelectedImage.setPixmap(QPixmap(u":/emoji/Pages/assets/emoji/1.png"))
        self.ShowSelectedImage.setScaledContents(True)
        self.splitter_5.addWidget(self.ShowSelectedImage)

        self.gridLayout_2.addWidget(self.splitter_5, 0, 0, 1, 1)

        self.splitter_4.addWidget(self.groupBox)
        self.groupBox_2 = QGroupBox(self.splitter_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font4)
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)

        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)

        self.ShowFaceImage = QLabel(self.groupBox_2)
        self.ShowFaceImage.setObjectName(u"ShowFaceImage")
        self.ShowFaceImage.setPixmap(QPixmap(u":/emoji/Pages/assets/emoji/2.png"))
        self.ShowFaceImage.setScaledContents(True)

        self.gridLayout_3.addWidget(self.ShowFaceImage, 1, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)

        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)

        self.ShowEmoji = QLabel(self.groupBox_2)
        self.ShowEmoji.setObjectName(u"ShowEmoji")
        self.ShowEmoji.setPixmap(QPixmap(u":/emoji/Pages/assets/emoji/3.png"))
        self.ShowEmoji.setScaledContents(True)

        self.gridLayout_3.addWidget(self.ShowEmoji, 3, 0, 1, 1)

        self.ResultEmotion = QLabel(self.groupBox_2)
        self.ResultEmotion.setObjectName(u"ResultEmotion")
        font7 = QFont()
        font7.setFamilies([u"Times New Roman"])
        font7.setPointSize(20)
        self.ResultEmotion.setFont(font7)
        self.ResultEmotion.setTextFormat(Qt.AutoText)
        self.ResultEmotion.setAlignment(Qt.AlignCenter)
        self.ResultEmotion.setIndent(0)

        self.gridLayout_3.addWidget(self.ResultEmotion, 4, 0, 1, 1)

        self.Start = QPushButton(self.groupBox_2)
        self.Start.setObjectName(u"Start")
        palette = QPalette()
        brush = QBrush(QColor(0, 255, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(240, 240, 240, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        self.Start.setPalette(palette)
        font8 = QFont()
        font8.setFamilies([u"\u9ed1\u4f53"])
        font8.setPointSize(16)
        self.Start.setFont(font8)
        self.Start.setIconSize(QSize(16, 16))
        self.Start.setCheckable(False)
        self.Start.setAutoExclusive(False)

        self.gridLayout_3.addWidget(self.Start, 5, 0, 1, 1)

        self.splitter_4.addWidget(self.groupBox_2)

        self.gridLayout_4.addWidget(self.splitter_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Image, "")
        self.Video = QWidget()
        self.Video.setObjectName(u"Video")
        self.gridLayout_5 = QGridLayout(self.Video)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.splitter_6 = QSplitter(self.Video)
        self.splitter_6.setObjectName(u"splitter_6")
        self.splitter_6.setOrientation(Qt.Horizontal)
        self.splitter_6.setOpaqueResize(True)
        self.splitter_6.setHandleWidth(0)
        self.groupBox_3 = QGroupBox(self.splitter_6)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font4)
        self.gridLayout_6 = QGridLayout(self.groupBox_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.splitter_3 = QSplitter(self.groupBox_3)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setFrameShadow(QFrame.Plain)
        self.splitter_3.setOrientation(Qt.Vertical)
        self.splitter_3.setHandleWidth(0)
        self.splitter_3.setChildrenCollapsible(True)
        self.OpenCamera = QPushButton(self.splitter_3)
        self.OpenCamera.setObjectName(u"OpenCamera")
        self.OpenCamera.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.OpenCamera.sizePolicy().hasHeightForWidth())
        self.OpenCamera.setSizePolicy(sizePolicy1)
        self.OpenCamera.setSizeIncrement(QSize(0, 0))
        font9 = QFont()
        font9.setFamilies([u"\u9ed1\u4f53"])
        font9.setPointSize(20)
        font9.setBold(False)
        font9.setItalic(False)
        self.OpenCamera.setFont(font9)
        self.OpenCamera.setAutoFillBackground(False)
        self.OpenCamera.setStyleSheet(u"padding:5;\n"
"margin:3")
        self.OpenCamera.setIconSize(QSize(16, 24))
        self.OpenCamera.setFlat(False)
        self.splitter_3.addWidget(self.OpenCamera)
        self.VideoCapture = QLabel(self.splitter_3)
        self.VideoCapture.setObjectName(u"VideoCapture")
        sizePolicy.setHeightForWidth(self.VideoCapture.sizePolicy().hasHeightForWidth())
        self.VideoCapture.setSizePolicy(sizePolicy)
        self.VideoCapture.setPixmap(QPixmap(u":/emoji/Pages/assets/emoji/1.png"))
        self.VideoCapture.setScaledContents(True)
        self.splitter_3.addWidget(self.VideoCapture)

        self.gridLayout_6.addWidget(self.splitter_3, 0, 0, 1, 1)

        self.splitter_6.addWidget(self.groupBox_3)
        self.groupBox_4 = QGroupBox(self.splitter_6)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFont(font4)
        self.gridLayout_7 = QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.ShowEmoji_2 = QLabel(self.groupBox_4)
        self.ShowEmoji_2.setObjectName(u"ShowEmoji_2")
        self.ShowEmoji_2.setPixmap(QPixmap(u":/emoji/Pages/assets/emoji/3.png"))
        self.ShowEmoji_2.setScaledContents(True)

        self.gridLayout_7.addWidget(self.ShowEmoji_2, 3, 0, 1, 1)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)

        self.gridLayout_7.addWidget(self.label_9, 0, 0, 1, 1)

        self.ResultEmotion_2 = QLabel(self.groupBox_4)
        self.ResultEmotion_2.setObjectName(u"ResultEmotion_2")
        self.ResultEmotion_2.setFont(font7)
        self.ResultEmotion_2.setTextFormat(Qt.AutoText)
        self.ResultEmotion_2.setAlignment(Qt.AlignCenter)
        self.ResultEmotion_2.setIndent(0)

        self.gridLayout_7.addWidget(self.ResultEmotion_2, 4, 0, 1, 1)

        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.gridLayout_7.addWidget(self.label_10, 2, 0, 1, 1)

        self.ShowFaceImage_2 = QLabel(self.groupBox_4)
        self.ShowFaceImage_2.setObjectName(u"ShowFaceImage_2")
        self.ShowFaceImage_2.setPixmap(QPixmap(u":/emoji/Pages/assets/emoji/2.png"))
        self.ShowFaceImage_2.setScaledContents(True)

        self.gridLayout_7.addWidget(self.ShowFaceImage_2, 1, 0, 1, 1)

        self.Start_2 = QPushButton(self.groupBox_4)
        self.Start_2.setObjectName(u"Start_2")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        self.Start_2.setPalette(palette1)
        self.Start_2.setFont(font8)
        self.Start_2.setIconSize(QSize(16, 16))
        self.Start_2.setCheckable(False)
        self.Start_2.setAutoExclusive(False)

        self.gridLayout_7.addWidget(self.Start_2, 5, 0, 1, 1)

        self.splitter_6.addWidget(self.groupBox_4)

        self.gridLayout_5.addWidget(self.splitter_6, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Video, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)


        self.retranslateUi(Inference)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Inference)
    # setupUi

    def retranslateUi(self, Inference):
        Inference.setWindowTitle(QCoreApplication.translate("Inference", u"\u6a21\u578b\u90e8\u7f72\u6f14\u793a", None))
        self.label.setText(QCoreApplication.translate("Inference", u"\u9009\u62e9\u6a21\u578b", None))
        self.SelectInferenceModel.setText(QCoreApplication.translate("Inference", u"\u786e\u5b9a", None))
        self.groupBox.setTitle(QCoreApplication.translate("Inference", u"\u5f85\u8bc6\u522b\u7684\u56fe\u7247", None))
        self.label_2.setText(QCoreApplication.translate("Inference", u"\u5f53\u524d\u56fe\u7247", None))
        self.CurrentImage.setText(QCoreApplication.translate("Inference", u"\u8bf7\u70b9\u51fb\u53f3\u4e0b\u89d2\u6309\u94ae\u8bfb\u53d6\u56fe\u7247", None))
        self.ShowSelectedImage.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("Inference", u"\u8bc6\u522b\u7ed3\u679c", None))
        self.label_7.setText(QCoreApplication.translate("Inference", u"\u622a\u53d6\u9762\u90e8\u533a\u57df", None))
        self.ShowFaceImage.setText("")
        self.label_8.setText(QCoreApplication.translate("Inference", u"\u8bc6\u522b\u7ed3\u679c", None))
        self.ShowEmoji.setText("")
        self.ResultEmotion.setText(QCoreApplication.translate("Inference", u"????", None))
        self.Start.setText(QCoreApplication.translate("Inference", u"\u8bfb\u53d6\u56fe\u7247", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Image), QCoreApplication.translate("Inference", u"\u56fe\u7247", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Inference", u"\u5b9e\u65f6\u6444\u50cf\u753b\u9762", None))
        self.OpenCamera.setText(QCoreApplication.translate("Inference", u"\u6253\u5f00\u6444\u50cf\u5934", None))
        self.VideoCapture.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("Inference", u"\u8bc6\u522b\u7ed3\u679c", None))
        self.ShowEmoji_2.setText("")
        self.label_9.setText(QCoreApplication.translate("Inference", u"\u622a\u53d6\u9762\u90e8\u533a\u57df", None))
        self.ResultEmotion_2.setText(QCoreApplication.translate("Inference", u"????", None))
        self.label_10.setText(QCoreApplication.translate("Inference", u"\u8bc6\u522b\u7ed3\u679c", None))
        self.ShowFaceImage_2.setText("")
        self.Start_2.setText(QCoreApplication.translate("Inference", u"\u5f00\u59cb\u8bc6\u522b", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Video), QCoreApplication.translate("Inference", u"\u89c6\u9891", None))
    # retranslateUi

