import random
import sys
import traceback
import webbrowser

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QAction, QApplication, QCommandLinkButton,
                             QDialog, QLabel, QMainWindow, QMenu, QMenuBar,
                             QMessageBox, QPlainTextEdit, QPushButton,
                             QTextBrowser)

from about import Ui_Dialog
from err import Ui_Errorbox
from window import Ui_MainWindow


def show(error, msg):
    w = Errorbox(msg = error,reason = msg)
    w.exec_()
        
class Errorbox(QDialog, Ui_Errorbox):
    def __init__(self, parent=None, msg="Error msg", reason=""):
        super(Errorbox, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("出错了！")
        self.err_reason.setText(reason)
        self.plainTextEdit.setPlainText(msg)


class About(QDialog,Ui_Dialog):
    def __init__(self, parent=None):
        super(About, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("关于")
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
            show(traceback.format_exc(), "输入数据非法")
        except OverflowError:
            show(traceback.format_exc(), "输入数据过大")
        except Exception:
            show(traceback.format_exc(), "未知错误")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
