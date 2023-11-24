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

def initiate_database():
    create_user_table = """
        CREATE TABLE IF NOT EXISTS users (
            username VARCHAR(25) NOT NULL,
            password VARCHAR(25) NOT NULL,
            PRIMARY KEY(username)
        );
    """
    (result, error) = execute_query(create_user_table)
    if(error):
        print("SQLite error: ", error)

    create_wishlist_table = """
        CREATE TABLE IF NOT EXISTS wishlist (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(25) NOT NULL,
            item_name VARCHAR(100) NOT NULL,
            price DECIMAL(10, 8) NOT NULL,
            website VARCHAR(50),
            link VARCHAR(250),
            FOREIGN KEY (username) REFERENCES users(username)
        );
    """
    (result, error) = execute_query(create_wishlist_table)
    if(error):
        print("SQLite error: ", error)

def create_user(username, password):
    add_user_query = "INSERT INTO users(username, password) VALUES (?,?);"
    (result, error) = execute_query(add_user_query, (username, password))
    if error:
        if error.sqlite_errorname == 'SQLITE_CONSTRAINT_PRIMARYKEY':
            return False
        else:
            return None
    else:
        return True

def view_users():
    view_users_query = "SELECT * FROM users;"
    (result, error) = execute_query(view_users_query)
    if error:
        return None
    else:
        return result

def get_password(username):
    select_pass_query = "SELECT password FROM users WHERE username = ?"
    (result, error) = execute_query(select_pass_query, [username])
    if error:
        return None
    elif len(result):
        return result[0][0]
    else:
        return False

def add_wishlist_item(username, item_name, price, website, link):
    add_item_query = "INSERT INTO wishlist(username, item_name, price, website, link) VALUES (?,?,?,?,?);"
    (result, error) = execute_query(add_item_query, (username, item_name, price, website, link))
    if error:
        print(error.sqlite_errorname)
        if error.sqlite_errorname == 'SQLITE_CONSTRAINT_FOREIGNKEY':
            return False
        else:
            return None
    else:
        return True

def delete_wishlist_item(username, id):
    delete_item_query = "DELETE FROM wishlist WHERE username=? AND id=?;"
    (result, error) = execute_query(delete_item_query, [username, id])
    if error:
        return None
    else:
        return True

def view_wishlist_items(username):
    view_items_query = "SELECT * FROM wishlist WHERE username=?;"
    (result, error) = execute_query(view_items_query, [username])
    if error:
        return None
    else:
        return result
