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
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from source.utils.url_shortener import shorten_url

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

class WebScrapper_TraderJoes:

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

    # def run(self):
    #     """ 
    #     Returns final result
    #     """
    #     self.driver = self.get_driver()
    #     try:
    #         # Get results from scrapping function
    #         results = self.scrap_traderjoes()
    #         # Condition to check whether results are avialable or not
    #         if len(results) == 0:
    #             print('TraderJoes_results empty')
    #             self.result = {}
    #         else:
    #             item = results[0]
    #             # Find teh atag containing our required item
    #             atag = item.h3.a
    #             # Extract description from the atag
    #             #self.result['description'] = atag.text.strip()
    #             self.result['description'] = item.find('h1', class_='ProductDetails_main__title__14Cnm').text.strip()
    #             print("description")
    #             print(self.result['description'])
    #             # Get the URL for the page and shorten it
    #             self.result['url'] = 'https://www.traderjoes.com/home'+atag.get('href')
    #             self.result['url'] = shorten_url(self.result['url']) # short url is not applied currently
    #             # Find the span containging price of the item
    #             #price_parent = item.find('span', 'a-price')
    #             # Find the price of the item
    #             self.result['price'] = item.find(
    #                 'span', 'ProductPrice_productPrice__price__3-50j').text
    #             # Assign the site as traderjoes to result
    #             self.result['site'] = 'traderjoes'
    #     except Exception as e:
    #         print('TraderJoes_results exception', e)
    #         self.result = {}
    #     return self.result
    def run(self):
        self.driver = self.get_driver()
        try:
            # Get results from scraping function
            results = self.scrap_traderjoes()
            # Condition to check whether results are available or not
            if len(results) == 0:
                print('TraderJoes_results empty')
                self.result = {}
            else:
                item = results[0]
                # Find the a-tag containing our required item
                atag = item.h3.a

                # Wait for the product details page to load
                product_details_url = 'https://www.traderjoes.com/home' + atag.get('href')
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//h1[@class='ProductDetails_main__title__14Cnm']"))
                )

                # Extract description from the product details page
                self.driver.get(product_details_url)
                product_details_soup = BeautifulSoup(self.driver.page_source, 'html.parser')
                self.result['description'] = product_details_soup.find('h1', class_='ProductDetails_main__title__14Cnm').text.strip()

                # Get the URL for the page and shorten it
                self.result['url'] = shorten_url(product_details_url)

                # Find the span containing the price of the item
                self.result['price'] = item.find('span', 'ProductPrice_productPrice__price__3-50j').text

                # Assign the site as traderjoes to the result
                self.result['site'] = 'traderjoes'

        except Exception as e:
            print('TraderJoes_results exception', e)
            self.result = {}
        finally:
            self.driver.quit()  # Make sure to close the driver after scraping
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

    def get_url_traderjoes(self):
        """ 
        Returns amazon URL of search box
        """
        try:
            # Prepare URL for given description
            template = 'https://www.traderjoes.com/home'+'/search?q={}&global=yes'
            
            search_term = self.description.replace(' ', '+')
            template = template.format(search_term)
        except:
            template = ''
        return template

    def scrap_traderjoes(self):
        """ 
        Returns Scraped result
        """
        results = []
        try:
            # Call the function to get URL
            url = self.get_url_traderjoes()
            response = requests.get(scrapeops_url(url))
            html_response = response.text
            self.driver.get(url)
            # Use BeautifulSoup to scrap the webpage
            soup = BeautifulSoup(html_response, 'html.parser')
            results = soup.find_all('article', class_='SearchResultCard_searchResultCard__3V-_h')
        except:
            results = []
        return results
