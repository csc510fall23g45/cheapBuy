"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

import sys

from bs4 import BeautifulSoup
from selenium import webdriver
from source.utils.url_shortener import shorten_url
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlencode
import requests
SCRAPEOPS_API_KEY =   "b8d3d18d-bc64-45dc-b765-d24bb865fd3c"


def scrapeops_url(url):
    payload = {'api_key': SCRAPEOPS_API_KEY, 'url': url, 'country': 'us'}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url

sys.path.append('../')


class WebScrapper_Costco:
    """
    Main class used to scrape results from Costco

    ...

    Attributes
    ----------
    description : str
        description of the product

    Methods
    -------
    run:
        Threaded method to execute subclasses
    get_driver:
        Returns Chrome Driver
    get_url_costco:
        Returns costco URL
    scrap_costco:
        Returns Scraped result
    """

    def __init__(self, description):
        """
        Parameters
        ----------
        description : str
            description of the product
        """
        if description:
            if len(description) < 5:
                self.description = description
            else:
                self.description = ' '.join(description.split()[:5])
        self.result = {}

    def run(self):
        """ 
        Returns final result
        """
        self.driver = self.get_driver()
        self.result = {}
        try:
            results = self.scrap_costco()
            if len(results) == 0:
                print('Costco_results empty')
                self.result = {}
            else:
                item = results[0]
                product_description = item.find('span', class_='description').text.strip()
                product_url = item.find('a')['href']
                product_price = item.find('div', class_='price').text.strip().split('$')[1]
                self.result['description'] = product_description
                self.result['url'] = product_url
                # self.result['url'] = shorten_url(self.result['url']) # short url is not applied currently
                # self.result['price'] = item.find(
                #     "div", {"class": "price"}).text.strip()
                self.result['price'] = product_price
                self.result['site'] = 'costco'
        except Exception as e:
            print('Costco_results exception', e)
            self.result = {}
        return self.result

    def get_driver(self):
        """ 
        Returns Chrome Driver
        """
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(
            options=options, executable_path=ChromeDriverManager().install())
        return driver

    def get_url_costco(self):
        """ 
        Returns costco URL of search box
        """
        template = "https://www.costco.com"+"/CatalogSearch?dept=All&keyword={}"
        search_term = self.description.replace(' ', '+')
        return template.format(search_term)

    def scrap_costco(self):
        """ 
        Returns Scraped result
        """
        url = self.get_url_costco()
        # self.driver.get(scrapeops_url(url))
        response = requests.get(scrapeops_url(url))
        html_response = response.text
        soup = BeautifulSoup(html_response, "html.parser")
        print(soup)
        results = soup.find_all('div', class_='product col-xs-12')
        print(results)
        return results
