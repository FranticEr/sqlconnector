import Ui_sql
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import *
import PyQt5
import ui_action
import Ui_sqlserver_set_ui
import Ui_select_sql
from PyQt5 import QtWidgets
import Ui_sqlserver_set_ui
import manager

def show_widget():
    print("打开主界面")
    app=QtWidgets.QApplication(sys.argv)

    main_widget=QtWidgets.QWidget()
    widget_designer=Ui_sql.Ui_Form()
    widget_designer.setupUi(main_widget)
    #set=pushButton:设置数据库链接
    widget_designer.pushButton.clicked.connect(lambda : show_select_sql(main_widget))
    #运行在textedit中的sql语句，并将结果现实在tableview中
    widget_designer.pushButton_2.clicked.connect(lambda : ui_action.test_sql(widget_designer.textEdit.toPlainText()))
    main_widget.show()
    sys.exit(app.exec_())

def show_select_sql(Widget):
    print("打卡数据库类型选取界面")
    Widget.setEnabled(False)
    select_sql_ui=QtWidgets.QDialog()
    select_sql_ui_designer=Ui_select_sql.Ui_Form()

    select_sql_ui_designer.setupUi(select_sql_ui)


    select_sql_ui_designer.comboBox_2.currentTextChanged.connect(lambda : print(select_sql_ui_designer.comboBox_2.currentText()))
    select_sql_ui_designer.pushButton_2.clicked.connect(lambda : ui_action.save_dbtype(select_sql_ui_designer.comboBox_2.currentText()))
    select_sql_ui_designer.pushButton_2.clicked.connect(lambda : ui_action.show_set_db_ui(select_sql_ui_designer.comboBox_2.currentText(),select_sql_ui))
    
    
    select_sql_ui.exec()
    Widget.setEnabled(True)

def show_set_db_ui(father_Form):
    print("打开数据库链接设置界面")

    designer=Ui_sqlserver_set_ui.Ui_Form()
    form=QtWidgets.QDialog()
    designer.setupUi(form)

    designer.pushButton_2.clicked.connect(lambda :collect_message(designer))
    form.exec()
    pass

def collect_message(designer):
    print("收集数据库链接设置信息")
    db_username=designer.lineEdit.text()
    db_password=designer.lineEdit_2.text()
    db_addr=designer.lineEdit_3.text()
    db_dbname=designer.lineEdit_4.text()
    
    message={"db_username":db_username,"db_password":db_password,"db_addr":db_addr,"db_dbname":db_dbname}
    print("db_dbname"+message["db_dbname"])
    ui_action.set_db_message(message)






    