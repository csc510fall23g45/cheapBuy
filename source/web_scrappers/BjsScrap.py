import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode

SCRAPEOPS_API_KEY =   "b8d3d18d-bc64-45dc-b765-d24bb865fd3c"


def scrapeops_url(url):
    payload = {'api_key': SCRAPEOPS_API_KEY, 'url': url, 'country': 'us'}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url

# Replace this URL with the actual URL of the web page you want to scrape
url = 'https://www.bjs.com/search/fryer/q?template=clp'

# Send an HTTP GET request to the URL
response = requests.get(scrapeops_url(url))

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the product containers (div elements)

    product_containers=soup.find_all('div', class_='product')
    # Iterate through each product container and extract the information
    for container in product_containers:
        # Extract product price
        product_price = container.find('div', class_='price-new-plp').text
        if product_price == ' Member Only Price ':
            product_price=product_price
        else:
            product_price=product_price.strip().split('$')[1]
        # Extract product description
        product_description = container.find('div', class_='title-new-plp').text

        # Extract product URL
        product_url = 'https://www.bjs.com'+container.find('a')['href']

        '''
        print("Product Price:", product_price)
        print("Product Description:", product_description)
        print("Product URL:", product_url)
        print("\n")
        '''

else:
    print("Failed to retrieve the web page. Status code:", response.status_code)
