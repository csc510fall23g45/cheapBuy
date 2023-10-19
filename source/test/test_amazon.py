"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""
# from source.web_scrappers.WebScrapper import WebScrapper
from source.web_scrappers.WebScrapper import WebScrapper
from source.web_scrappers.WebScrapper_Amazon import WebScrapper_Amazon
from source.web_scrappers.WebScrapper_Bestbuy import WebScrapper_Bestbuy
from source.web_scrappers.WebScrapper_Costco import WebScrapper_Costco
import sys

from source.web_scrappers.WebScrapper_Walmart import WebScrapper_Walmart

sys.path.append('../../')


def test_amazon():
    description = 'Coca cola tins'
    fd = WebScrapper(description)
    assert fd.get_description('amazon') == "Coca cola tins"
