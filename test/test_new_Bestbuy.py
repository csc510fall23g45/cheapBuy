"""
Copyright (c) 2023 Group45
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

from source.web_scrappers.WebScrapper_Bestbuy import WebScrapper_Bestbuy

import sys

sys.path.append('../')


def test_bestbuy_scrapper():

    description = 'Coca cola tins'
    t = WebScrapper_Bestbuy(description)

    assert t.result is not None
