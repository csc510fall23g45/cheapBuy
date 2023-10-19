# CheapBuy Phase 4 - Improved Version<br><br>
**Motivation:**<br><br>
CheapBuy Extension provides an easy solution look for prices of any product accross a number of your favorite 
given websites like Amazon, Walmart, Ebay, Bjs, Costco, etc., to help you analyze the product prices at once.
It takes a lot of time to search for the same product in different websites, and find the cheapest one, 
instead just adding this extension cheapBuy and it will automatically fetch you price of the same product from different websites and you can directly compare the prices from different websites through our extension. In sum, cheapBuy is a one stop solution to buy the cheapest product online.
<br><br>
**Features** - Price Comparison, Get alternative websites for the products, highlights cheapest product.
<br><br>
**Which users use this?**
Everyone who buys products online from famous online websites can use this to compare prices for any product they wish to buy.
<br><br>
**Steps for Execution:**
<br><br>
1. Clone the github repository at local machine. You will need git to be pre-installed in the system. Once the repository is cloned in your system, with the help of cd command ,
```
git clone https://github.com/anshulp2912/cheapBuy.git
cd cheapBuy
```
2. This project uses Python 3, so make sure that [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installation/) are preinstalled. All requirements of the project are listed in the ```requirements.txt``` file. Use pip to install all of the requirements.
```
pip install -r requirements.txt
```
3. Check out the demo video to know about the use of the website in the media files.
4. To locally run the streamlit website, we would recommend setting up an Anaconda Environment and running the command
```
streamlit run cheapBuy_user_interface1.py
```
**Code Functionalities:**
<br><br>
**web_scrappers**
1. **FetchDescription.py**
<br><br>
* function fetch_desc_amazon() : The function fetch_desc_amazon parses the link and gets the product description <br>
* function fetch_desc_walmart() : The function fetch_desc_walmart parses the link and gets the product description <br>
* function fetch_desc_ebay() : The function fetch_desc_ebay parses the link and gets the product description <br>
* function fetch_desc_costco() : The function fetch_desc_costco parses the link and gets the product description <br> 
* function fetch_desc_bestbuy() : The function fetch_desc_bestbuy parses the link and gets the product description <br> 
* function fetch_desc_bjs() : The function fetch_desc_bjs parses the link and gets the product description <br> 

<br><br><br>
2. **WebScrapper.py**<br> <br>
* function scrapper(product_description): Checks for each ecommerce platform the product_description(parameter of function) for details. Details include description, price and url. This function returns these details as a dictionary.
3. **WebScrapper_Amazon.py** <br><br>
* function run(): The function run is executed when the thread is started. It gets result from function scrap_amazon and extracts output in desired format from the result<br>
* function get_driver(): The function get_driver prepares and returns a Chrome driver using Selenium.<br>
* function get_url_amazon(search_item): This function returns the Amazon url of the product (search_term) given as an argument..<br>
* function scrap_amazon(): The function scrap_amazon performs web scraping using BeautifulSoup on the URL provided by function get_url_amazon.
<br><br> 
4. **WebScrapper_Bjs.py** <br><br>
* function get_url_bjs(search_term): This function returns the bjs url of the product (search_term) given as an argument.<br>
* function scrap_bjs(driver, search_term): Webpage of the product corresponding to search_term is retrieved using BeautifulSoup. <br>
* function run(search_term): Extracts the product description, price , URL and website name corresponding to search_term and returns it through a dictionary variable.
<br><br>
5. **WebScrapper_Costco.py**<br><br>
* function get_url_costco(search_term): This function returns the Costco url of the product (search_term) given as an argument.<br>
* function scrap_costco( search_term): Webpage of the product corresponding to search_term is retrieved using BeautifulSoup.<br>
* function run(search_term): Extracts the product description, price , URL and website name corresponding to search_term and returns it through a dictionary variable.
<br><br> 
6. **WebScrapper_Ebay.py** <br><br>
* function get_url_amazon(search_term): This function returns the Amazon url of the product (search_term) given as an argument.<br>
* function scrap_ebay( search_term): Webpage of the product corresponding to search_term is retrieved using BeautifulSoup.<br>
* function run(search_term): Extracts the product description, price, URL and website name corresponding to search_term and returns it through a dictionary variable.
<br><br>
7. **WebScrapper_Walmart.py** <br><br>
* function get_url_walmart(search_term):This function returns the Walmart url of the product (search_term) given as an argument.<br>
* function scrap_walmart search_term): Webpage of the product corresponding to search_term is retrieved using BeautifulSoup.<br>
* function run(search_term): Extracts the product description, price , URL and website name corresponding to search_term and returns it through a dictionary variable.
<br><br>

**Output:**<br>
The below screenshot shows the website created for cheapBuy. In the output, the cheapest option is highlighted in the website.<br>
<img src = "https://github.com/EZ7051/cheapBuy/blob/main/media/home1.jpeg"><br><br>
<img src = "https://github.com/EZ7051/cheapBuy/blob/main/media/results.jpeg"><br><br>
<img src = "https://github.com/EZ7051/cheapBuy/blob/main/media/allWebsiteslinks.jpeg"><br><br>
<img src = "https://github.com/EZ7051/cheapBuy/blob/main/media/singleWebsite.jpeg"><br><br>
