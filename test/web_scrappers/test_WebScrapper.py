from source.web_scrappers.WebScrapper import WebScrapper

WebScrapper1 = WebScrapper("Pens")
WebScrapper = WebScrapper("Socks")


def test_get_description_NA():
    na = WebScrapper.get_description('foodlion')
    assert na == "N/A"

def test_get_description_walmart():
    walmart_desc = WebScrapper.get_description('walmart')
    actual_desc = "Socks"
    assert walmart_desc == actual_desc

def test_get_description_amazon():
    amazon_desc = WebScrapper.get_description('amazon')
    actual_desc = "Socks"
    assert amazon_desc == actual_desc

''' 
TODO
def test_get_description_ebay():
    ebay_desc = WebScrapper.get_description('ebay')
    actual_desc = "Socks"
    assert ebay_desc == actual_desc
'''

def test_get_description_costco():
    costco_desc = WebScrapper.get_description('costco')
    actual_desc = "Socks"
    assert costco_desc == actual_desc

def test_get_description_bjs():
    bjs_desc = WebScrapper1.get_description('bjs')
    actual_desc = "Pens"
    assert bjs_desc == actual_desc

def test_get_description_bestbuy():
    bestbuy_desc = WebScrapper1.get_description('bestbuy')
    actual_desc = "Pens"
    assert bestbuy_desc == actual_desc

def test_get_description_traderjoes():
    traderjoes_desc = WebScrapper1.get_description('traderjoes')
    actual_desc = "Pens"
    assert traderjoes_desc == actual_desc

def test_get_description_kroger():
    kroger_desc = WebScrapper1.get_description('kroger')
    actual_desc = "Pens"
    assert kroger_desc == actual_desc

def test_call_scrapper_amazon():
    amazon_res_socks = WebScrapper.call_scrapper('amazon')
    assert len(amazon_res_socks) != 0

def test_call_scrapper_walmart():
    walmart_res_socks = WebScrapper.call_scrapper('walmart')
    assert len(walmart_res_socks) != 0

def test_call_scrapper_bjs():
    bjs_res_pens = WebScrapper.call_scrapper('bjs')
    assert len(bjs_res_pens) != 0

def test_call_scrapper_ebay():
    ebay_res_pens = WebScrapper.call_scrapper('ebay')
    assert len(ebay_res_pens) != 0

def test_call_scrapper_all_sites_socks():
    all_sites_pens = WebScrapper.call_scrapper('All Sites')
    assert len(all_sites_pens) != 0

def test_call_scrapper_costco_pens():
    costco_res_pens = WebScrapper.call_scrapper('costco')
    assert len(costco_res_pens) != 0

def test_call_scrapper_bestbuy_pens():
    bestbuy_res_pens = WebScrapper.call_scrapper('bestbuy')
    assert len(bestbuy_res_pens) != 0


