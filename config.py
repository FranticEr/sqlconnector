#创建config文件，修改config文件，初始胡config文件，设定初始化config文件的信息

import os
from lxml import etree


from manager import manager

    #判断是否有配置文件
        #有读取配置文件信息
        #没有则创建
            #读取配置文件信息

        
def read_config():
    config_filename="config.xml"
    if os.path.exists(config_filename) :
        read_xml(config_filename)
        pass
    else :
        init_config_xml()
        read_config()
def read_xml(filename):
    print("im reading config_file")

    tree=etree.parse(filename)
    manager.db_address=tree.xpath("//db_addr")[0].text
    manager.db_dbname=tree.xpath("//db_dbname")[0].text
    manager.db_username=tree.xpath("//db_username")[0].text
    print(manager.db_address)

    print("read xml over")
def creat_config_file():
    config_filename="filename"
    print("im creating config file")
    if os.path.exists(config_filename) :
        pass 

    print("creat config over")
    read_config()
def init_config_xml():

    #保存数据库类型，数据库地址、用户名、密码、库名、sql语句，
    db_elemnet=etree.Element("db_message")
    
    db_addr=etree.Element("db_addr")
    db_addr.text=r"D:\install\火车浏览器\Configuration\config.db3"
    db_elemnet.append(db_addr)
    db_username=etree.Element("db_username")
    db_elemnet.append(db_username)
    db_password=etree.Element("db_password")
    db_elemnet.append(db_password)
    db_dbname=etree.Element("db_dbname")
    db_elemnet.append(db_dbname)
    db_sql=etree.Element("sql")
    db_elemnet.append(db_sql)
    db_dbtable=etree.Element("db_table")
    db_elemnet.append(db_dbtable)
    
    #定时任务的执行时间，任务内容
    job_message=etree.Element("jobtiming")

    #采集文件保存位置，服务器位置
    file_root_path=etree.Element("file_root_path")


    root=etree.Element("root")
    root.append(db_elemnet)
    root.append(job_message)
    root.append(file_root_path)

    #打印
    print(etree.tostring(root, pretty_print=True))

    #生成config文件
    tree=etree.ElementTree(root)   
    tree.write('config.xml', pretty_print=True, xml_declaration=True, encoding='utf-8')

    #定时任务的执行时间，任务内容
    #采集文件保存位置，服务器位置
    # root=etree.Element("root",{"age":"18"})
    # son=etree.Element("son",{"son":"1"})
    # root.append(son)
    # print(etree.tostring(root, pretty_print=True))
    # tree=etree.ElementTree(root)
    # tree.write('config.xml', pretty_print=True, xml_declaration=True, encoding='utf-8')
def save_config():
    config_filename="config.xml"
    if os.path.exists(config_filename) :
        tree=etree.parse(config_filename)
        tree.xpath("//db_addr")[0].text=manager.db_address
        tree.xpath("//db_username")[0].text=manager.db_username
        tree.xpath("//db_password")[0].text=manager.db_password
        tree.xpath("//db_dbname")[0].text=manager.db_dbname
        print(manager.db_dbname)
        tree.write('config.xml', pretty_print=True, xml_declaration=True, encoding='utf-8')
        pass
    else :
        init_config_xml()
        save_config()

if __name__ == "__main__":
    tree=etree.parse("config.xml")
    manager.db_address=tree.xpath("//db_addr")[0].text
    print(manager.db_address)
    print(type(manager.db_address))
    pass