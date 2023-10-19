"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

from source.web_scrappers.WebScrapper_Bjs import WebScrapper_Bjs
import sys
sys.path.append('../../../')


def test_bjs_scrapper():

    description = 'Coca cola tins'
    t = WebScrapper_Bjs(description)

    assert t.result is not None
