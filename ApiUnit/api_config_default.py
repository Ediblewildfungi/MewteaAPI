#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Config '

__author__ = 'MewTea'

#应用配置

#数据库配置
class DB_CONFIG:
    
    HOST = "0.0.0.0"
    PORT = "3306"
    USER = "root"
    PASSWORD = ""
    DATABASE_NAME1 = "DBNAME"



if __name__=='__main__':

    #UNIT TEST CODE

    print(DB_CONFIG.HOST)