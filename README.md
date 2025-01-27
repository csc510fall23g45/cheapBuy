# <h1 align="center">CHEAPBUY</h1>

[![DOI](https://zenodo.org/badge/714713156.svg)](https://zenodo.org/doi/10.5281/zenodo.10211696)
![Github](https://img.shields.io/badge/language-python-red.svg)
[![codecov](https://codecov.io/gh/csc510fall23g45/cheapBuy/graph/badge.svg?token=Qntv9b30AU)](https://codecov.io/gh/csc510fall23g45/cheapBuy)
[![Running Code Coverage](https://github.com/csc510fall23g45/cheapBuy/actions/workflows/code_cov.yml/badge.svg)](https://github.com/csc510fall23g45/cheapBuy/actions/workflows/code_cov.yml)
[![Python Style Checker](https://github.com/csc510fall23g45/cheapBuy/actions/workflows/style_checker.yml/badge.svg)](https://github.com/csc510fall23g45/cheapBuy/actions/workflows/style_checker.yml)
[![Run Tests On Push](https://github.com/csc510fall23g45/cheapBuy/actions/workflows/unit_test.yml/badge.svg?branch=main)](https://github.com/csc510fall23g45/cheapBuy/actions/workflows/unit_test.yml)
[![Lint Python](https://github.com/csc510fall23g45/cheapBuy/actions/workflows/main.yml/badge.svg)](https://github.com/csc510fall23g45/cheapBuy/actions/workflows/main.yml)
<a href="https://github.com/csc510fall23g45/cheapBuy/blob/main/LICENSE" target="blank">
<img src="https://img.shields.io/github/license/csc510fall23g45/cheapBuy?style=flat-square" alt="cheapBuy license" /> </a>
<a href="https://github.com/csc510fall23g45/cheapBuy/issues" target="blank"><img src="https://img.shields.io/github/issues/csc510fall23g45/cheapBuy?style=flat-square" alt="cheapBuy issues"/></a>
<a href="https://github.com/csc510fall23g45/cheapBuy/issues?q=is%3Aissue+is%3Aclosed" target="blank">
<img src="https://img.shields.io/github/issues-closed/csc510fall23g45/cheapBuy" alt="cheapBuy issues closed"/></a>
<a href="https://github.com/csc510fall23g45/cheapBuy/pulls" target="blank">
<img src="https://img.shields.io/github/issues-pr/csc510fall23g45/cheapBuy?style=flat-square" alt="cheapBuy pull-requests"/></a>
<a href="https://github.com/csc510fall23g45/cheapBuy/graphs/commit-activity" alt="commit activity">
<img src="https://img.shields.io/github/commit-activity/w/csc510fall23g45/cheapBuy" /></a> 
<a href="https://img.shields.io/github/repo-size/csc510fall23g45/cheapBuy" alt="repo size">
<img src="https://img.shields.io/github/repo-size/csc510fall23g45/cheapBuy" /></a>

<p align="center">
    <a href="https://github.com/csc510fall23g45/cheapBuy/issues/new/choose">Report Bug</a>
    ·
    <a href="https://github.com/csc510fall23g45/cheapBuy/issues/new/choose">Request Feature</a>
</p>

## Table of Contents
- [Introduction](#Introduction)
- [Features](#Features)
- [Installation Steps](#ExecutionSteps)
- [Plan of Action](#PlanofAction)
  - [Phase 1](#phase-1-)
  - [Phase 2](#phase-2--)
  - [Phase 3](#phase-3--)
  - [Phase 4](#phase-4--)
  - [***(new)Phase 5***](#phase-5--)
  - [Future phase](#future-phase--)
- [Video](#Video)
- [License](#License)
- [Contributing](#Contributing)
- [Team Members](#TeamMember)
- [Acknowledgements](#Acknowledgement)

## 📖 Introduction <a name="Introduction"></a>

**CheapBuy** is a user-friendly website that simplifies online shopping with an improved interface. It offers convenient price comparisons for the same product across various websites, including popular ones like Amazon, Walmart, eBay, BJ's, Costco, and more. With user accounts, personalized wishlists, and the ability to filter and select multiple websites at once, cheapBuy provides a seamless shopping experience. This streamlined process not only saves you time and money but also offers the convenience of personalized wishlists and account features, making cheapBuy your go-to solution for finding the best deals online.

<h1 align="center">
 <img src="https://github.com/csc510fall23g45/cheapBuy/blob/Project3/media/cheapBuyGif.gif" />
</h1>


# :dizzy: Features <a name="Features"></a>
### User Accounts
<p align="center"><img width="700" src="media/cheapbuylogin.gif"></p>

### Enhanced UI
<p align="center"><img width="700" src="media/cheapbuysearch.gif"></p>

### Personal wishlists
<p align="center"><img width="700" src="media/cheapbuywishlist.gif"></p>

### Filter option for searching
<p align="center"><img width="700" src="media/cheapbuychoosewebsite.gif"></p>

## 🛠️ Steps for Execution <a name="ExecutionSteps"></a>

1. **Clone the GitHub Repository:**
   - Clone the GitHub repository to your preferred location on your system. Ensure that Git is preinstalled.
     ```bash
     git clone https://github.com/csc510fall23g45/cheapBuy.git
     cd cheapBuy
     ```
2. **Install Python and Pip:**
   - This project uses Python 3. Make sure Python and Pip are preinstalled on your system. If not, download and install them:
     - [Python](https://www.python.org/downloads/)
     - [Pip](https://pip.pypa.io/en/stable/installation/)

3. **Install Project Dependencies:**
   - Install the project dependencies listed in the `requirements.txt` file using the following command:
     ```bash
     pip install -r requirements.txt
     ```

4. **Generate ScrapeOps API Key:**
   - Visit [ScrapeOps](https://scrapeops.io/) website, sign in to your account, and navigate to the API Keys section. Create a new API key in the      ScrapeOps dashboard nd verify your email address to start scraping using the api-key.
  
# Running

**Set Environment Variable for Windows PowerShell:**
```bash
$Env:SCRAPEOPS_API_KEY = "your_api_key_here"
```

**Set Environment Variable for macOS and Linux:**
```bash
export SCRAPEOPS_API_KEY="your_api_key_here"
```

**Set Environment Variable for Windows Command Prompt:**
```bash
set SCRAPEOPS_API_KEY=your_api_key_here
```
   Replace `"your_api_key_here"` with the actual API key you obtained from ScrapeOps. This key will be used for making requests to the ScrapeOps API within the project.

**Run Flask Application:**
- Execute the following command to run the Flask application:
```bash
python app.py
```
- Navigate to the provided link (usually `http://127.0.0.1:5000/`) in your web browser to use cheapBuy.

## 📅 Plan of Action <a name="PlanofAction"></a>
### PHASE-1✅ <a name="Phase1"></a>
1. Fetching descirption of the user's current tab for ebay.
2. Fetching descirption of the user's current tab for Walmart.
3. Fetching descirption of the user's current tab for amazon.
4. Fetching descirption of the user's current tab for Bjs.
5. Fetching descirption of the user's current tab for Costco.
6. Web Scrapping various product details from Amazon.
7. Web Scrapping various product details from Ebay.
8. Exception handling of web scrapping.
9. Server API for web scrapping.
10. Deploying server on AWS.
11. Build an extension for this price comparison.
12. Extract knowledge like prices, sites, URL, comparison, description from scrapped data.
13. Show all the scrapped data and the knowledge gained on the extension page.

### PHASE-2 ✅ <a name="Phase2"></a>
1. Develop a website instead of extension.
2. Improvement of extension UI.
3. Highlight the cheapest option available.
4. Code restructuring.
5. Improve accuracy of the product. Example : If user's current tab is having Television of a particular brand and there is a better option available at a cheaper or comparable rate than provide alternative product accordingly.
6. Web Scrapping various product details from Walmart.
7. Web Scrapping various product details from Costco.
8. Web Scrapping various product details from BJs.
9. Improve code execution speed using multithreading.

### PHASE-3 ✅ <a name="Phase3"></a>
1. Fetching descirption of the user's current tab for Bestbuy.
2. Fetching descirption of the user's current tab for Trader Joes.
3. Fetching descirption of the user's current tab for Kroger.
4. Web Scrapping various product details from Bestbuy.
5. Web Scrapping various product details from Trader Joes.
6. Web Scrapping various product details from Kroger.
7. Improve code execution speed using multiprocessing.
8. Improve website UI.
9. Add a sidebar.
10. Users can choose the selected website and price range.
11. Improve the accuracy of searching products.
12. Link buttons for all websites.

### PHASE-4 ✅ <a name="Phase4"></a>
1. Showing the cheapest product from every website (previously they were giving the first product and not the least cost one).
2. Remove the product link and use the product name or description to search.
3. Fix proxy issues in web scraping of all websites.
4. Increase the speed of execution of single site selection.
5. Remove the Chrome Driver from web-scrapers to decrease the latency.
6. Optimise the results fetching time.
7. Remove price range as we are looking for the cheapest product across a website or on a website.
8. Enhance the user interface, and keep only relevant images and content.
9. Reduce the time complexity and latency for the product search by removing inner loops.

### PHASE-5 ✅ <a name="Phase5"></a>
1. Implemented a new functionality that allows users to effortlessly set up new accounts.
2. Implemented a new wishlist feature that empowers users to personalize and seamlessly save their desired products.
3. Updated the front-end framework to Flask to improve the page hosting.
4. Enhanced the user interface.
5. Added option for users to select one or more websites for selected searching.
6. Improved Test case code coverage from 27% to 67%.
7. Secured the ScrapeOps API key using environment variables.
8. Fixed web scraper issues for BJs, Costco and eBay.

### FUTURE PHASE ⌛ <a name="FuturePhase"></a>
1. Creating ordering and payment functionality for customers to directly order from Website.
2. Email notification of the available coupon to the user.
3. Adding more filter options.
4. Creating multiple wishlists.
5. Decrease the load time.
6. Storing the data more securly.
7. Add more websites for web scrapping like Target, Kroger, and Traderjoes.

🌟 You are all set! 🌟

## Video <a name="Video"></a>
[CSC 510 - Project 3 - Project Demo](https://youtu.be/70gB6JjtWYc)

## 📝 License <a name="License"></a>
This project is licensed under the terms of the MIT license. Please check [License](https://github.com/csc510fall23g45/cheapBuy/blob/Project3/LICENSE) for more details.

## 🍰 Contributing <a name="Contributing"></a>
Please contribute using [GitHub Flow](https://guides.github.com/introduction/flow). Create a branch, add commits, and [open a pull request](https://github.com/EZ7051/cheapBuy/compare/main...csc510fall23g45:cheapBuy:Project3).

Please read [`CONTRIBUTING`](CONTRIBUTING.md) for details on our [`CODE OF CONDUCT`](CODE_OF_CONDUCT.md), and the process for submitting pull requests to us.

## Project 3 Rubric
Click [here](https://github.com/csc510fall23g45/cheapBuy/blob/Project3/Proj3/README.md) for project 3 rubric

## 👥 Team Members <a name="TeamMember"></a>
<table>
  <tr>
    <td align="center"><a href="https://github.com/sairajzero"><img src="https://avatars.githubusercontent.com/u/39055732?v=4" width="75px;" alt=""/><br /><sub><b>Sai Raj</b></sub></a></td>
    <td align="center"><a href="https://github.com/NityaNagaSai"><img src="https://avatars.githubusercontent.com/u/73474889?v=4" width="75px;" alt=""/><br /><sub><b>Nitya</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/anish7-anish"><img src="https://avatars.githubusercontent.com/u/79855191?v=4" width="75px;" alt=""/><br /><sub><b>Anish</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/mahathii"><img src="https://avatars.githubusercontent.com/u/95462566?v=4" width="75px;" alt=""/><br /><sub><b>Mahathi</b></sub></a><br /></td>
  </tr>
</table>

| Name                   | Unity ID                           |
|------------------------|------------------------------------|
| Sai Raj Thirumalai     | sthirum4                           |
| Nitya Naga Sai Atluri  | natluri                            |
| Anish Rao Toorpu       | atoorpu                            |
| Mahathi Kolishetty     | mkolish                            |

## More documentation
- [function_description](https://github.com/csc510fall23g45/cheapBuy/blob/Project3/Proj3/function_description.md)

## Chat Channel

<code><a href="https://discord.gg/MxDrcdSs4p" target="_blank"><img height="100" width="250" src="https://user-images.githubusercontent.com/42767118/135394825-26dee6db-7a64-4e3f-902a-1e35abd4cf0c.png"></a></code>

## :email: Support
To Subscribe and for any help, please reach out to us at: sefall2023project45@gmail.com

## 🙏 Acknowledgements <a name="Acknowledgement"></a>
We would like to thank Professor Dr Timothy Menzies for helping us understand the process of building a good Software Engineering project. We would also like to thank the teaching assistants San Gilson, Andre Lustosa, Xueqi (Sherry) Yang, Yasitha Rajapaksha, and Rahul Yedida for their support throughout the project.
We would also like to extend our gratitude to the previous group : [[https://github.com/EZ7051/cheapBuy](https://github.com/EZ7051/cheapBuy)]
- [https://shields.io/](https://shields.io/)
- [https://www.powtoon.com/](https://www.powtoon.com/)
<br>
