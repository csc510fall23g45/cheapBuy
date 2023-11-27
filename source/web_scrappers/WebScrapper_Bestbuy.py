"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

import sys
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup

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



class WebScrapper_Bestbuy:
    """
    Main class used to scrape results from Bestbuy

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
    get_url_bestbuy:
        Returns bestbuy URL
    scrap_bestbuy:
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
            results = self.scrap_bestbuy()
            # Condition to check whether results are available or not
            if len(results) == 0:
                print('Bestbuy_results empty')
                self.result = {}
            else:

                item = results[0]
                self.result['description'] = item.find('h4', class_='sku-title').text
                self.result['url'] = 'https://www.bestbuy.com' + item.find('a')['href']
                self.result['price'] = item.find(
                    "div", class_="priceView-hero-price priceView-customer-price").find('span',
                                                                                        class_='sr-only').text.strip().split(
                    "$")[1]
                self.result['site'] = 'bestbuy'

                '''
                for item in results:
                    print("Bestbuy:\n\n")
                    title = item.find("h4", class_="sku-header").get_text()
                    price = item.find("div", class_="priceView-hero-price priceView-customer-price").get_text()
                    print(title,"\n")
                    print(price,"\n")
                    print('↑Bestbuy↑')
                '''
        except Exception as e:
            print('Bestbuy_results exception', e)
            self.result = {}
        return self.result

    def get_url_bestbuy(self):
        """ 
        Returns bestbuy URL of search box
        """
        try:
            # Prepare URL for given description
            #template = 'https://www.bestbuy.com/site/searchpage.jsp?st={}&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys'
            template = 'https://www.bestbuy.com/site/searchpage.jsp?id=pcat17071&sp=%2Bcurrentprice%20skuidsaas&st={}'
            search_term = self.description.replace(' ', '+')
            template = template.format(search_term)
        except:
            template = ''
        return template

    def scrap_bestbuy(self):
        """ 
        Returns Scraped result
        """
        results = []
        try:
            # Call the function to get URL
            url = self.get_url_bestbuy()
            response = requests.get(scrapeops_url(url))
            html_response = response.text
            # Use BeautifulSoup to scrap the webpage
            soup = BeautifulSoup(html_response, 'html.parser')
            results = soup.find_all('li', {'class': 'sku-item'})
        except:
            results = []

        return results
