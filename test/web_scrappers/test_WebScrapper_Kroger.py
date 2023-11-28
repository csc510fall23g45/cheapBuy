"""
Copyright (c) 2023 Group45
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

from source.web_scrappers.WebScrapper_Kroger import WebScrapper_Kroger

webScrapperKroger = WebScrapper_Kroger('socks')
scrapper = WebScrapper_Kroger('')


def test_get_url_kroger_valid():
    """Test the get_url_kroger method with a valid description."""
    result = webScrapperKroger.get_url_kroger()
    expected = 'https://www.kroger.com/search?query=socks&searchType=default_search&fulfillment=all'
    assert result == expected


def test_get_url_kroger_empty():
    """Test the get_url_kroger method with an empty description."""
    result1 = scrapper.get_url_kroger()
    expected1 = 'https://www.kroger.com/search?query=&searchType=default_search&fulfillment=all'
    assert result1 == expected1


def test_get_driver_chrome():
    assert 'chrome.webdriver' in str(type(scrapper.get_driver()))


def test_run():
    result = webScrapperKroger.run()
    assert 'dict' in str(type(result))


def test_scrap_kroger():
    result = webScrapperKroger.scrap_kroger()
    assert 'Set' in str(type(result))
