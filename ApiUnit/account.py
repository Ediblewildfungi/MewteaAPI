#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' account manage '

import database

#是否开启单元测试模式，开启后单元可独立工作

UNIT_TEST_MODE = True

Mew_DB = database.Mew_DB()

class Mew_USER:
    
    def register (self,name,pwd,email,time):
        insert = "1231213"
        insert = name + "|" + pwd + "|" + email + "|" + time
        print(insert)
        Mew_DB.insert_database("user","user_name|user_pwd|user_email|user_create_time",insert)

    def login (parameter_list):
        pass
    def admin (parameter_list):
        pass
 



if UNIT_TEST_MODE:
    if __name__=='__main__':

        #UNIT TEST CODE
        Mew_USER = Mew_USER()

        Mew_USER.register("NAME","12345","test@mewtea","111")

else:
    pass
