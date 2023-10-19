from source.web_scrappers.WebScrapper_Amazon import WebScrapper_Amazon
import sys
sys.path.append('../../../')


def test_amazon_scrapper():

    description = 'Coca cola tins'
    t = WebScrapper_Amazon(description)

    assert t.result is not None