import sqlite3
from sqlite3 import Error

#create connection to db
def cc():
    connection = None
    try:
        connection = sqlite3.connect("Assets\gameData.db")
    except Error as e:
        input(e)
    return connection

#get data from name        
def queryField(table,name):
    connection=cc()
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT * FROM {} WHERE name="{}"'.format(table,name))
        return cursor.fetchall()
    except Error as e:
        input(e)
    connection.close()

#return values for loot list
def lootListReturn(level):
    connection=cc()
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT name FROM ItemTable WHERE lootList="{}"'.format(level))
        lootList = []
        for i in cursor.fetchall():
            lootList.append(i[0])
        return(lootList)
    except Error as e:
        input(e)
    connection.close()

#return values for loot list
def shopListReturn(level):
    connection=cc()
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT name FROM ItemTable WHERE lootList BETWEEN 1 AND"{}"'.format(level))
        lootList = []
        for i in cursor.fetchall():
            lootList.append(i[0])
        return(lootList)
    except Error as e:
        input(e)
    connection.close()
    
#deletes record from SaveData by name
def delData(name):
    connection=cc()
    cursor = connection.cursor()
    delData = 'DELETE FROM SaveData WHERE name = "{}"'.format(name)
    try:
        cursor.execute(delData)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        input(e)
    connection.close()

#Gets all info from SaveData table
def getAllData(table):
    connection=cc()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM {}".format(table))
        return cursor.fetchall()
    except Error as e:
        input(e)
    connection.close()
