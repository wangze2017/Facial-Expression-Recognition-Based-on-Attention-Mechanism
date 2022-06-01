# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'NewDatasetWidget.ui'
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
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QSplitter, QToolButton, QWidget)

class Ui_NewDataset(object):
    def setupUi(self, NewDataset):
        if not NewDataset.objectName():
            NewDataset.setObjectName(u"NewDataset")
        NewDataset.resize(636, 292)
        self.gridLayout_2 = QGridLayout(NewDataset)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(NewDataset)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setFamilies([u"\u9ed1\u4f53"])
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.LabelDatasetDescription = QLabel(self.groupBox)
        self.LabelDatasetDescription.setObjectName(u"LabelDatasetDescription")
        font1 = QFont()
        font1.setFamilies([u"\u9ed1\u4f53"])
        font1.setPointSize(12)
        self.LabelDatasetDescription.setFont(font1)

        self.gridLayout.addWidget(self.LabelDatasetDescription, 1, 0, 1, 1)

        self.splitter_2 = QSplitter(self.groupBox)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.label_4 = QLabel(self.splitter_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.splitter_2.addWidget(self.label_4)
        self.datasetPath = QLineEdit(self.splitter_2)
        self.datasetPath.setObjectName(u"datasetPath")
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(12)
        self.datasetPath.setFont(font2)
        self.splitter_2.addWidget(self.datasetPath)
        self.savePath = QToolButton(self.splitter_2)
        self.savePath.setObjectName(u"savePath")
        self.savePath.setFont(font)
        self.splitter_2.addWidget(self.savePath)

        self.gridLayout.addWidget(self.splitter_2, 3, 0, 1, 1)

        self.DatasetDescription = QPlainTextEdit(self.groupBox)
        self.DatasetDescription.setObjectName(u"DatasetDescription")

        self.gridLayout.addWidget(self.DatasetDescription, 2, 0, 1, 1)

        self.splitter = QSplitter(self.groupBox)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.LabelDatasetID = QLabel(self.splitter)
        self.LabelDatasetID.setObjectName(u"LabelDatasetID")
        self.LabelDatasetID.setFont(font1)
        self.splitter.addWidget(self.LabelDatasetID)
        self.DatasetID = QLabel(self.splitter)
        self.DatasetID.setObjectName(u"DatasetID")
        self.DatasetID.setFont(font2)
        self.DatasetID.setTextFormat(Qt.AutoText)
        self.splitter.addWidget(self.DatasetID)
        self.LabelDatasetName = QLabel(self.splitter)
        self.LabelDatasetName.setObjectName(u"LabelDatasetName")
        self.LabelDatasetName.setFont(font1)
        self.splitter.addWidget(self.LabelDatasetName)
        self.DatasetName = QLineEdit(self.splitter)
        self.DatasetName.setObjectName(u"DatasetName")
        self.DatasetName.setFont(font2)
        self.splitter.addWidget(self.DatasetName)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        self.DatasetOK = QPushButton(self.groupBox)
        self.DatasetOK.setObjectName(u"DatasetOK")
        font3 = QFont()
        font3.setFamilies([u"\u9ed1\u4f53"])
        font3.setPointSize(20)
        self.DatasetOK.setFont(font3)
        self.DatasetOK.setStyleSheet(u"padding:10")

        self.gridLayout.addWidget(self.DatasetOK, 4, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(NewDataset)

        QMetaObject.connectSlotsByName(NewDataset)
    # setupUi

    def retranslateUi(self, NewDataset):
        NewDataset.setWindowTitle(QCoreApplication.translate("NewDataset", u"\u65b0\u5efa\u6570\u636e\u96c6", None))
        self.groupBox.setTitle(QCoreApplication.translate("NewDataset", u"\u521b\u5efa\u4fe1\u606f", None))
        self.LabelDatasetDescription.setText(QCoreApplication.translate("NewDataset", u"\u6570\u636e\u96c6\u63cf\u8ff0", None))
        self.label_4.setText(QCoreApplication.translate("NewDataset", u"\u6570\u636e\u96c6\u4fdd\u5b58\u8def\u5f84", None))
        self.savePath.setText(QCoreApplication.translate("NewDataset", u"...", None))
        self.LabelDatasetID.setText(QCoreApplication.translate("NewDataset", u"\u6570\u636e\u96c6ID", None))
        self.DatasetID.setText(QCoreApplication.translate("NewDataset", u"D1", None))
        self.LabelDatasetName.setText(QCoreApplication.translate("NewDataset", u"\u6570\u636e\u96c6\u540d\u79f0", None))
        self.DatasetOK.setText(QCoreApplication.translate("NewDataset", u"\u786e\u5b9a", None))
    # retranslateUi

