"""
Copyright (c) 2023 Group45
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

from source.web_scrappers.traderJoeyScrap import scrapeops_url
from source.web_scrappers.traderJoeyScrap import response_call
from source.web_scrappers.traderJoeyScrap import SCRAPEOPS_API_KEY
from urllib.parse import unquote

# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urlencode


def test_scrapeops_url():
    url = 'https://www.traderjoes.com/home/search?q=potato'
    result = scrapeops_url(url)
    expected = "https://proxy.scrapeops.io/v1/?api_key=None&url=https://www.traderjoes.com/home/search?q=potato&country=us"
    assert result == expected


def test_response_call():
    status_code = response_call()
    expected = 401
    assert status_code == 401
