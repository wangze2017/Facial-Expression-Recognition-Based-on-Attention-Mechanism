# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StartTrainWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QWidget)

class Ui_Train(object):
    def setupUi(self, Train):
        if not Train.objectName():
            Train.setObjectName(u"Train")
        Train.resize(625, 171)
        self.gridLayout = QGridLayout(Train)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Label = QLabel(Train)
        self.Label.setObjectName(u"Label")
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        font.setPointSize(16)
        self.Label.setFont(font)

        self.horizontalLayout.addWidget(self.Label)

        self.SelectTrainID = QComboBox(Train)
        self.SelectTrainID.setObjectName(u"SelectTrainID")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(16)
        self.SelectTrainID.setFont(font1)

        self.horizontalLayout.addWidget(self.SelectTrainID)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.VisualTrain = QPushButton(Train)
        self.VisualTrain.setObjectName(u"VisualTrain")
        font2 = QFont()
        font2.setFamilies([u"\u9ed1\u4f53"])
        font2.setPointSize(24)
        self.VisualTrain.setFont(font2)

        self.gridLayout.addWidget(self.VisualTrain, 1, 0, 1, 1)


        self.retranslateUi(Train)

        QMetaObject.connectSlotsByName(Train)
    # setupUi

    def retranslateUi(self, Train):
        Train.setWindowTitle(QCoreApplication.translate("Train", u"\u8bad\u7ec3\u53ef\u89c6\u5316", None))
        self.Label.setText(QCoreApplication.translate("Train", u"\u9009\u62e9\u8bad\u7ec3ID", None))
        self.VisualTrain.setText(QCoreApplication.translate("Train", u"\u53ef\u89c6\u5316\u8bad\u7ec3\u8fc7\u7a0b", None))
    # retranslateUi

