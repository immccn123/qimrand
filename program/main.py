import random
import sys
import traceback
import webbrowser

import requests
from PyQt5.QtWidgets import (QDialog, QMainWindow, QApplication)

import newver
from about import Ui_Dialog
from err import Ui_Errorbox
from window import Ui_MainWindow

from PyInstaller.utils.hooks import collect_data_files, collect_submodules


version = 'v1.0.2'
newest_version_status = {}


def show(error, msg):
    w = Errorbox(msg=error, reason=msg)
    w.exec()


class Errorbox(QDialog, Ui_Errorbox):
    def __init__(self, parent=None, msg="Error msg", reason=""):
        super(Errorbox, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("出错了！")
        self.err_reason.setText(reason)
        self.plainTextEdit.setPlainText(msg)

# class MoreBox()


class About(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(About, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("关于")
        self.commandLinkButton.clicked.connect(self.ps)
        self.commandLinkButton_2.clicked.connect(self.gh)
        self.update.clicked.connect(self.chk_update)

    def ps(self):
        webbrowser.open("https://github.com/immccn123/")

    def gh(self):
        webbrowser.open("https://github.com/immccn123/qimrand/")

    def chk_update(self):
        global newest_version_status
        update_status = requests.get(
            "https://api.github.com/repos/immccn123/qimrand/releases/latest")
        newest_version_status = update_status.json()
        if version != newest_version_status["tag_name"]:
            new_version_dig = VerDig()
            new_version_dig.version.setText(
                "新版本{}可用。下载吗？".format(newest_version_status["tag_name"]))
            new_version_dig.release_msg.setPlainText(
                newest_version_status["body"])
            new_version_dig.exec()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("随机学号生成")
        self.con.clicked.connect(self.buttonClicked)
        self.about.triggered.connect(self.showAboutDig)

    def showAboutDig(self):
        w = About()
        w.exec()

    def buttonClicked(self):
        try:
            self.screen.display(random.randint(1, int(self.input.text())))
        except ValueError:
            show(traceback.format_exc(), "输入数据非法")
        except OverflowError:
            show(traceback.format_exc(), "输入数据过大")
        except Exception:
            show(traceback.format_exc(), "未知错误")


class VerDig(newver.Ui_Dialog, QDialog):
    def __init__(self, parent=None):
        super(newver.Ui_Dialog, self).__init__(parent)
        self.setupUi(self)
        self.cancel.clicked.connect(self.close)
        self.download.clicked.connect(self.down)

    def down(self):
        webbrowser.open(
            str(newest_version_status["assets"][0]["browser_download_url"]))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    myWin = MainWindow()
    myWin.show()

    a = 0
    a = app.exec()

    sys.exit(a)
