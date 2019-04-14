# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, -10, 121, 571))
        self.groupBox.setObjectName("groupBox")
        self.threshSlider = QtWidgets.QSlider(self.groupBox)
        self.threshSlider.setGeometry(QtCore.QRect(10, 190, 101, 22))
        self.threshSlider.setOrientation(QtCore.Qt.Horizontal)
        self.threshSlider.setObjectName("threshSlider")
        self.chooseImgBtn = QtWidgets.QPushButton(self.groupBox)
        self.chooseImgBtn.setGeometry(QtCore.QRect(10, 150, 101, 23))
        self.chooseImgBtn.setObjectName("chooseImgBtn")
        self.histBtn = QtWidgets.QPushButton(self.groupBox)
        self.histBtn.setGeometry(QtCore.QRect(10, 230, 101, 23))
        self.histBtn.setObjectName("histBtn")
        self.otsuBtn = QtWidgets.QPushButton(self.groupBox)
        self.otsuBtn.setGeometry(QtCore.QRect(10, 270, 101, 23))
        self.otsuBtn.setObjectName("otsuBtn")
        self.entBtn = QtWidgets.QPushButton(self.groupBox)
        self.entBtn.setGeometry(QtCore.QRect(10, 310, 101, 23))
        self.entBtn.setObjectName("entBtn")
        self.sourceView = QtWidgets.QGraphicsView(self.centralwidget)
        self.sourceView.setGeometry(QtCore.QRect(130, 40, 321, 231))
        self.sourceView.setObjectName("sourceView")
        self.histView = QtWidgets.QGraphicsView(self.centralwidget)
        self.histView.setGeometry(QtCore.QRect(460, 40, 321, 231))
        self.histView.setObjectName("histView")
        self.otsuView = QtWidgets.QGraphicsView(self.centralwidget)
        self.otsuView.setGeometry(QtCore.QRect(130, 321, 321, 231))
        self.otsuView.setObjectName("otsuView")
        self.entropyView = QtWidgets.QGraphicsView(self.centralwidget)
        self.entropyView.setGeometry(QtCore.QRect(460, 321, 321, 231))
        self.entropyView.setObjectName("entropyView")
        self.sourceLb = QtWidgets.QLabel(self.centralwidget)
        self.sourceLb.setGeometry(QtCore.QRect(130, 10, 71, 16))
        self.sourceLb.setObjectName("sourceLb")
        self.hisLb = QtWidgets.QLabel(self.centralwidget)
        self.hisLb.setGeometry(QtCore.QRect(460, 10, 54, 12))
        self.hisLb.setObjectName("hisLb")
        self.otsuLb = QtWidgets.QLabel(self.centralwidget)
        self.otsuLb.setGeometry(QtCore.QRect(130, 290, 54, 12))
        self.otsuLb.setObjectName("otsuLb")
        self.entLb = QtWidgets.QLabel(self.centralwidget)
        self.entLb.setGeometry(QtCore.QRect(460, 290, 54, 12))
        self.entLb.setObjectName("entLb")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.chooseImgBtn.setText(_translate("MainWindow", "加载源图"))
        self.histBtn.setText(_translate("MainWindow", "显示直方图"))
        self.otsuBtn.setText(_translate("MainWindow", "OTSU二值化"))
        self.entBtn.setText(_translate("MainWindow", "ENTRPY二值化"))
        self.sourceLb.setText(_translate("MainWindow", "SourceImg"))
        self.hisLb.setText(_translate("MainWindow", "Histogram"))
        self.otsuLb.setText(_translate("MainWindow", "OTSU"))
        self.entLb.setText(_translate("MainWindow", "ENTEOPY"))

