"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

import sys
from urllib.parse import urlencode
import requests
from bs4 import BeautifulSoup

SCRAPEOPS_API_KEY = "453fce39-0418-4083-8bd4-6f9e6376b8c7"


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
        # Initialize class variables
        self.description = description
        self.result = {}

    def run(self):
        """ 
        Returns final result
        """
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
                self.result['price'] = product_price
                self.result['site'] = 'costco'
        except Exception as e:
            print('Costco_results exception', e)
            self.result = {}
        return self.result

    def get_url_costco(self):
        """ 
        Returns costco URL of search box
        """
        template = "https://www.costco.com" + "/CatalogSearch?dept=All&keyword={}" #+"&dept=All&sortBy=item_location_pricing_salePrice+asc"
        search_term = self.description.replace(' ', '+')
        return template.format(search_term)

    def scrap_costco(self) :
        """ 
        Returns Scraped result
        """
        url = self.get_url_costco()
        response = requests.get(scrapeops_url(url))
        html_response = response.text
        soup = BeautifulSoup(html_response, "html.parser")
        # with open('costco.html', 'w') as file:
        #     file.write(soup.text)
        results = soup.find_all('div', class_='product')
        return results
