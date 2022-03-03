# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat_bot.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Chatbot_mainwindow(object):
    def setupUi(self, Chatbot_mainwindow):
        Chatbot_mainwindow.setObjectName("Chatbot_mainwindow")
        Chatbot_mainwindow.resize(519, 824)
        Chatbot_mainwindow.setStyleSheet("gridline-color: rgba(191, 64, 64, 0);")
        self.centralwidget = QtWidgets.QWidget(Chatbot_mainwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(501, 300))
        font = QtGui.QFont()
        font.setPointSize(2)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: rgb(85, 87, 83);\n"
"border-radius: 15px; \n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.header_frame = QtWidgets.QFrame(self.frame)
        self.header_frame.setGeometry(QtCore.QRect(0, 0, 247, 300))
        self.header_frame.setMinimumSize(QtCore.QSize(229, 300))
        self.header_frame.setMaximumSize(QtCore.QSize(16777215, 5000))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.header_frame.setFont(font)
        self.header_frame.setStyleSheet("*{\n"
"border:none;\n"
"}")
        self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_frame.setObjectName("header_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.header_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.left_header = QtWidgets.QFrame(self.header_frame)
        self.left_header.setMinimumSize(QtCore.QSize(211, 138))
        self.left_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_header.setObjectName("left_header")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.left_header)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.hi_label = QtWidgets.QLabel(self.left_header)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.hi_label.setFont(font)
        self.hi_label.setObjectName("hi_label")
        self.verticalLayout_3.addWidget(self.hi_label, 0, QtCore.Qt.AlignHCenter)
        self.name_label = QtWidgets.QLabel(self.left_header)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.name_label.setFont(font)
        self.name_label.setObjectName("name_label")
        self.verticalLayout_3.addWidget(self.name_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.verticalLayout_2.addWidget(self.left_header)
        self.right_header = QtWidgets.QFrame(self.frame)
        self.right_header.setGeometry(QtCore.QRect(280, 10, 211, 282))
        self.right_header.setMinimumSize(QtCore.QSize(140, 140))
        self.right_header.setStyleSheet("*{\n"
"border:none;\n"
"}")
        self.right_header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_header.setObjectName("right_header")
        self.bot_icon = QtWidgets.QLabel(self.right_header)
        self.bot_icon.setGeometry(QtCore.QRect(20, 20, 121, 111))
        self.bot_icon.setMinimumSize(QtCore.QSize(121, 111))
        self.bot_icon.setStyleSheet("*{\n"
"border:none;\n"
"\n"
"}")
        self.bot_icon.setText("")
        self.bot_icon.setPixmap(QtGui.QPixmap("Birdie Adium.AdiumIcon/Sleep.png"))
        self.bot_icon.setObjectName("bot_icon")
        self.bot_name = QtWidgets.QLabel(self.right_header)
        self.bot_name.setGeometry(QtCore.QRect(10, 130, 200, 71))
        self.bot_name.setMinimumSize(QtCore.QSize(200, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.bot_name.setFont(font)
        self.bot_name.setObjectName("bot_name")
        self.bot_name.raise_()
        self.bot_icon.raise_()
        self.verticalLayout.addWidget(self.frame)
        self.body_frame = QtWidgets.QFrame(self.centralwidget)
        self.body_frame.setEnabled(True)
        self.body_frame.setMinimumSize(QtCore.QSize(501, 500))
        self.body_frame.setToolTip("")
        self.body_frame.setToolTipDuration(-1)
        self.body_frame.setStyleSheet("background-color: rgb(136, 138, 133);\n"
"border-radius: 15px; ")
        self.body_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body_frame.setObjectName("body_frame")
        self.input_frame = QtWidgets.QFrame(self.body_frame)
        self.input_frame.setEnabled(True)
        self.input_frame.setGeometry(QtCore.QRect(30, 350, 461, 141))
        self.input_frame.setMinimumSize(QtCore.QSize(431, 141))
        self.input_frame.setStyleSheet("")
        self.input_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.input_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.input_frame.setObjectName("input_frame")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.input_frame)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 60, 391, 71))
        self.plainTextEdit.setStyleSheet("*{\n"
"margin-left: 10px;\n"
"padding:10px;\n"
" border-radius: 25px; \n"
"border: 2px solid black;\n"
"background: white; \n"
"color: black;\n"
"}")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.input_frame)
        self.pushButton.setGeometry(QtCore.QRect(400, 70, 51, 51))
        font = QtGui.QFont()
        font.setKerning(True)
        self.pushButton.setFont(font)
        self.pushButton.setToolTipDuration(1000)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Button-Next-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(40, 40))
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.body_frame)
        Chatbot_mainwindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(Chatbot_mainwindow)
        QtCore.QMetaObject.connectSlotsByName(Chatbot_mainwindow)

    def retranslateUi(self, Chatbot_mainwindow):
        _translate = QtCore.QCoreApplication.translate
        Chatbot_mainwindow.setWindowTitle(_translate("Chatbot_mainwindow", "Chatbot"))
        self.hi_label.setText(_translate("Chatbot_mainwindow", "Hi"))
        self.name_label.setText(_translate("Chatbot_mainwindow", "Guest"))
        self.bot_name.setText(_translate("Chatbot_mainwindow", "John Bot"))
        self.pushButton.setToolTip(_translate("Chatbot_mainwindow", "Send Message"))

# if __name__ == '__main__':
#         import sys
#
#         app = QtWidgets.QApplication(sys.argv)
#         bot = QtWidgets.QMainWindow()
#         ui = Ui_Chatbot_mainwindow()
#         ui.setupUi(bot)
#         bot.show()
#         sys.exit(app.exec_())
