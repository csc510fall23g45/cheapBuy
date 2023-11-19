"""
Copyright (c) 2023 Sai Raj
This code is licensed under MIT license (see LICENSE.MD for details)

@author: sairajzero
"""

import sqlite3

DB_NAME = 'test.db'

def execute_query(query, values = []):
    result = None
    error = None
    try:
        conn = sqlite3.connect('test.db')
        conn.execute("PRAGMA foreign_keys = 1")
        cursor = conn.cursor()
        with conn:
            cursor.execute(query, values)
            result = cursor.fetchall()
    except sqlite3.Error as e:
        print(e)
        error = e
    finally:
        if conn:
            conn.close()
        return (result, error)

