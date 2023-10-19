"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

from source.web_scrappers.WebScrapper_Costco import WebScrapper_Costco
import sys

from source.web_scrappers.WebScrapper_Walmart import WebScrapper_Walmart

sys.path.append('../../')


def test_walmart_scrapper():

    description = 'Coca cola tins'
    t = WebScrapper_Walmart(description)

    assert t.result is not None
