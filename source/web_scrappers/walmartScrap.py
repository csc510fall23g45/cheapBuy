import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode,unquote

SCRAPEOPS_API_KEY =   "453fce39-0418-4083-8bd4-6f9e6376b8c7"


def scrapeops_url(url):
    payload = {'api_key': SCRAPEOPS_API_KEY, 'url': url, 'country': 'us'}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return unquote(proxy_url)

def response_call():
    url = 'https://www.walmart.com/search?q=maggi&sort=price_low'

    # Send an HTTP GET request to the URL
    response = requests.get(scrapeops_url(url))

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page using Beautiful Soup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all the product containers (div elements)
        product_containers = soup.find_all('div', class_='mb0 ph1 pa0-xl bb b--near-white w-25')

        # Iterate through each product container and extract the information
        for container in product_containers:
            # Extract product price
            product_price = container.find('div', class_='flex flex-wrap justify-start items-center lh-title mb1').find('span', class_='w_iUH7').text.strip()

            # Extract product description
            product_description = container.find('span', class_='w_iUH7').text

            # Extract product URL
            product_url = 'https://www.walmart.com' + container.find('a')['href']

            print("Product Price:", product_price)
            print("Product Description:", product_description)
            print("Product URL:", product_url)
            print("\n")

    else:
        print("Failed to retrieve the web page. Status code:", response.status_code)

    return response.status_code

response_call()
