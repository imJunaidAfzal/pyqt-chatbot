from chat_bot import Ui_Chatbot_mainwindow
from welcome_screen import Ui_welcome_win
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


if __name__ == '__main__':

        app = QtWidgets.QApplication(sys.argv)
        bot = QtWidgets.QMainWindow()
        ui = Ui_Chatbot_mainwindow()
        ui.setupUi(bot)
        bot.show()

        sys.exit(app.exec_())
