import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode

SCRAPEOPS_API_KEY ="b8d3d18d-bc64-45dc-b765-d24bb865fd3c"


def scrapeops_url(url):
    payload = {'api_key': SCRAPEOPS_API_KEY, 'url': url, 'country': 'us'}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url

# Replace this URL with the actual URL of the web page you want to scrape
#url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=chair&_sacat=38204&LH_TitleDesc=0&_odkw=tablemaggi&_osacat=38204'
url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=chair&_sacat=0&_sop=15'
# Send an HTTP GET request to the URL
response = requests.get(scrapeops_url(url))

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the product containers (div elements)
    product_containers = soup.find_all(
        "li", {"class": "s-item s-item__pl-on-bottom"})

    # Iterate through each product container and extract the information
    for container in product_containers:
        # # Extract product name
        # product_name = container.find('span', class_='normal dark-gray mb0 mt1 lh-title f6 f5-l lh-copy').text

        # Extract product price
        product_price = container.find('div', class_='s-item__detail s-item__detail--primary').find('span', class_='s-item__price').text.strip().split('$')[1]

        # Extract product description
        product_description = container.find('div', class_="s-item__title").text.strip()

        # Extract product URL
        product_url = container.find('a')['href']

        # Print or store the extracted information as needed
        # print("Product Name:", product_name)
        print("Product Price:", product_price)
        print("Product Description:", product_description)
        print("Product URL:", product_url)
        print("\n")

else:
    print("Failed to retrieve the web page. Status code:", response.status_code)
