"""
Copyright (c) 2023 Group45
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""


import sys
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup

import pyshorteners


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


# Set working directory path
sys.path.append('../')


class WebScrapper_Ebay:
    """
    Main class used to scrape results from Ebay

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
    get_url_ebay:
        Returns ebay URL
    scrap_ebay:
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

    def shorten_url(long_url):
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(long_url)
        return short_url

    def run(self):
        """ 
        Returns final result
        """
        self.result = {}
        try:
            # Get results from scrapping function
            results = self.scrap_ebay()
            # Condition to check whether results are avialable or not
            if len(results) == 0:
                self.result = {}
                print('Ebay_results empty')
            else:
                item = results[1]
                # Extract product price
                product_price = item.find('div', class_='s-item__detail s-item__detail--primary').find(
                    'span', class_='s-item__price').text.strip().split('$')[1]
                # Extract product description
                product_description = item.find(
                    'div', class_="s-item__title").text.strip()
                # Extract product URL
                product_url = item.find('a')['href']
                self.result['description'] = product_description
                # Get the URL for the page and shorten item
                self.result['url'] = product_url
                print(product_url)
                # self.result['url']= self.shorten_url(self.result['url'])
                print(self.result['url'])
                # Find the price of the item
                self.result['price'] = product_price
                # Assign the site as ebay to result
                self.result['site'] = 'ebay'
        except Exception as e:
            print('Ebay_results exception', e)
            self.result = {}
        return self.result

    def get_url_ebay(self):
        """ 
        Returns ebay URL of search box
        """
        try:
            # Prepare URL for given description
            # template = "https://www.ebay.com" + \
            #           "/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={}"
            template = "https://www.ebay.com/sch/i.html?_from=R40&_nkw={}&_sacat=0&_sop=15"
            template = template.format(self.description)
        except:
            template = ''
        return template

    def scrap_ebay(self):
        """ 
        Returns Scraped result
        """
        results = []
        try:
            # Call the function to get URL
            url = self.get_url_ebay()
            response = requests.get(scrapeops_url(url))
            html_response = response.text
            # Use BeautifulSoup to scrap the webpage
            soup = BeautifulSoup(html_response, 'html.parser')
            results = soup.find_all(
                "li", {"class": "s-item s-item__pl-on-bottom"})
        except:
            results = []
        return results
