#!/usr/bin/env python
# encoding: utf-8
'''
@author: zwd
@contact: zwdeng@163.com
@file: testConnection.py
@time: 2019/8/6 14:40
@function:通过给的连接参数测试是否能够连接上数据库，失败返回False和错误对象msg，成功返回True和游标cursor
@inputParam 用户名 密码 链接 服务名
@returnParam 状态值+错误对象或连接对象
'''
import cx_Oracle
import sqlite3
import backGround.globalConn as gC
import logging

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"    # 日志格式化输出
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"                        # 日期格式
fp = logging.FileHandler('log.txt', encoding='utf-8')
fs = logging.StreamHandler()
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT, handlers=[fp, fs])    # 调用


"""
      处理返回的一维列表
"""
def tuplesToList(fetchTuples):
    returnList = []
    if((fetchTuples==None)|(len(fetchTuples)==0)):
        return []

    for subTuple in fetchTuples:
        if(subTuple==None):
            returnList.append([])
        else:
            returnList.append(list(subTuple))
    return returnList
def connectOracle(userName, passWord, host, serviceName):
    try:
        connection=cx_Oracle.connect(userName, passWord, host + "/" + serviceName)
    except cx_Oracle.DatabaseError as msg:
        return False, str(msg)
    gC._init()
    gC.set_value('userName', userName)
    gC.set_value('passWord', passWord)
    gC.set_value('host', host)
    gC.set_value('serviceName', serviceName)
    return True,'success'

def getOrcaleConnection():
    gC._init()
    userName = gC.get_value('userName')
    passWord = gC.get_value('passWord')
    host = gC.get_value('host')
    serviceName = gC.get_value('serviceName')
    try:
        connection=cx_Oracle.connect(userName, passWord, host + "/" + serviceName)
        return connection
    except cx_Oracle.DatabaseError as msg:
        logging.debug(msg)
        return connection
def getSqliteConnection():

    try:
        connection=sqlite3.connect("test.db")
        return connection
    except cx_Oracle.DatabaseError as msg:
        logging.debug(msg)
        return connection
def sqliteExecute(sql):
    sqlConn = getSqliteConnection()
    try:
        sqliteCursor = sqlConn.cursor()
        sqliteCursor.execute(sql)
        returnList = sqliteCursor.fetchall()
        sqlConn.commit()
        returnList = tuplesToList(returnList)
        return returnList
    except sqlite3.Error as errmsg:
        logging.debug(errmsg)
        logging.debug(sql)
        return []
# 测试语句 第一条正常 第二条报错
# logging.debug(connectOracle('faisdb','faisdb','192.168.36.244','fais'))
# logging.debug(connectOracle('faisdb','faisdb','192.168.36.244','fais1'))
def oracleExcute(sql):
    oracleConn = getOrcaleConnection()
    try:
        oracleCursor = oracleConn.cursor()
        oracleCursor.execute(sql)
        logging.debug(sql)
        returnList = oracleCursor.fetchall()
        oracleConn.commit()
        returnList = tuplesToList(returnList)
        return returnList
    except cx_Oracle.DatabaseError as errmsg:
        logging.debug(errmsg)
        logging.debug(sql)
        return []
def oracleNoFetch(sql):
    oracleConn = getOrcaleConnection()
    try:
        oracleCursor = oracleConn.cursor()
        oracleCursor.execute(sql)
        logging.debug(sql)
        oracleConn.commit()
    except cx_Oracle.DatabaseError as errmsg:
        logging.debug(errmsg)
        logging.debug(sql)
        return []
