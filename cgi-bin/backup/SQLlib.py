#!/usr/bin/python3

import pymysql.cursors
#import re
#import numpy as np

def get_user_info(cursor, user_code):
    SQL = "select info_name,info,register_date,provider_name,URL,provide_date from personal_details natural join info_classify natural join provide natural join provider_companies where user_code=\'%s\'" % user_code
    cursor.execute(SQL)
    rets = cursor.fetchall()
    return rets
#特定の行を抽出するSQL文を作成（PyMySQLだと列名の指定とかできなさそうだったので）
#columns:列名、tables:テーブル名、cond:条件文('クオーテーションに注意)

def get_provider_name(cursor, provider_name):
    SQL = "select info_name,info,register_date,user_code,URL,provide_date from personal_details natural join info_classify natural join provide natural join provider_companies where provider_name=\'%s\'" % provider_name
    cursor.execute(SQL)
    rets = cursor.fetchall()
    return rets

def select(columns, tables, cond):
    SELECTsql = "select %s from %s where %s;" % (columns, tables, cond)
    return SELECTsql

#特定の行を追加するSQL文を作成
def insert(tables, new_data):
    INSERTsql = "insert into %s values(%s);" % (tables,new_data)
    return INSERTsql

#例外処理
def execute(cursor, sen):
    try:
        cursor.execute(sen)
    except Exception as e:
        a = 1
    return

#連番を取得するための関数
def get_max_num(cursor,column, table, cond):
    maxfunc = "max(%s)" % column
    sen = select(maxfunc, table, cond)
    cursor.execute(sen)
    rets = cursor.fetchall()
    return rets[0][maxfunc] if len(rets) != 0 else 0

#データベース接続
def connect_personalDB():
    conn = pymysql.connect(host = 'db-for-japan1.cvs5tutsbarq.ap-northeast-1.rds.amazonaws.com',
            user='apserver',
            password='alljapan',
            db='personal_manager',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor)
    return conn

#データベース切断
def close_DB(conn):
    conn.close()
    return

#個人情報を追加する（失敗すると-1、成功すると追加したpersonal_info_idを返す）
def insert_info(cursor, user_code, info_name, info):
    sen = select("user_code", "user", "user_code=\'%s\'" % user_code)
    cursor.execute(sen)
    rets = cursor.fetchall()
    #userが存在しなければ、-1を返す、
    if len(rets) == 0:
        print("user doesn't exist")
        return -1
    else:
        info_class = 0
        sen = select("info_class,info_name", "info_classify", "info_name=\'%s\'" % (info_name))
        cursor.execute(sen)
        rets = cursor.fetchall()
        #print_all(rets);
        #info_classにinfo_nameが存在しなければ、追加する
        if len(rets) == 0:
            info_class = get_max_num(cursor, "info_class", "info_classify", "1=1") +1
            sen = insert("info_classify", "%d,\'%s\'" % (info_class, info_name))
            execute(cursor,sen)
        else:
            info_class = rets[0]['info_class']
        per_id = get_max_num(cursor, "personal_info_id", "personal_details", "user_code=\'%s\' group by user_code" % user_code) +1
        sen = insert("personal_details", "\'%s\',%d,%d,\'%s\',curdate()" % (user_code, per_id, info_class, info))
        execute(cursor,sen)
    return per_id

#個人情報と企業情報を紐づける
def provide(cursor, user_code, per_id, company_name, URL):
    provider_code = 0
    sen = select("provider_code,provider_name", "provider_companies", "provider_name=\'%s\'" % company_name)
    cursor.execute(sen)
    rets = cursor.fetchall()
    #print_all(rets)

    #provider_nameが存在しなければ、companyに追加。
    if len(rets) == 0:
        provider_code = get_max_num(cursor, "provider_code", "provider_companies", "1=1") +1
        sen = insert("provider_companies", "%d,\'%s\',\'%s\'" % (provider_code, company_name, URL))
        #print(sen)
        execute(cursor,sen)
    else:
        provider_code = rets[0]['provider_code']

    #provideテーブルに追加
    sen = insert("provide", "\'%s\',%d,%d,curdate()" % (user_code, per_id, provider_code))
    #print(sen)
    execute(cursor,sen)



#すべての行を標準出力
def print_all(rets):
    for r in rets:
        print(r)
    return
