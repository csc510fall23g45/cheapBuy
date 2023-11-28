"""
Copyright (c) 2023 Group45
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""


import sys

from source.web_scrappers.WebScrapper_Ebay import WebScrapper_Ebay

sys.path.append('../')


def test_ebay_scrapper():

    description = 'Coca cola tins'
    t = WebScrapper_Ebay(description)

    assert t.result is not None
