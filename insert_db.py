"""
System administration, Machine supervision project:

    this module allowed to connect to the GrafTable data base, in PhpMyAdmin
    and insert data in different tables

    Copyright (c) 2021 Zohra BACHI

"""
import mysql.connector


def connect_db():
    """
        connect to the MySQL data base : GrafTable
        in phpMyAdmin

    """
    my_db = ""
    try:
        my_db = mysql.connector.connect(
            host="192.168.64.2",
            user="zora",
            password="123",
            database="GrafTable")

    except mysql.connector.Error as err:
        print(f'Something went wrong: {err}')

    return my_db


#
# ---------------------------------- insert into database---------------------
#
def sql_connect_db(table_name, value1, value2, value3, value4):
    """
        Insert value in tables : CPU, Disk or MV.

    """
    sql = ""
    try:
        my_db = connect_db()
        my_cursor = my_db.cursor()
        if table_name == 'CPU':

            sql = f"INSERT INTO {table_name}(host, cpPercent1, cpPercent2, cpPercent3, cpPercent4) " \
                  f"VALUES (%s, %s,%s,%s,%s)"

        elif table_name == 'Disk':
            sql = f"INSERT INTO {table_name}(host, diskPercent, diskFreeBytes, diskUsedBytes, diskTotalBytes)" \
                  f"VALUES (%s, %s, %s, %s, %s)"
        elif table_name == 'MV':
            sql = f"INSERT INTO {table_name}(host, mvPercent, mvUsedBytes, mvFreeBytes, mvAvaibleBytes)" \
                  f"VALUES (%s, %s, %s, %s, %s)"

        val = ("192.168.64.2", value1, value2, value3, value4)

    except mysql.connector.Error as err:
        print(f'Something went wrong: {err}')

        return
    my_cursor.execute(sql, val)
    my_db.commit()
    my_db.close()


#
# ---------------------------------- insert into table IO_byte---------------------
#
def sql_connect_db_io(table_name, value1, value2):
    """
        function takes three parameters:

        insert value in IO tables
    """
    my_db = connect_db()

    try:
        my_cursor = my_db.cursor()
        sql = f"INSERT INTO {table_name}(host, ioBytesSent, ioBytesRecv) VALUES (%s, %s, %s)"
        val = ("192.168.64.2", value1, value2)

    except mysql.connector.Error as err:
        print(f'Something went wrong: {err}')

        return
    my_cursor.execute(sql, val)
    my_db.commit()
    my_db.close()
