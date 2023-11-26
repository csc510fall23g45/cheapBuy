"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

import sys
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup

# Set working directory path
sys.path.append('../')

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
        self.result = {}
        try:
            # Get results from scrapping function
            results = self.scrap_walmart()
            # Condition to check whether results are available or not
            if len(results) == 0:
                self.result = {}
                print('Walmart_results empty')
            else:
                item = results[0]
                # Extract product price
                product_price = \
                item.find('div', class_='flex flex-wrap justify-start items-center lh-title mb1').find('span',
                                                                                                       class_='w_iUH7') \
                    .text.strip().split(" ")[2].split("$")[1]

                # Extract product description
                product_description = item.find('span', class_='w_iUH7').text

                # Extract product URL
                product_url = 'https://www.walmart.com' + item.find('a')['href']
                # Extract description from the atag
                self.result['description'] = product_description
                # Get the URL for the page and shorten it
                self.result['url'] = product_url
                # Find the price of the item
                self.result['price'] = product_price
                # Assign the site as walmart to result
                self.result['site'] = 'walmart'
        except Exception as e:
            print('Walmart_results exception', e)
            self.result = {}
        return self.result

    def get_url_walmart(self):
        """ 
        Returns walmart URL of search box
        """
        # Prepare URL for given description
        template = 'https://www.walmart.com/search?q={}&sort=price_low'
        search_term = self.description.replace(' ', '+')
        return template.format(search_term)

    def scrap_walmart(self):
        """ 
        Returns Scraped result
        """
        # Call the function to get URL
        url = self.get_url_walmart()
        response = requests.get(scrapeops_url(url))
        html_response = response.text
        # Use BeautifulSoup to scrap the webpage
        soup = BeautifulSoup(html_response, 'html.parser')
        results = soup.find_all('div', class_='mb0 ph1 pa0-xl bb b--near-white w-25')
        return results
