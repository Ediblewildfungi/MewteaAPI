#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' database link unit '

import os
import codecs
import pymysql
import api_config

#是否开启单元测试模式，开启后单元可独立工作

UNIT_TEST_MODE = True

DBCONFIG = api_config.DB_CONFIG

DBHOST = DBCONFIG.HOST
DBUSER = DBCONFIG.USER
DBPWD  = DBCONFIG.PASSWORD
DBNAME = DBCONFIG.DATABASE_NAME1

db = pymysql.connect(DBHOST,DBUSER,DBPWD,DBNAME)

# 数据库类
class Mew_DB:
    
    def link_database(self):
        db = pymysql.connect(DBHOST,DBUSER,DBPWD,DBNAME)
        return 0

    def __init_input(self,type,input):
        
        if type == "insert":

            #格式化处理输入的字符串,删除逗号
            init_output = input.replace(",", "")
            return init_output
        else:
            pass
        
    #数据库插入函数
    def insert_database(self,table,name,value):
        cursor = db.cursor() 

        #格式化处理输入
        name  = self.__init_input("insert",name)
        table = self.__init_input("insert",table)
        value = self.__init_input("insert",value)
       
        #分割输入的参数
        name  = name.split('|')
        value = value.split('|')

        #将输入载入sql语句
        sql_pre   = "INSERT INTO " + table
        sql_retro = "VALUES"

        sql_pre = sql_pre + " ("

        #确保2输入参数相对应
        if len(name) == len(value) :
            print(len(name))
            
            #将参数往sql_pre 后叠加
            for x in name:
                sql_pre = sql_pre + x + ", "
            
            #删除最后2个逗号空格  补上括弧
            sql_pre = sql_pre[:-2] + ") "
            
            # 前段格式化完成
            # print(sql_pre)

            sql = sql_pre + sql_retro + " ("

            #叠加value参数
            for x in value:
                sql = sql + "'" + x +"',"
            sql = sql[:-1] + ") "

            # sql语句格式化完成
            print(sql)

            # 执行sql插入语句
            try:
                # 执行sql语句
                cursor.execute(sql)
                db.commit()
                return True

            except:
                # 发生错误，回滚
                db.rollback()
                return False

            

        else:

            #错误信息
            return False
        

        # sql = "INSERT INTO %s %s VALUES '%s'" % (table,name,value)
        # sql = "INSERT INTO monster_sign( user_id, pic_name, creat_sign_time, status) VALUES ('1222','1333','0000-00-00 00:00:00','1555')"
        # cursor.execute(sql)
        # try:

        #     # 执行sql语句
        #     cursor.execute(sql)
        #     db.commit()

        # except:

        #     # 发生错误，回滚
        #     db.rollback()

    def close_database(self):
        
        db.close()
        return 0


if UNIT_TEST_MODE:
    if __name__=='__main__':

        #UNIT TEST CODE

        MewDB = Mew_DB()

        if MewDB.insert_database("monster_sign","user_id|pic_name|creat_sign_time|status","1111|2222|2019-05-10 09:51:30|13333"):
            print('OK')
        else:
            print('ERR')

        MewDB.close_database()
        
        print('OK')

else:
    pass