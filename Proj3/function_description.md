# Code Description

## Web Scrapers

### 1. FetchDescription.py

#### `fetch_desc_amazon(link: str) -> str`
Parses the Amazon link and retrieves the product description.

#### `fetch_desc_walmart(link: str) -> str`
Parses the Walmart link and retrieves the product description.

#### `fetch_desc_ebay(link: str) -> str`
Parses the eBay link and retrieves the product description.

#### `fetch_desc_costco(link: str) -> str`
Parses the Costco link and retrieves the product description.

#### `fetch_desc_bestbuy(link: str) -> str`
Parses the Best Buy link and retrieves the product description.

#### `fetch_desc_bjs(link: str) -> str`
Parses the BJ's link and retrieves the product description.

### 2. WebScrapper.py

#### `scrapper(product_description: str) -> dict`
Checks each ecommerce platform for product details. Returns a dictionary with description, price, and URL.

### 3. web_scrapper_amazon.py

#### `get_url_amazon(search_term: str) -> str`
Returns the Amazon URL for the given search term.

#### `scrap_amazon(driver, search_term: str) -> dict`
Retrieves the product webpage using BeautifulSoup, extracts description, price, URL, and website name.

#### `run(search_term: str) -> dict`
Executes the scraping process and returns details through a dictionary.

### 4. web_scrapper_bjs.py

#### `get_url_bjs(search_term: str) -> str`
Returns the BJ's URL for the given search term.

#### `scrap_bjs(driver, search_term: str) -> dict`
Retrieves the product webpage using BeautifulSoup, extracts description, price, URL, and website name.

#### `run(search_term: str) -> dict`
Executes the scraping process and returns details through a dictionary.

### 5. web_scrapper_ebay.py

#### `get_url_ebay(search_term: str) -> str`
Returns the eBay URL for the given search term.

#### `scrap_ebay(search_term: str) -> dict`
Retrieves the product webpage using BeautifulSoup, extracts description, price, URL, and website name.

#### `run(search_term: str) -> dict`
Executes the scraping process and returns details through a dictionary.

### 6. web_scrapper_walmart.py

#### `get_url_walmart(search_term: str) -> str`
Returns the Walmart URL for the given search term.

#### `scrap_walmart(search_term: str) -> dict`
Retrieves the product webpage using BeautifulSoup, extracts description, price, URL, and website name.

#### `run(search_term: str) -> dict`
Executes the scraping process and returns details through a dictionary.

### 7. web_scrapper_costco.py

#### `get_url_costco(search_term: str) -> str`
Returns the Costco URL for the given search term.

#### `scrap_costco(search_term: str) -> dict`
Retrieves the product webpage using BeautifulSoup, extracts description, price, URL, and website name.

#### `run(search_term: str) -> dict`
Executes the scraping process and returns details through a dictionary.

### 8. web_scrapper_bestbuy.py

#### `get_url_bestbuy(search_term: str) -> str`
Returns the Best Buy URL for the given search term.

#### `scrap_bestbuy(search_term: str) -> dict`
Retrieves the product webpage using BeautifulSoup, extracts description, price, URL, and website name.

#### `run(search_term: str) -> dict`
Executes the scraping process and returns details through a dictionary.

### 9. database_functions.py

#### `execute_query(query, values = []) -> Tuple[List[Tuple], Optional[sqlite3.Error]]`
Executes a SQLite query with optional parameters and returns the result along with any potential errors.

#### `initiate_database() -> None`
Initializes the SQLite database by creating tables for users and wishlist if they do not exist.

#### `create_user(username, password) -> Union[bool, None]`
Inserts a new user with a username and password into the database, returns True if successful, False if the username already exists, and None on other errors.

#### `view_users() -> Optional[List[Tuple]]`
Retrieves and returns all users from the database, or None if an error occurs.

#### `get_password(username) -> Union[str, bool, None]`
Retrieves the password for a given username, returns the password as a string, False if the user does not exist, or None on errors.

#### `add_wishlist_item(username, item_name, price, website, link) -> Union[bool, None]`
Adds an item to the wishlist with details like item name, price, website, and link; returns True if successful, False if the user does not exist, and None on other errors.

#### `delete_wishlist_item(username, id) -> Union[bool, None]`
Deletes an item from the wishlist based on the item's ID and the username; returns True if successful, and None on errors.

#### `view_wishlist_items(username) -> Optional[List[Dict[str, Union[int, str, float]]]]`
Retrieves and returns wishlist items for a given username in a structured dictionary format, or None if an error occurs.

# Flask Application Code Description

## app.py

### `index() -> str`
Renders the landing page or login page based on the user session.

### `search() -> str`
Handles the search functionality, calls the web scraper, and renders search results.

### `wishlist() -> str`
Renders the wishlist page with items retrieved from the database for the logged-in user.

### `add_wishlist_item() -> str`
Handles adding items to the wishlist and updates the database accordingly.

### `rm_wishlist_item() -> str`
Handles removing items from the wishlist and updates the database accordingly.

### `create_account() -> str`
Handles user account creation, logs in the user if successful, and provides error feedback if needed.

### `login() -> str`
Handles user login, authenticates the user, and redirects to the landing page or provides error feedback.

### `logout() -> str`
Logs out the current user and redirects to the landing page.
