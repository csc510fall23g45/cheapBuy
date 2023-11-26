from source.web_scrappers.WebScrapper_TraderJoes import WebScrapper_TraderJoes
webScrapper_TraderJoes = WebScrapper_TraderJoes('socks')
scraper = WebScrapper_TraderJoes('')

def test_run():
    result = webScrapper_TraderJoes.run()
    assert 'dict' in str(type(result))

def test_get_driver_chrome():
    assert 'chrome.webdriver' in str(type(scraper.get_driver()))

def test_get_url_traderjoes_valid():
    result = webScrapper_TraderJoes.get_url_traderjoes()
    expected= 'https://www.traderjoes.com/home/search?q=socks&global=yes'
    assert result==expected

def test_get_url_traderjoes_empty():
    result1 = scraper.get_url_traderjoes()
    expected1= 'https://www.traderjoes.com/home/search?q=&global=yes'
    assert result1==expected1

def test_scrap_traderjoes():
    result = webScrapper_TraderJoes.scrap_traderjoes()
    assert 'list' in str(type(result))