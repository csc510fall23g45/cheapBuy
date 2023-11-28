"""
Copyright (c) 2023 Group45
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

from source.web_scrappers.WebScrapper_Costco import WebScrapper_Costco
import sys
sys.path.append('../')


def test_costco_scrapper():

    description = 'Coca cola tins'
    t = WebScrapper_Costco(description)

    assert t.result is not None
