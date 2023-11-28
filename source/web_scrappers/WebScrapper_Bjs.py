"""
Copyright (c) 2023 Group45
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""


import sys

from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlencode
import requests

import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Retrieve the API key from the environment variable
SCRAPEOPS_API_KEY = os.getenv('SCRAPEOPS_API_KEY')


def scrapeops_url(url):
    payload = {'api_key': SCRAPEOPS_API_KEY, 'url': url, 'country': 'us'}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url


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

                product_description = item.find(
                    'span', {'auto-data': 'product_name'}).text
                product_url = 'https://www.bjs.com' + \
                    item.find('a', class_="product-link")['href']
                product_price = item.find('div', class_='normal-price').text
                print(product_url)
                print(product_price)
                print(product_description)
                if product_description:
                    self.result['description'] = product_description.text
                if product_url:
                    self.result['url'] = product_url
                if product_price:
                    self.result['price'] = product_price.text
                # self.result['description'] = product_description
                # self.result['url'] = product_url
                # self.result['price'] = product_price
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
        response = requests.get(scrapeops_url(url))
        html_response = response.text
        soup = BeautifulSoup(html_response, "html.parser")
        results = soup.find_all('div', class_='product')
        return results
