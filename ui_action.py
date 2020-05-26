from PyQt5.QtWidgets import QFileDialog
import sqlite3
import manager
import pandas 
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QTableView,QTableWidget,QTableWidgetItem
import PyQt5
import ui_process
import config






def readFile(f):
        f.setEnabled(False)
        fname = QFileDialog.getOpenFileName(f, "Open File", "./", "db (*.db3)")
                                                                                        #打开文件 返回一个字符串第一个是路径， 第二个是要打开文件的类型
                                                                                        #如果用户主动关闭文件对话框，则返回值为空
        if fname[0]:                                                                   #判断路径非空
                                                                    #创建文件对象，不创建文件对象也不报错 也可以读文件和写文件
                                                                                        #open()会自动返回一个文件对象
            print(fname[0])    
        f.closeEvent=f.setEnabled(True)                                         #打开路径所对应的文件， "r"以只读的方式 也是默认的方式
        return fname[0]

def open_config_ui():
    pass

def test_sql(sql):
    
    


    try:
        db=sqlite3.connect(manager.manager.db_address)
        cur=db.cursor()
        cur.execute(sql)
        print(cur.fetchall())
    except Exception as ex:
        print("出现如下异常%s"%ex)
    finally:
        cur.close()
        db.close()
    pass


        #set_sqlite_file
        #打开fileldialog界面
        #返回选中的文件名`
       
def show_table(dataframe):
    pass

def show_set_db_ui(dbtype,father_Form):
    if dbtype=="sqlite":
        readFile(father_Form)
        pass
    elif dbtype=="sqlserver":
        ui_process.show_set_db_ui(father_Form)
        pass
    elif dbtype=="odbc":
        pass
    elif dbtype=="oracle":
        pass
    elif dbtype=="mysql":
        pass

def set_db_message(message):
    print("保存数据库链接信息")
    manager.manager.db_address=message["db_addr"]
    manager.manager.db_dbname=message["db_dbname"]
    manager.manager.db_password=message["db_password"]
    manager.manager.db_username=message["db_username"]
    config.save_config()
        
def save_dbtype(dbtype):
    print("save_dbtype")
    manager.manager.db_type=dbtype
    print("manager.manager.db_type:"+manager.manager.db_type)

    