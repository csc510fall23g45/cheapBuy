"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""
from source.web_scrappers.WebScrapper_Bestbuy import WebScrapper_Bestbuy
from source.web_scrappers.WebScrapper_Costco import WebScrapper_Costco
import sys

from source.web_scrappers.WebScrapper_Walmart import WebScrapper_Walmart

sys.path.append('../../../')


def test_bestbuy_scrapper():

    description = 'Coca cola tins'
    t = WebScrapper_Bestbuy(description)

    assert t.result is not None
