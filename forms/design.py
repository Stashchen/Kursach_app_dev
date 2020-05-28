# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled_v2.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1178, 790)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openGLWidget = CustomGL(self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(20, 10, 761, 721))
        self.openGLWidget.setObjectName("openGLWidget")
        self.cylinder_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cylinder_btn.setGeometry(QtCore.QRect(910, 180, 81, 41))
        self.cylinder_btn.setCheckable(False)
        self.cylinder_btn.setObjectName("cylinder_btn")
        self.dome_btn = QtWidgets.QPushButton(self.centralwidget)
        self.dome_btn.setEnabled(True)
        self.dome_btn.setGeometry(QtCore.QRect(1090, 180, 81, 41))
        self.dome_btn.setCheckable(False)
        self.dome_btn.setChecked(False)
        self.dome_btn.setObjectName("dome_btn")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(790, 190, 201, 17))
        self.label_4.setObjectName("label_4")
        self.error_msg = QtWidgets.QLabel(self.centralwidget)
        self.error_msg.setGeometry(QtCore.QRect(790, 230, 381, 81))
        self.error_msg.setFrameShape(QtWidgets.QFrame.Box)
        self.error_msg.setText("")
        self.error_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.error_msg.setObjectName("error_msg")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(790, 40, 381, 131))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(790, 10, 181, 21))
        self.label.setObjectName("label")
        self.sphere_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sphere_btn.setGeometry(QtCore.QRect(1000, 180, 81, 41))
        self.sphere_btn.setCheckable(False)
        self.sphere_btn.setObjectName("sphere_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1178, 22))
        self.menubar.setObjectName("menubar")
        self.menuword = QtWidgets.QMenu(self.menubar)
        self.menuword.setObjectName("menuword")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionWord = QtWidgets.QAction(MainWindow)
        self.actionWord.setObjectName("actionWord")
        self.actionExcel = QtWidgets.QAction(MainWindow)
        self.actionExcel.setObjectName("actionExcel")
        self.actionHel = QtWidgets.QAction(MainWindow)
        self.actionHel.setObjectName("actionHel")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuword.addAction(self.actionWord)
        self.menuword.addAction(self.actionExcel)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionExit)
        self.menubar.addAction(self.menuword.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Курсовая работа"))
        self.cylinder_btn.setText(_translate("MainWindow", "Cylinder"))
        self.dome_btn.setText(_translate("MainWindow", "Dome"))
        self.label_4.setText(_translate("MainWindow", "Add new figure:"))
        self.label.setText(_translate("MainWindow", "All the figures:"))
        self.sphere_btn.setText(_translate("MainWindow", "Sphere"))
        self.menuword.setTitle(_translate("MainWindow", "Save"))
        self.menuHelp.setTitle(_translate("MainWindow", "Options"))
        self.actionWord.setText(_translate("MainWindow", "Word"))
        self.actionExcel.setText(_translate("MainWindow", "Excel"))
        self.actionHel.setText(_translate("MainWindow", "Hel["))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
from custom_gl import CustomGL
