#!/usr/bin/env python
# encoding: utf-8
'''
@author: zwd
@contact: zwdeng@163.com
@file: getBackupInfo.py
@time: 2019/8/6 14:54
@function:查询备份的信息
@inputParam:
@returnParam:
'''
import sqlite3
import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"    # 日志格式化输出
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"                        # 日期格式
fp = logging.FileHandler('log.txt', encoding='utf-8')
fs = logging.StreamHandler()
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT, handlers=[fp, fs])    # 调用



"""
      增加一条新备份信息
"""
def insertBackupInformation(backupVersion,backupTime,beginTime,endTime):
    sqlite3Conn = sqlite3.connect('test.db')
    sqlite3Cursor = sqlite3Conn.cursor()
    sql = "INSERT INTO backupInformation(backupVersion,backupTime,beginTime,endTime,hasContrast) VALUES('%d',%d,%d,%d,0);"%(backupVersion,backupTime,beginTime,endTime)
    sqlite3Cursor.execute(sql)
    sqlite3Cursor.close()
    sqlite3Conn.commit()
    sqlite3Conn.close()
"""
增加新的对象(表 存储过程)和版本
"""
def insertBackupObject(backupVersion,objectName,backupObjectName,ObjectType):
    sqlite3Conn = sqlite3.connect('test.db')
    sqlite3Cursor = sqlite3Conn.cursor()
    sql = "INSERT INTO backupObjectNameList(backupVersion,objectName,backupObjectName,ObjectType) VALUES('%s','%s','%s','%s');"%(backupVersion,objectName,backupObjectName,ObjectType)
    sqlite3Cursor.execute(sql)
    sqlite3Cursor.close()
    sqlite3Conn.commit()
    sqlite3Conn.close()





"""
      增加对比结果
"""
def insertContrastResults(backupObjectName,differenceType,primaryKeyId,differenceField):
    sqlite3Conn = sqlite3.connect('test.db')
    sqlite3Cursor = sqlite3Conn.cursor()
    sql = "INSERT INTO contrastResults(backupObjectName,differenceType,primaryKeyId,differenceField) VALUES('%s','%s','%s','%s');"%(backupObjectName,differenceType,primaryKeyId,differenceField)
    sqlite3Cursor.execute(sql)
    sqlite3Cursor.close()
    sqlite3Conn.commit()
    sqlite3Conn.close()


insertBackupObject(1,'表1','backup4',1)
