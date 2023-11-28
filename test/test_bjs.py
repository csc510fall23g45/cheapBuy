"""
Copyright (c) 2023 Group45
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

from source.web_scrappers.WebScrapper import WebScrapper
import sys

sys.path.append('../')


def test_bjs():
    description = 'Coca cola tins'
    fd = WebScrapper(description)
    assert fd.get_description('bjs') == "Coca cola tins"
