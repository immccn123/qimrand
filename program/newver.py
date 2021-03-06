# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './newver.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(378, 319)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 354, 291))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.title.setFont(font)
        self.title.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.release_msg = QtWidgets.QPlainTextEdit(self.widget)
        self.release_msg.setEnabled(True)
        font = QtGui.QFont()
        self.release_msg.setFont(font)
        self.release_msg.setReadOnly(True)
        self.release_msg.setObjectName("release_msg")
        self.verticalLayout.addWidget(self.release_msg)
        self.version = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.version.setFont(font)
        self.version.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.version.setObjectName("version")
        self.verticalLayout.addWidget(self.version)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.download = QtWidgets.QCommandLinkButton(self.widget)
        self.download.setObjectName("download")
        self.horizontalLayout.addWidget(self.download)
        self.cancel = QtWidgets.QCommandLinkButton(self.widget)
        self.cancel.setObjectName("cancel")
        self.horizontalLayout.addWidget(self.cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title.setText(_translate("Dialog", "???????????????"))
        self.release_msg.setPlainText(_translate("Dialog", "Error Message "))
        self.version.setText(_translate("Dialog", "?????????{}?????????"))
        self.download.setText(_translate("Dialog", "??????????????????"))
        self.cancel.setText(_translate("Dialog", "??????"))
