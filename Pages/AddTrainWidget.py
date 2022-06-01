# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddTrainWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSpinBox, QToolButton, QVBoxLayout, QWidget)

class Ui_newTrain(object):
    def setupUi(self, newTrain):
        if not newTrain.objectName():
            newTrain.setObjectName(u"newTrain")
        newTrain.resize(566, 650)
        self.horizontalLayout = QHBoxLayout(newTrain)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.scrollArea = QScrollArea(newTrain)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 546, 630))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.TrainOK = QPushButton(self.scrollAreaWidgetContents)
        self.TrainOK.setObjectName(u"TrainOK")
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        font.setPointSize(20)
        self.TrainOK.setFont(font)

        self.gridLayout_2.addWidget(self.TrainOK, 1, 0, 1, 1)

        self.groupBox = QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName(u"groupBox")
        font1 = QFont()
        font1.setFamilies([u"\u9ed1\u4f53"])
        font1.setPointSize(14)
        self.groupBox.setFont(font1)
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(40)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.LabelTrainID = QLabel(self.groupBox)
        self.LabelTrainID.setObjectName(u"LabelTrainID")
        font2 = QFont()
        font2.setFamilies([u"\u9ed1\u4f53"])
        font2.setPointSize(12)
        self.LabelTrainID.setFont(font2)

        self.horizontalLayout_16.addWidget(self.LabelTrainID)

        self.TrainID = QLabel(self.groupBox)
        self.TrainID.setObjectName(u"TrainID")
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(12)
        self.TrainID.setFont(font3)
        self.TrainID.setTextFormat(Qt.AutoText)

        self.horizontalLayout_16.addWidget(self.TrainID)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.LabelTrainName = QLabel(self.groupBox)
        self.LabelTrainName.setObjectName(u"LabelTrainName")
        self.LabelTrainName.setFont(font2)

        self.horizontalLayout_17.addWidget(self.LabelTrainName)

        self.TrainName = QLineEdit(self.groupBox)
        self.TrainName.setObjectName(u"TrainName")
        self.TrainName.setFont(font3)

        self.horizontalLayout_17.addWidget(self.TrainName)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_17)


        self.verticalLayout_2.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(40)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.horizontalLayout_19.addWidget(self.label_4)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.TrainPath = QLineEdit(self.groupBox)
        self.TrainPath.setObjectName(u"TrainPath")
        self.TrainPath.setFont(font3)

        self.horizontalLayout_15.addWidget(self.TrainPath)

        self.SelectPath = QToolButton(self.groupBox)
        self.SelectPath.setObjectName(u"SelectPath")
        self.SelectPath.setFont(font1)

        self.horizontalLayout_15.addWidget(self.SelectPath)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_15)


        self.verticalLayout_2.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.Label_2 = QLabel(self.groupBox)
        self.Label_2.setObjectName(u"Label_2")
        self.Label_2.setFont(font2)

        self.horizontalLayout_13.addWidget(self.Label_2)

        self.SelectDataset = QComboBox(self.groupBox)
        self.SelectDataset.setObjectName(u"SelectDataset")
        self.SelectDataset.setFont(font2)

        self.horizontalLayout_13.addWidget(self.SelectDataset)


        self.verticalLayout_2.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.Label5 = QLabel(self.groupBox)
        self.Label5.setObjectName(u"Label5")
        self.Label5.setFont(font2)

        self.horizontalLayout_14.addWidget(self.Label5)

        self.SelectModel = QComboBox(self.groupBox)
        self.SelectModel.addItem("")
        self.SelectModel.addItem("")
        self.SelectModel.addItem("")
        self.SelectModel.setObjectName(u"SelectModel")
        self.SelectModel.setFont(font2)

        self.horizontalLayout_14.addWidget(self.SelectModel)


        self.verticalLayout_2.addLayout(self.horizontalLayout_14)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font2)
        self.gridLayout_10 = QGridLayout(self.groupBox_2)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamilies([u"\u6977\u4f53"])
        font4.setPointSize(12)
        self.label.setFont(font4)

        self.gridLayout_10.addWidget(self.label, 0, 0, 1, 1)

        self.LabelLearningRate = QLabel(self.groupBox_2)
        self.LabelLearningRate.setObjectName(u"LabelLearningRate")
        self.LabelLearningRate.setFont(font4)

        self.gridLayout_10.addWidget(self.LabelLearningRate, 3, 0, 1, 1)

        self.LabelBatchSize = QLabel(self.groupBox_2)
        self.LabelBatchSize.setObjectName(u"LabelBatchSize")
        self.LabelBatchSize.setFont(font4)

        self.gridLayout_10.addWidget(self.LabelBatchSize, 4, 0, 1, 1)

        self.BatchSize = QSpinBox(self.groupBox_2)
        self.BatchSize.setObjectName(u"BatchSize")
        self.BatchSize.setFont(font3)
        self.BatchSize.setMaximum(500)
        self.BatchSize.setValue(48)

        self.gridLayout_10.addWidget(self.BatchSize, 4, 1, 1, 1)

        self.LearningRate = QDoubleSpinBox(self.groupBox_2)
        self.LearningRate.setObjectName(u"LearningRate")
        self.LearningRate.setFont(font3)
        self.LearningRate.setDecimals(8)
        self.LearningRate.setMaximum(1.000000000000000)
        self.LearningRate.setSingleStep(0.000001000000000)
        self.LearningRate.setValue(0.001000000000000)

        self.gridLayout_10.addWidget(self.LearningRate, 3, 1, 1, 1)

        self.TrainSet = QSpinBox(self.groupBox_2)
        self.TrainSet.setObjectName(u"TrainSet")
        self.TrainSet.setFont(font3)
        self.TrainSet.setMaximum(100)
        self.TrainSet.setValue(80)
        self.TrainSet.setDisplayIntegerBase(10)

        self.gridLayout_10.addWidget(self.TrainSet, 0, 1, 1, 1)

        self.Epoch = QSpinBox(self.groupBox_2)
        self.Epoch.setObjectName(u"Epoch")
        self.Epoch.setFont(font3)
        self.Epoch.setMaximum(500)
        self.Epoch.setValue(100)

        self.gridLayout_10.addWidget(self.Epoch, 2, 1, 1, 1)

        self.LabelEpoch = QLabel(self.groupBox_2)
        self.LabelEpoch.setObjectName(u"LabelEpoch")
        self.LabelEpoch.setFont(font4)

        self.gridLayout_10.addWidget(self.LabelEpoch, 2, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font4)

        self.gridLayout_10.addWidget(self.label_2, 1, 0, 1, 1)

        self.ValidSet = QSpinBox(self.groupBox_2)
        self.ValidSet.setObjectName(u"ValidSet")
        self.ValidSet.setFont(font3)
        self.ValidSet.setValue(20)

        self.gridLayout_10.addWidget(self.ValidSet, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font2)
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Bright = QGroupBox(self.groupBox_3)
        self.Bright.setObjectName(u"Bright")
        self.Bright.setFont(font4)
        self.gridLayout = QGridLayout(self.Bright)
        self.gridLayout.setObjectName(u"gridLayout")
        self.BrightOn = QRadioButton(self.Bright)
        self.BrightOn.setObjectName(u"BrightOn")
        self.BrightOn.setFont(font4)
        self.BrightOn.setChecked(True)

        self.gridLayout.addWidget(self.BrightOn, 0, 0, 1, 1)

        self.BrightOff = QRadioButton(self.Bright)
        self.BrightOff.setObjectName(u"BrightOff")
        self.BrightOff.setFont(font4)

        self.gridLayout.addWidget(self.BrightOff, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.Bright, 0, 0, 1, 1)

        self.shelter = QGroupBox(self.groupBox_3)
        self.shelter.setObjectName(u"shelter")
        self.shelter.setFont(font4)
        self.gridLayout_9 = QGridLayout(self.shelter)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.shelterOn = QRadioButton(self.shelter)
        self.shelterOn.setObjectName(u"shelterOn")
        self.shelterOn.setFont(font4)
        self.shelterOn.setChecked(True)

        self.gridLayout_9.addWidget(self.shelterOn, 0, 0, 1, 1)

        self.shelterOff = QRadioButton(self.shelter)
        self.shelterOff.setObjectName(u"shelterOff")
        self.shelterOff.setFont(font4)

        self.gridLayout_9.addWidget(self.shelterOff, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.shelter, 1, 2, 1, 1)

        self.contrast = QGroupBox(self.groupBox_3)
        self.contrast.setObjectName(u"contrast")
        self.contrast.setFont(font4)
        self.gridLayout_6 = QGridLayout(self.contrast)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.contrastOn = QRadioButton(self.contrast)
        self.contrastOn.setObjectName(u"contrastOn")
        self.contrastOn.setFont(font4)
        self.contrastOn.setChecked(True)

        self.gridLayout_6.addWidget(self.contrastOn, 0, 0, 1, 1)

        self.contrastOff = QRadioButton(self.contrast)
        self.contrastOff.setObjectName(u"contrastOff")
        self.contrastOff.setFont(font4)

        self.gridLayout_6.addWidget(self.contrastOff, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.contrast, 0, 2, 1, 1)

        self.saturation = QGroupBox(self.groupBox_3)
        self.saturation.setObjectName(u"saturation")
        self.saturation.setFont(font4)
        self.gridLayout_7 = QGridLayout(self.saturation)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.saturationOn = QRadioButton(self.saturation)
        self.saturationOn.setObjectName(u"saturationOn")
        self.saturationOn.setFont(font4)
        self.saturationOn.setChecked(True)

        self.gridLayout_7.addWidget(self.saturationOn, 0, 0, 1, 1)

        self.saturationOff = QRadioButton(self.saturation)
        self.saturationOff.setObjectName(u"saturationOff")
        self.saturationOff.setFont(font4)

        self.gridLayout_7.addWidget(self.saturationOff, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.saturation, 1, 0, 1, 1)

        self.flip = QGroupBox(self.groupBox_3)
        self.flip.setObjectName(u"flip")
        self.flip.setFont(font4)
        self.gridLayout_8 = QGridLayout(self.flip)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.flipOn = QRadioButton(self.flip)
        self.flipOn.setObjectName(u"flipOn")
        self.flipOn.setFont(font4)
        self.flipOn.setChecked(True)

        self.gridLayout_8.addWidget(self.flipOn, 0, 0, 1, 1)

        self.flipOff = QRadioButton(self.flip)
        self.flipOff.setObjectName(u"flipOff")
        self.flipOff.setFont(font4)

        self.gridLayout_8.addWidget(self.flipOff, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.flip, 1, 1, 1, 1)

        self.rotate = QGroupBox(self.groupBox_3)
        self.rotate.setObjectName(u"rotate")
        self.rotate.setFont(font4)
        self.gridLayout_5 = QGridLayout(self.rotate)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.rotateOn = QRadioButton(self.rotate)
        self.rotateOn.setObjectName(u"rotateOn")
        self.rotateOn.setFont(font4)
        self.rotateOn.setChecked(True)

        self.gridLayout_5.addWidget(self.rotateOn, 0, 0, 1, 1)

        self.rotateOff = QRadioButton(self.rotate)
        self.rotateOff.setObjectName(u"rotateOff")
        self.rotateOff.setFont(font4)

        self.gridLayout_5.addWidget(self.rotateOff, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.rotate, 0, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.groupBox_3)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.scrollArea)


        self.retranslateUi(newTrain)

        QMetaObject.connectSlotsByName(newTrain)
    # setupUi

    def retranslateUi(self, newTrain):
        newTrain.setWindowTitle(QCoreApplication.translate("newTrain", u"\u65b0\u5efa\u8bad\u7ec3", None))
        self.TrainOK.setText(QCoreApplication.translate("newTrain", u"\u786e\u5b9a", None))
        self.groupBox.setTitle(QCoreApplication.translate("newTrain", u"\u8bad\u7ec3\u4fe1\u606f", None))
        self.LabelTrainID.setText(QCoreApplication.translate("newTrain", u"\u8bad\u7ec3ID", None))
        self.TrainID.setText(QCoreApplication.translate("newTrain", u"T1", None))
        self.LabelTrainName.setText(QCoreApplication.translate("newTrain", u"\u8bad\u7ec3\u540d\u79f0", None))
        self.label_4.setText(QCoreApplication.translate("newTrain", u"\u8bad\u7ec3\u4fdd\u5b58\u8def\u5f84", None))
        self.SelectPath.setText(QCoreApplication.translate("newTrain", u"...", None))
        self.Label_2.setText(QCoreApplication.translate("newTrain", u"\u9009\u62e9\u6570\u636e\u96c6", None))
        self.Label5.setText(QCoreApplication.translate("newTrain", u"\u9009\u62e9\u6a21\u578b", None))
        self.SelectModel.setItemText(0, QCoreApplication.translate("newTrain", u"ResNet34", None))
        self.SelectModel.setItemText(1, QCoreApplication.translate("newTrain", u"\u65b9\u6cd5\u4e00", None))
        self.SelectModel.setItemText(2, QCoreApplication.translate("newTrain", u"\u65b9\u6cd5\u4e8c", None))

        self.groupBox_2.setTitle(QCoreApplication.translate("newTrain", u"\u8bad\u7ec3\u53c2\u6570", None))
        self.label.setText(QCoreApplication.translate("newTrain", u"\u8bad\u7ec3\u96c6\u5927\u5c0f", None))
        self.LabelLearningRate.setText(QCoreApplication.translate("newTrain", u"\u5b66\u4e60\u7387", None))
        self.LabelBatchSize.setText(QCoreApplication.translate("newTrain", u"\u6279\u5927\u5c0f", None))
        self.LabelEpoch.setText(QCoreApplication.translate("newTrain", u"\u8fed\u4ee3\u8f6e\u6570", None))
        self.label_2.setText(QCoreApplication.translate("newTrain", u"\u9a8c\u8bc1\u96c6\u5927\u5c0f", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("newTrain", u"\u6570\u636e\u589e\u5f3a", None))
        self.Bright.setTitle(QCoreApplication.translate("newTrain", u"\u968f\u673a\u4eae\u5ea6", None))
        self.BrightOn.setText(QCoreApplication.translate("newTrain", u"\u5f00", None))
        self.BrightOff.setText(QCoreApplication.translate("newTrain", u"\u5173", None))
        self.shelter.setTitle(QCoreApplication.translate("newTrain", u"\u968f\u673a\u906e\u6321", None))
        self.shelterOn.setText(QCoreApplication.translate("newTrain", u"\u5f00", None))
        self.shelterOff.setText(QCoreApplication.translate("newTrain", u"\u5173", None))
        self.contrast.setTitle(QCoreApplication.translate("newTrain", u"\u968f\u673a\u5bf9\u6bd4\u5ea6", None))
        self.contrastOn.setText(QCoreApplication.translate("newTrain", u"\u5f00", None))
        self.contrastOff.setText(QCoreApplication.translate("newTrain", u"\u5173", None))
        self.saturation.setTitle(QCoreApplication.translate("newTrain", u"\u968f\u673a\u9971\u548c\u5ea6", None))
        self.saturationOn.setText(QCoreApplication.translate("newTrain", u"\u5f00", None))
        self.saturationOff.setText(QCoreApplication.translate("newTrain", u"\u5173", None))
        self.flip.setTitle(QCoreApplication.translate("newTrain", u"\u968f\u673a\u7ffb\u8f6c", None))
        self.flipOn.setText(QCoreApplication.translate("newTrain", u"\u5f00", None))
        self.flipOff.setText(QCoreApplication.translate("newTrain", u"\u5173", None))
        self.rotate.setTitle(QCoreApplication.translate("newTrain", u"\u968f\u673a\u65cb\u8f6c", None))
        self.rotateOn.setText(QCoreApplication.translate("newTrain", u"\u5f00", None))
        self.rotateOff.setText(QCoreApplication.translate("newTrain", u"\u5173", None))
    # retranslateUi

