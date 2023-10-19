import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode

SCRAPEOPS_API_KEY =   "453fce39-0418-4083-8bd4-6f9e6376b8c7"


def scrapeops_url(url):
    payload = {'api_key': SCRAPEOPS_API_KEY, 'url': url, 'country': 'us'}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url

# Replace this URL with the actual URL of the web page you want to scrape
url = 'https://www.bestbuy.com/site/searchpage.jsp?id=pcat17071&sp=%2Bcurrentprice%20skuidsaas&st=chair'

# Send an HTTP GET request to the URL
response = requests.get(scrapeops_url(url))

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the product containers (div elements)
    product_containers = soup.find_all('li', class_='sku-item')

    # Iterate through each product container and extract the information
    for container in product_containers:
        # # Extract product name
        # product_name = container.find('span', class_='normal dark-gray mb0 mt1 lh-title f6 f5-l lh-copy').text

        # Extract product price
        product_price = container.find('div', class_='priceView-hero-price priceView-customer-price').find('span', class_='sr-only').text.strip().split("$")[1]

        # Extract product description
        product_description = container.find('h4', class_='sku-title').text

        # Extract product URL
        product_url = 'https://www.bestbuy.com' + container.find('a')['href']

        # Print or store the extracted information as needed
        # print("Product Name:", product_name)
        print("Product Price:", product_price)
        print("Product Description:", product_description)
        print("Product URL:", product_url)
        print("\n")

else:
    print("Failed to retrieve the web page. Status code:", response.status_code)
