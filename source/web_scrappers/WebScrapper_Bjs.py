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

SCRAPEOPS_API_KEY =   "453fce39-0418-4083-8bd4-6f9e6376b8c7"


def scrapeops_url(url):
    payload = {'api_key': SCRAPEOPS_API_KEY, 'url': url, 'country': 'us'}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url
# Set working directory path

sys.path.append('../')


class WebScrapper_Bjs:
    """
    Main class used to scrape results from BJs

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
    get_url_bjs:
        Returns bjs URL
    scrap_bjs:
        Returns Scraped result
    """

    def __init__(self, description):
        """
        Parameters
        ----------
        description : str
            description of the product
        """
        # Initialize class variables
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
        try:
            # Get results from scrapping function
            results = self.scrap_bjs()
            self.result = {}
            # Condition to check whether results are avialable or not
            if len(results) == 0:
                print('BJs_results empty')
                self.result = {}
            else:
                item = results[0]
                # Find teh atag containing our required item
                # atag = item.find(
                #     "a", {"class": "product-link mt-xl-3 mt-xs-3 mt-md-0 mt-3"})
                # # Extract description from the atag
                # self.result['description'] = (
                #     atag.find("h2", {"class": "product-title no-select d-none"})).text
                # # Get the URL for the page and shorten item
                # self.result['url'] = "www.bjs.com" + str(atag.get('href'))
                # self.result['url'] = shorten_url(self.result['url']) # short url is not applied currently
                # # Find the price of the item
                # self.result['price'] = item.find(
                #     "div", {"class": "display-price"}).find('span', {'class': 'price'}).text
                # # Assign the site as bjs to result
                product_description = item.find('div', class_='title-new-plp').text
                product_url = 'https://www.bjs.com'+item.find('a')['href']
                product_price = item.find('div', class_='price-new-plp').text
                # if product_price == ' Member Only Price ':
                #     product_price=product_price
                # else:
                #     product_price=product_price.strip().split('$')[1]
                self.result['description'] = product_description
                self.result['url'] = product_url
                self.result['price'] = product_price
                self.result['site'] = 'bjs'
        except Exception as e:
            print('BJs_results exception', e)
            self.result = {}
        return self.result

    def get_driver(self):
        """ 
        Returns Chrome Driver
        """
        # Prepare driver for scrapping
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(
            options=options, executable_path=ChromeDriverManager().install())
        return driver

    def get_url_bjs(self):
        """ 
        Returns bjs URL of search box
        """
        # Prepare URL for given description
        template = "https://www.bjs.com"+"/search/{}/q?template=clp"
        search_term = self.description.replace(' ', '+')
        return template.format(search_term)

    def scrap_bjs(self):
        """ 
        Returns Scraped result
        """
        # Call the function to get URL
        url = self.get_url_bjs()
        self.driver.get(url)
        # Use BeautifulSoup to scrap the webpage
        # soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        # results = soup.find_all('div', {'class': 'products-list'})
        response = requests.get(scrapeops_url(url))
        html_response = response.text
        soup = BeautifulSoup(html_response, "html.parser")
        # with open('costco.html', 'w') as file:
        #     file.write(soup.text)
        results = soup.find_all('div', class_='product')
        return results
