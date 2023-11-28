"""
Copyright (c) 2023 Group45
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode, unquote


import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


SCRAPEOPS_API_KEY = os.getenv('SCRAPEOPS_API_KEY')


def scrapeops_url(url):
    payload = {'api_key': SCRAPEOPS_API_KEY, 'url': url, 'country': 'us'}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return unquote(proxy_url)


def response_call():
    # Replace this URL with the actual URL of the web page you want to scrape
    url = 'https://www.traderjoes.com/home/search?q=potato'

    # Send an HTTP GET request to the URL
    response = requests.get(scrapeops_url(url))

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page using Beautiful Soup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the product containers (div elements)
        product_containers = soup.find_all(
            'article', class_='SearchResultCard_searchResultCard__3V-_h')

        # Iterate through each product container and extract the information
        for container in product_containers:
            # Extract product price
            product_price = container.find(
                'span', class_='ProductPrice_productPrice__price__3-50j').text.strip()

            # Extract product description
            product_description = container.find(
                'a', class_='Link_link__1AZfr SearchResultCard_searchResultCard__titleLink__2nz6x').text

            # Extract product URL
            product_url = 'https://www.traderjoes.com' + \
                container.find(
                    'a', class_='Link_link__1AZfr SearchResultCard_searchResultCard__titleLink__2nz6x')['href']

            print("Product Price:", product_price)
            print("Product Description:", product_description)
            print("Product URL:", product_url)
            print("\n")

    else:
        print("Failed to retrieve the web page. Status code:", response.status_code)

    return response.status_code


response_call()
