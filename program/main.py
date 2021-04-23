import random
import sys
import webbrowser

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QAction, QApplication, QCommandLinkButton,
                             QDialog, QMainWindow, QMenu, QMenuBar,
                             QMessageBox, QPushButton, QTextBrowser)

from about import Ui_Dialog
from window import Ui_MainWindow


def show():
    msgbox = QMessageBox()
    # msgbox.setIcon(QMessageBox.warning)
    msgbox.setText("键入的值非法。")
    msgbox.setWindowTitle("出错拉")
    msgbox.setStandardButtons(QMessageBox.Ok)
    rv = msgbox.exec()
    if rv == QMessageBox.Ok:
        return
        

class About(QDialog,Ui_Dialog):
    def __init__(self, parent=None):
        super(About, self).__init__(parent)
        self.setWindowTitle("关于")
        self.setupUi(self)
        self.commandLinkButton.clicked.connect(self.ps)
        self.commandLinkButton_2.clicked.connect(self.gh)
    def ps(self):
        webbrowser.open("https://github.com/immccn123/")
    def gh(self):
        webbrowser.open("https://github.com/immccn123/qimrand/")

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("随机学号生成")
        self.con.clicked.connect(self.buttonClicked)
        self.about.triggered.connect(self.aabout)
    def aabout(self):
        w = About()
        w.exec_()
    def buttonClicked(self):
        try:
            self.screen.display(random.randint(1,int(self.input.text())))
        except ValueError:
            show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
