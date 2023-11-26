"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""
import sys
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup

from source.utils.url_shortener import shorten_url
import os
from dotenv import load_dotenv


# Set working directory path
sys.path.append('../')

# Load environment variables from .env
load_dotenv()

# Retrieve the API key from the environment variable
SCRAPEOPS_API_KEY = os.getenv('SCRAPEOPS_API_KEY')


def scrapeops_url(url):
    payload = {'api_key': SCRAPEOPS_API_KEY, 'url': url, 'country': 'us'}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url


class WebScrapper_Amazon:
    """
    Main class used to scrape results from Amazon

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
    get_url_amazon:
        Returns amazon URL
    scrap_amazon:
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
        try:
            # Get results from scrapping function
            results = self.scrap_amazon()
            # Condition to check whether results are available or not
            if len(results) == 0:
                print('Amazon_results empty')
                self.result = {}
            else:
                item = results[0]
                # Find teh atag containing our required item
                atag = item.h2.a
                # Extract description from the atag
                self.result['description'] = atag.text.strip()
                # Get the URL for the page and shorten it
                self.result['url'] = 'https://www.amazon.com' + atag.get('href')
                self.result['url'] = shorten_url(self.result['url'])  # short url is not applied currently
                # Find the span containing price of the item
                price_parent = item.find('span', 'a-price')
                # Find the price of the item
                self.result['price'] = price_parent.find(
                    'span', 'a-offscreen').text
                # Assign the site as amazon to result
                self.result['site'] = 'amazon'
        except Exception as e:
            print('Amazon_results exception', e)
            self.result = {}
        return self.result

    def get_url_amazon(self):
        """ 
        Returns amazon URL of search box
        """
        try:
            # Prepare URL for given description
            template = 'https://www.amazon.com' + '/s?k={}&ref=nb_sb_ss_ts-doa-p_3_5'
            search_term = self.description.replace(' ', '+')
            template = template.format(search_term)
        except:
            template = ''
        return template

    def scrap_amazon(self):
        """ 
        Returns Scraped result
        """
        results = []
        try:
            # Call the function to get URL
            url = self.get_url_amazon()
            # self.driver.get(url)
            response = requests.get(scrapeops_url(url))
            html_response = response.text
            # Use BeautifulSoup to scrap the webpage
            soup = BeautifulSoup(html_response, 'html.parser')
            results = soup.find_all(
                'div', {'data-component-type': 's-search-result'})
        except:
            results = []
        return results
