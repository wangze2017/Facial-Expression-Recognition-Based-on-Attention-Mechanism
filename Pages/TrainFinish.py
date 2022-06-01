# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TrainFinish.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QSizePolicy, QWidget)

class Ui_TrainFinish(object):
    def setupUi(self, TrainFinish):
        if not TrainFinish.objectName():
            TrainFinish.setObjectName(u"TrainFinish")
        TrainFinish.resize(589, 250)
        self.gridLayout = QGridLayout(TrainFinish)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(TrainFinish)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        font.setPointSize(14)
        self.label.setFont(font)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.TrainTime = QLabel(self.groupBox)
        self.TrainTime.setObjectName(u"TrainTime")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(14)
        self.TrainTime.setFont(font1)

        self.gridLayout_2.addWidget(self.TrainTime, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.TrainEpoch = QLabel(self.groupBox)
        self.TrainEpoch.setObjectName(u"TrainEpoch")
        self.TrainEpoch.setFont(font1)

        self.gridLayout_2.addWidget(self.TrainEpoch, 1, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)

        self.ValidAcc = QLabel(self.groupBox)
        self.ValidAcc.setObjectName(u"ValidAcc")
        self.ValidAcc.setFont(font1)

        self.gridLayout_2.addWidget(self.ValidAcc, 2, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)

        self.ModelSavePath = QLabel(self.groupBox)
        self.ModelSavePath.setObjectName(u"ModelSavePath")
        self.ModelSavePath.setFont(font1)

        self.gridLayout_2.addWidget(self.ModelSavePath, 3, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(TrainFinish)

        QMetaObject.connectSlotsByName(TrainFinish)
    # setupUi

    def retranslateUi(self, TrainFinish):
        TrainFinish.setWindowTitle(QCoreApplication.translate("TrainFinish", u"\u8bad\u7ec3\u5b8c\u6210", None))
        self.groupBox.setTitle(QCoreApplication.translate("TrainFinish", u"GroupBox", None))
        self.label.setText(QCoreApplication.translate("TrainFinish", u"\u8bad\u7ec3\u65f6\u957f", None))
        self.TrainTime.setText("")
        self.label_3.setText(QCoreApplication.translate("TrainFinish", u"\u8fed\u4ee3\u8f6e\u6570", None))
        self.TrainEpoch.setText("")
        self.label_5.setText(QCoreApplication.translate("TrainFinish", u"\u9a8c\u8bc1\u96c6\u51c6\u786e\u7387", None))
        self.ValidAcc.setText("")
        self.label_7.setText(QCoreApplication.translate("TrainFinish", u"\u6a21\u578b\u4fdd\u5b58\u8def\u5f84", None))
        self.ModelSavePath.setText("")
    # retranslateUi

