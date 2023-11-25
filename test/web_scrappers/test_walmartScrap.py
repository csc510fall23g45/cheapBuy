from source.web_scrappers.walmartScrap import scrapeops_url
from source.web_scrappers.walmartScrap import response_call
from source.web_scrappers.walmartScrap import SCRAPEOPS_API_KEY
from urllib.parse import unquote

# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urlencode

def test_scrapeops_url():
    url = 'https://www.walmart.com/search?q=maggi&sort=price_low'
    result = scrapeops_url(url)
    expected = "https://proxy.scrapeops.io/v1/?api_key=453fce39-0418-4083-8bd4-6f9e6376b8c7&url="+url+"&country=us"
    assert result == expected

def test_response_call():
    status_code = response_call()
    expected = 401
    assert status_code== 401