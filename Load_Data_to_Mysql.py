#!/usr/bin/python
#coding: utf-8

"""
Load_Data_to_Mysql.py

load data to mysql
"""

import os
import MySQLdb

class LoadData(object):

    """load data.


    Attributes:
        no.
    """

    def __init__(self):

        """initiate object.


        Attributes:
            no.
        """
        self.data_dir = "D:/QQ/Desktop/"
        try:
            self.conn = MySQLdb.connect(host='localhost', port=3306,
                                    user='root', passwd='root', db="stock")
        except Exception, e:
            print e
        self.cursor = self.conn.cursor()
        self.file_name = "My_Record"

    def _get_comment(self):

        """get comment from files.


        Attributes:
            no.
        """
        temp = open(self.data_dir)
        tmp = temp.readlines()
        temp.close()
        result = []
        for line in tmp:
            result.append(line.encode("utf-8").split())
        return result

    def _insert_into_mysql(self, data):

        """insert data into mysql.


        Attributes:
            no.
        """
        for line in records:
            sql = "INSERT INTO My_Account (C_Time, C_Object, C_Num, Total_Price) " \
                  "VALUES ('%s', '%s', %s, %s)" % (line[0], line[1], line[2], line[3])
            try:
                self.cursor.execute(sql)
            except Exception, e:
                print e

    def main(self):

        """main functino..


        Attributes:
            no.
        """
        all_files = os.listdir(self.data_dir)
        if self.file_name in all_files:
            records = self._get_comment()
            if records:
                self._insert_into_mysql(records)

        self.conn.commit()
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    load_data_to_mysql = LoadData()
    load_data_to_mysql.main()

