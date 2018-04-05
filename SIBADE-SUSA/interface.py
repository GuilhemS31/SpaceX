# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt4 import QtCore, QtGui
#from PyQt4.QtGui import *
#from PyQt4.QtCore import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(617, 442)
        self.verticalLayoutWidget_2 = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 601, 421))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.comboBox = QtGui.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.verticalLayout_2.addWidget(self.comboBox)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.tableView = QtGui.QTableView(self.verticalLayoutWidget_2)
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.horizontalLayout_2.addWidget(self.tableView)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textBrowser = QtGui.QTextBrowser(self.verticalLayoutWidget_2)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        self.pushButton = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.lineEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayoutWidget_2.raise_()
        self.tableView.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.pushButton.setText(_translate("Dialog", "PushButton", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
