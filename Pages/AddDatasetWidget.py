# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddDatasetWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QToolButton,
    QVBoxLayout, QWidget)

class Ui_AddDatasetWidget(object):
    def setupUi(self, AddDatasetWidget):
        if not AddDatasetWidget.objectName():
            AddDatasetWidget.setObjectName(u"AddDatasetWidget")
        AddDatasetWidget.resize(640, 480)
        AddDatasetWidget.setMaximumSize(QSize(640, 480))
        self.DatasetOK = QPushButton(AddDatasetWidget)
        self.DatasetOK.setObjectName(u"DatasetOK")
        self.DatasetOK.setGeometry(QRect(210, 420, 211, 51))
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        font.setPointSize(20)
        self.DatasetOK.setFont(font)
        self.layoutWidget = QWidget(AddDatasetWidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 601, 401))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        font1 = QFont()
        font1.setFamilies([u"\u9ed1\u4f53"])
        font1.setPointSize(14)
        self.groupBox.setFont(font1)
        self.LabelDatasetID = QLabel(self.groupBox)
        self.LabelDatasetID.setObjectName(u"LabelDatasetID")
        self.LabelDatasetID.setGeometry(QRect(20, 40, 71, 20))
        font2 = QFont()
        font2.setFamilies([u"\u9ed1\u4f53"])
        font2.setPointSize(12)
        self.LabelDatasetID.setFont(font2)
        self.DatasetID = QLabel(self.groupBox)
        self.DatasetID.setObjectName(u"DatasetID")
        self.DatasetID.setGeometry(QRect(130, 40, 71, 20))
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(12)
        self.DatasetID.setFont(font3)
        self.DatasetID.setTextFormat(Qt.AutoText)
        self.LabelDatasetDescription = QLabel(self.groupBox)
        self.LabelDatasetDescription.setObjectName(u"LabelDatasetDescription")
        self.LabelDatasetDescription.setGeometry(QRect(20, 80, 90, 20))
        self.LabelDatasetDescription.setFont(font2)
        self.DatasetDescription = QPlainTextEdit(self.groupBox)
        self.DatasetDescription.setObjectName(u"DatasetDescription")
        self.DatasetDescription.setGeometry(QRect(20, 110, 561, 61))
        self.LabelDatasetName = QLabel(self.groupBox)
        self.LabelDatasetName.setObjectName(u"LabelDatasetName")
        self.LabelDatasetName.setGeometry(QRect(230, 40, 91, 20))
        self.LabelDatasetName.setFont(font2)
        self.DatasetName = QLineEdit(self.groupBox)
        self.DatasetName.setObjectName(u"DatasetName")
        self.DatasetName.setGeometry(QRect(340, 40, 113, 22))
        self.DatasetName.setFont(font3)

        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.layoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font1)
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 150, 90, 20))
        self.label_4.setFont(font2)
        self.findPath = QToolButton(self.groupBox_2)
        self.findPath.setObjectName(u"findPath")
        self.findPath.setGeometry(QRect(440, 150, 60, 22))
        self.findPath.setFont(font1)
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 40, 561, 81))
        font4 = QFont()
        font4.setFamilies([u"\u6977\u4f53"])
        font4.setPointSize(12)
        self.label_6.setFont(font4)
        self.label_6.setTextFormat(Qt.PlainText)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_6.setWordWrap(True)
        self.datasetPath = QLineEdit(self.groupBox_2)
        self.datasetPath.setObjectName(u"datasetPath")
        self.datasetPath.setGeometry(QRect(200, 150, 221, 22))
        self.datasetPath.setFont(font3)

        self.verticalLayout.addWidget(self.groupBox_2)


        self.retranslateUi(AddDatasetWidget)

        QMetaObject.connectSlotsByName(AddDatasetWidget)
    # setupUi

    def retranslateUi(self, AddDatasetWidget):
        AddDatasetWidget.setWindowTitle(QCoreApplication.translate("AddDatasetWidget", u"\u65b0\u5efa\u6570\u636e\u96c6", None))
        self.DatasetOK.setText(QCoreApplication.translate("AddDatasetWidget", u"\u786e\u5b9a", None))
        self.groupBox.setTitle(QCoreApplication.translate("AddDatasetWidget", u"\u521b\u5efa\u4fe1\u606f", None))
        self.LabelDatasetID.setText(QCoreApplication.translate("AddDatasetWidget", u"\u6570\u636e\u96c6ID", None))
        self.DatasetID.setText(QCoreApplication.translate("AddDatasetWidget", u"D1", None))
        self.LabelDatasetDescription.setText(QCoreApplication.translate("AddDatasetWidget", u"\u6570\u636e\u96c6\u63cf\u8ff0", None))
        self.LabelDatasetName.setText(QCoreApplication.translate("AddDatasetWidget", u"\u6570\u636e\u96c6\u540d\u79f0", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("AddDatasetWidget", u"\u6570\u636e\u96c6\u5bfc\u5165", None))
        self.label_4.setText(QCoreApplication.translate("AddDatasetWidget", u"\u6570\u636e\u96c6\u8def\u5f84", None))
        self.findPath.setText(QCoreApplication.translate("AddDatasetWidget", u"...", None))
        self.label_6.setText(QCoreApplication.translate("AddDatasetWidget", u"\u9700\u8981\u9009\u5b9a\u6570\u636e\u96c6\u6240\u5728\u6587\u4ef6\u5939\u8def\u5f84\uff08\u8def\u5f84\u4e2d\u4ec5\u542b\u4e00\u4e2a\u6570\u636e\u96c6)\uff0c\u4e0d\u652f\u6301.zip\u3001tar.gz\u7b49\u538b\u7f29\u5305\u5f62\u5f0f\u7684\u6570\u636e\u5bfc\u5165\uff0c\u56fe\u7247\u683c\u5f0f\u652f\u6301png. jpg. jpeg. bmp\u683c\u5f0f\uff0c\u6587\u4ef6\u5939\u540d\u4e3a\u9700\u8981\u5206\u7c7b\u7684\u7c7b\u540d\uff0c\u8f93\u5165\u9650\u5b9a\u4e3a\u82f1\u6587\u5b57\u7b26\uff0c\u4e0d\u53ef\u5305\u542b\u7a7a\u683c\u3001\u4e2d\u6587\u6216\u7279\u6b8a\u5b57\u7b26\u3002", None))
    # retranslateUi

