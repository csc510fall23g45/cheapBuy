"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

from source.web_scrappers.WebScrapper import WebScrapper

import sys

sys.path.append('../')


def test_amazon():
    description = 'Coca cola tins'
    fd = WebScrapper(description)
    assert fd.get_description('amazon') == "Coca cola tins"
