# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QWidget)
import assets_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1279, 717)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Microsoft YaHei"])
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.ActionNewTrain = QAction(MainWindow)
        self.ActionNewTrain.setObjectName(u"ActionNewTrain")
        self.ActionNewDataset = QAction(MainWindow)
        self.ActionNewDataset.setObjectName(u"ActionNewDataset")
        self.ActionSelectDataset = QAction(MainWindow)
        self.ActionSelectDataset.setObjectName(u"ActionSelectDataset")
        self.ActionStartTrain = QAction(MainWindow)
        self.ActionStartTrain.setObjectName(u"ActionStartTrain")
        self.ActionStartInference = QAction(MainWindow)
        self.ActionStartInference.setObjectName(u"ActionStartInference")
        self.actions_2 = QAction(MainWindow)
        self.actions_2.setObjectName(u"actions_2")
        self.ActionLoadDataset = QAction(MainWindow)
        self.ActionLoadDataset.setObjectName(u"ActionLoadDataset")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"background-image: url(:/cover/Pages/assets/cover.png)")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1279, 22))
        self.train = QMenu(self.menubar)
        self.train.setObjectName(u"train")
        self.inference = QMenu(self.menubar)
        self.inference.setObjectName(u"inference")
        self.seetings = QMenu(self.menubar)
        self.seetings.setObjectName(u"seetings")
        self.dataset = QMenu(self.menubar)
        self.dataset.setObjectName(u"dataset")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.dataset.menuAction())
        self.menubar.addAction(self.train.menuAction())
        self.menubar.addAction(self.inference.menuAction())
        self.menubar.addAction(self.seetings.menuAction())
        self.train.addAction(self.ActionNewTrain)
        self.train.addAction(self.ActionStartTrain)
        self.inference.addAction(self.ActionStartInference)
        self.dataset.addAction(self.ActionNewDataset)
        self.dataset.addAction(self.ActionLoadDataset)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u6f14\u793a", None))
        self.ActionNewTrain.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u8bad\u7ec3", None))
        self.ActionNewDataset.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa\u6570\u636e\u96c6", None))
        self.ActionSelectDataset.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6570\u636e\u96c6", None))
        self.ActionStartTrain.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8bad\u7ec3", None))
        self.ActionStartInference.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.actions_2.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u8bc6\u522b", None))
        self.ActionLoadDataset.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165\u6570\u636e\u96c6", None))
        self.train.setTitle(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u8bad\u7ec3\u6f14\u793a", None))
        self.inference.setTitle(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u90e8\u7f72\u6f14\u793a", None))
        self.seetings.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.dataset.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u96c6", None))
    # retranslateUi

