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
import json

# Set working directory path
sys.path.append('../')


SCRAPEOPS_API_KEY =   "b8d3d18d-bc64-45dc-b765-d24bb865fd3c"


def scrapeops_url(url):
    payload = {'api_key': SCRAPEOPS_API_KEY, 'url': url, 'country': 'us'}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url


class WebScrapper_Walmart:
    """
    Main class used to scrape results from Walmart

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
    get_url_walmart:
        Returns walmart URL
    scrap_walmart:
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
        self.description = description
        self.result = {}

    def run(self):
        """ 
        Returns final result
        """
        # print("New Codeee")
        self.driver = self.get_driver()
        self.result = {}
        try:
            # Get results from scrapping function
            results = self.scrap_walmart()
            # Condition to check whether results are avialable or not
            if len(results) == 0:
                self.result = {}
                print('Walmart_results empty')
            else:
                item = results[0]
                # Extract product price
                product_price = item.find('div', class_='flex flex-wrap justify-start items-center lh-title mb1').find('span', class_='w_iUH7')\
                                .text.strip().split(" ")[2].split("$")[1]

                # Extract product description
                product_description = item.find('span', class_='w_iUH7').text

                # Extract product URL
                product_url = 'https://www.walmart.com' + item.find('a')['href']
                # Find teh atag containing our required item
                atag = item.find("a", {"class": "absolute w-100 h-100 z-1"})
                # Extract description from the atag
                self.result['description'] = product_description
                # Get the URL for the page and shorten it
                # self.result['url'] = shorten_url(self.result['url']) # short url is not applied currently
                self.result['url'] = product_url
                # Find the parent div containging price of the item
                parent_price = item.find(
                    "div", {"class": "flex flex-wrap justify-start items-center lh-title mb2 mb1-m"})
                # Find the price of the item
                self.result['price'] = product_price
                # Assign the site as walmart to result
                self.result['site'] = 'walmart'
        except Exception as e:
            print('Walmart_results exception', e)
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

    def get_url_walmart(self):
        """ 
        Returns walmart URL of search box
        """
        # Prepare URL for given description
        template = 'https://www.walmart.com/search?q={}'
        search_term = self.description.replace(' ', '+')
        return template.format(search_term)

    def scrap_walmart(self):
        """ 
        Returns Scraped result
        """
        # Call the function to get URL
        url = self.get_url_walmart()
        # url = scrapeops_url(url)
        response = requests.get(scrapeops_url(url))
        html_response = response.text
        # Assign the URL to driver
        self.driver.get(url)
        # Use BeautifulSoup to scrap the webpage
        soup = BeautifulSoup(html_response, 'html.parser')
        # print("*********")
        # print(soup)
        results = soup.find_all('div', class_='mb0 ph1 pa0-xl bb b--near-white w-25')
        # results = soup.find_all(
        #     'div', {'class': 'h-100 pb1-xl pr4-xl pv1 ph1'})
        # print(results)
        return results
