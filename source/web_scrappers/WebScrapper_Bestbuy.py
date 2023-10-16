"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""


import sys

from bs4 import BeautifulSoup
from selenium import webdriver
from source.utils.url_shortener import shorten_url
import requests
from urllib.parse import urlencode
from webdriver_manager.chrome import ChromeDriverManager

# Set working directory path
sys.path.append('../')

SCRAPEOPS_API_KEY =   "b8d3d18d-bc64-45dc-b765-d24bb865fd3c"


def scrapeops_url(url):
    payload = {'api_key': SCRAPEOPS_API_KEY, 'url': url, 'country': 'us'}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url


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
        self.driver = self.get_driver()
        try:
            # Get results from scrapping function
            results = self.scrap_bestbuy()
            # Condition to check whether results are avialable or not
            if len(results) == 0:
                print('Bestbuy_results empty')
                self.result = {}
            else:
                """
                item=results[0]
                #Find teh atag containing our required item
                atag = item.h2.a
                #Extract description from the atag
                self.result['description'] = atag.text.strip()
                #Get the URL for the page and shorten it
                self.result['url'] = 'https://www.bestbuy.com'+atag.get('href')
                self.result['url'] = shorten_url(self.result['url'])
                #Find the span containging price of the item
                price_parent = item.find('span', 'a-price')
                #Find the price of the item
                self.result['price'] = price_parent.find('span', 'a-offscreen').text
                #Assign the site as bestbuy to result
                self.result['site'] = 'bestbuy'
                """

                item = results[0]
                self.result['description'] = item.find('h4', class_='sku-title').text
                self.result['url'] = 'https://www.bestbuy.com' + item.find('a')['href']
                self.result['price'] = item.find(
                    "div", class_="priceView-hero-price priceView-customer-price").find('span', class_='sr-only').text.strip().split("$")[1]
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

    def get_url_bestbuy(self):
        """ 
        Returns bestbuy URL of search box
        """
        try:
            # Prepare URL for given description
            template = 'https://www.bestbuy.com/site/searchpage.jsp?st={}&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys'
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
            # url = scrapeops_url(url)
            response = requests.get(scrapeops_url(url))
            html_response = response.text
            # Assign the URL to driver
            self.driver.get(url)
            # Use BeautifulSoup to scrap the webpage
            soup = BeautifulSoup(html_response, 'html.parser')
            results = soup.find_all('li', {'class': 'sku-item'})
        except:
            results = []

        return results
