# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\program\python\sql\select_sql.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(481, 300)
        self.splitter_2 = QtWidgets.QSplitter(Form)
        self.splitter_2.setGeometry(QtCore.QRect(70, 80, 291, 41))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.splitter_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(140, 80, 144, 23))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox_2.setItemText(0, _translate("Form", "sqlite"))
        self.comboBox_2.setItemText(1, _translate("Form", "sqlserver"))
        self.comboBox_2.setItemText(2, _translate("Form", "odbc"))
        self.comboBox_2.setItemText(3, _translate("Form", "oracle"))
        self.comboBox_2.setItemText(4, _translate("Form", "mysql"))
        self.pushButton_2.setText(_translate("Form", "确定"))
