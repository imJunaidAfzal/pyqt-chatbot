# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_welcome_win(object):
    def setupUi(self, welcome_win):
        welcome_win.setObjectName("welcome_win")
        welcome_win.resize(486, 336)
        welcome_win.setMinimumSize(QtCore.QSize(486, 336))
        welcome_win.setMaximumSize(QtCore.QSize(486, 336))
        self.header_frame = QtWidgets.QFrame(welcome_win)
        self.header_frame.setGeometry(QtCore.QRect(10, 10, 461, 111))
        self.header_frame.setMinimumSize(QtCore.QSize(461, 111))
        self.header_frame.setStyleSheet("border-radius: 25px; \n"
"background-color: rgb(114, 159, 207);")
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.header_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.welcome_frame = QtWidgets.QFrame(self.header_frame)
        self.welcome_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.welcome_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.welcome_frame.setObjectName("welcome_frame")
        self.welcome_label = QtWidgets.QLabel(self.welcome_frame)
        self.welcome_label.setGeometry(QtCore.QRect(20, 10, 177, 37))
        self.welcome_label.setMinimumSize(QtCore.QSize(177, 30))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.welcome_label.setFont(font)
        self.welcome_label.setObjectName("welcome_label")
        self.label = QtWidgets.QLabel(self.welcome_frame)
        self.label.setGeometry(QtCore.QRect(40, 40, 119, 37))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.welcome_frame)
        self.frame_3 = QtWidgets.QFrame(self.header_frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(60, 0, 81, 81))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Birdie Adium.AdiumIcon/Alert1.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(welcome_win)
        self.frame_2.setGeometry(QtCore.QRect(20, 149, 441, 171))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(90, 10, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(100, 60, 221, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(160, 110, 101, 31))
        self.pushButton.setStyleSheet("selection-background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(welcome_win)
        QtCore.QMetaObject.connectSlotsByName(welcome_win)

    def retranslateUi(self, welcome_win):
        _translate = QtCore.QCoreApplication.translate
        welcome_win.setWindowTitle(_translate("welcome_win", "Welcome To Chatbot"))
        self.welcome_label.setText(_translate("welcome_win", "Welcome To"))
        self.label.setText(_translate("welcome_win", "Chatbot"))
        self.label_2.setText(_translate("welcome_win", "Enter Your Name"))
        self.pushButton.setText(_translate("welcome_win", "Go"))
