"""
Copyright (c) 2023 Group45
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

from source.database import execute_query, initiate_database, create_user, view_users, get_password, add_wishlist_item, delete_wishlist_item, view_wishlist_items
import pytest


def test_initiate_database():
    result = initiate_database()
    assert result is None


def test_create_user():
    initiate_database()
    result = create_user("Mahathi", "Kolishetty@1")
    assert result is True


def test_execute_query():
    initiate_database()
    query = "SELECT * FROM users;"
    result, error = execute_query(query)
    assert result == [('Mahathi', 'Kolishetty@1')]
    print(result)
    assert error is None


def test_view_users():
    initiate_database()
    result = view_users()
    assert result == [('Mahathi', 'Kolishetty@1')]


def test_get_password():
    initiate_database()
    create_user("TestUser", "TestPassword")
    result = get_password("TestUser")
    assert result == "TestPassword"


def test_add_wishlist_item():
    result = add_wishlist_item("TestUser", "Item1", 10.0, "Website1", "Link1")
    assert result is True


def test_view_wishlist_items():
    create_user("TestUser1", "TestPassword1")
    result = view_wishlist_items("TestUser")
    assert result == [{'id': 1, 'link': 'Link1',
                       'price': 10, 'title': 'Item1', 'website': 'Website1'}]


def test_delete_wishlist_item():
    result = delete_wishlist_item("TestUser", 1)
    assert result is True
