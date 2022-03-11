
import json
import sqlite3

def InitDbIfNotExisted():
    conn = sqlite3.connect('customer.db')
    print("Opened database successfully")

    conn.execute('''CREATE TABLE IF NOT EXISTS  CUSTOMER
         (ID INTEGER PRIMARY KEY  AUTOINCREMENT,
         PHONE           TEXT    NOT NULL,
         DATA           TEXT    NOT NULL);''')
    print("Table created successfully")
    conn.close()


def InsertDb(phone, data):
    try:
        conn = sqlite3.connect('customer.db')
        jsonData = json.dumps(data)
        sql = f'''insert into CUSTOMER(PHONE,"DATA") \
            Values('{phone}','{jsonData}')'''
        conn.execute(sql)
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)
        pass