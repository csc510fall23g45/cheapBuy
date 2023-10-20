[![cheapBuy Project 3 DEMO](https://github.com/freakleesin/cheapBuy/blob/main/media/cheapbuy.png)](https://www.youtube.com/watch?v=-P3LxID5QzA)
## ⬆️ Click on the icon above to see the new video



[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10020346.svg)](https://doi.org/10.5281/zenodo.10020346)
[![Running Code Coverage](https://github.com/EZ7051/cheapBuy/actions/workflows/code_cov.yml/badge.svg)](https://github.com/EZ7051/cheapBuy/actions/workflows/code_cov.yml)
[![Python Style Checker](https://github.com/EZ7051/cheapBuy/actions/workflows/style_checker.yml/badge.svg)](https://github.com/EZ7051/cheapBuy/actions/workflows/style_checker.yml)
[![Run Tests On Push](https://github.com/EZ7051/cheapBuy/actions/workflows/unit_test.yml/badge.svg?branch=main)](https://github.com/EZ7051/cheapBuy/actions/workflows/unit_test.yml)
[![Lint Python](https://github.com/EZ7051/cheapBuy/actions/workflows/main.yml/badge.svg)](https://github.com/EZ7051/cheapBuy/actions/workflows/main.yml)


<!--Badges-->
<a href="https://github.com/EZ7051/cheapBuy/blob/main/LICENSE" target="blank">
<img src="https://img.shields.io/github/license/EZ7051/cheapBuy?style=flat-square" alt="cheapBuy license" />
    
</a>
<a href="https://github.com/EZ7051/cheapBuy/forks" target="blank">
<img src="https://img.shields.io/github/forks/EZ7051/cheapBuy?style=flat-square" alt="cheapBuy forks"/>
</a>
<a href="https://github.com/EZ7051/cheapBuy/stargazers" target="blank">
<img src="https://img.shields.io/github/stars/EZ7051/cheapBuy?style=flat-square" alt="gcheapBuy stars"/>
</a>
<a href="https://github.com/EZ7051/cheapBuy/issues" target="blank">
<img src="https://img.shields.io/github/issues/EZ7051/cheapBuy?style=flat-square" alt="cheapBuy issues"/>
</a>
<a href="https://github.com/EZ7051/cheapBuy/issues?q=is%3Aissue+is%3Aclosed" target="blank">
<img src="https://img.shields.io/github/issues-closed/EZ7051/cheapBuy" alt="cheapBuy issues closed"/>
</a>
<a href="https://github.com/EZ7051/cheapBuy/pulls" target="blank">
<img src="https://img.shields.io/github/issues-pr/EZ7051/cheapBuy?style=flat-square" alt="cheapBuy pull-requests"/>
</a>
<a href="https://github.com/EZ7051/cheapBuy/milestones" alt="milestones">
<img src="https://img.shields.io/github/milestones/all/EZ7051/cheapBuy" /></a> 
<a href="https://github.com/EZ7051/cheapBuy/graphs/commit-activity" alt="commit activity">
<img src="https://img.shields.io/github/commit-activity/w/EZ7051/cheapBuy" /></a> 
<a href="https://img.shields.io/github/repo-size/EZ7051/cheapBuy" alt="repo size">
<img src="https://img.shields.io/github/repo-size/EZ7051/cheapBuy" /></a>



<p align="center">
    <a href="https://github.com/EZ7051/cheapBuy/issues/new/choose">Report Bug</a>
    ·
    <a href="https://github.com/EZ7051/cheapBuy/issues/new/choose">Request Feature</a>
</p>


<h1 align="center">
 <img src="https://github.com/freakleesin/cheapBuy/blob/main/media/saveMoney2.gif" />
</h1>


<h1 align="center">
  cheapBuy
</h1>

## Table of Contents
- [Introduction](#Introduction)
- [Features](#Features)
- [Demo](#Demo)
- [Installation Steps](#ExecutionSteps)
- [Plan of Action](#PlanofAction)
  - [Phase 1](#Phase1)
  - [Phase 2](#Phase2)
  - [Phase 3](#Phase3)
- [License](#License)
- [Contributing](#Contributing)
- [Team Members](#TeamMember)
- [Acknowledgements](#Acknowledgement)

## 📖 Introduction <a name="Introduction"></a>

**cheapBuy Extension** provides you an easy way to buy any product through your favourite website's like Amazon, Walmart, Ebay, Bjs, Costco, etc, while providing prices comparison from same product from different websites. Usually, it takes lot of time to do price comparison by checking different websites. However, you can instead add our extension **cheapBuy** and it will automatically fetch you price of the same product from different websites which you can then directly compare. This extension will not only save you time, but also save you money! Overall, **cheapBuy** is an one stop solution to buy the cheapest product online.
<h2 align="center">
 <img src= "https://github.com/anshulp2912/cheapBuy/blob/main/media/Drake_BF_meme.gif" width="500"/>
</h2>

## 🧐 Features <a name="Features"></a>
- **Price Comparison**
- **Get alternative website for the product**
- **Highlight Cheapest product**

## 🚀 Demo <a name="Demo"></a>
The project is deployed on Streamlit cloud:
- [Streamlit](https://share.streamlit.io/anshulp2912/cheapbuy/main/cheapBuy_user_interface.py)

## 🛠️ Steps of Execution <a name="ExecutionSteps"></a>

1. Clone the github repository at the preferable location in your local machine. You will need git to be preinstalled in the system. Once the repository is cloned in your system, with the help of cd command ,
```
git clone https://github.com/freakleesin/cheapBuy.git
cd cheapBuy
```
2. This project uses Python 3, so make sure that [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installation/) are preinstalled. All requirements of the project are listed in the ```requirements.txt``` file. Use pip to install all of the requirements.
```
pip install -r requirements.txt
```
3. Check out the demo video to know about the use of the website in the media files.
4. To locally run the streamlit website, we would recommend setting up an Anaconda Environment and running the command
```
streamlit run cheapBuy_user_interface.py
```

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

### PHASE-5 ⌛ <a name="Phase5"></a>
1. Dashboard including how many users click on the website.
2. Email notification of the available coupon to the user.
3. Alternate product suggestion feature.
4. Add more websites for web scrapping like Target, Kroger, and Traderjoes.

🌟 You are all set! 🌟

## 📝 License <a name="License"></a>
This project is licensed under the terms of the MIT license. Please check [License](https://github.com/EZ7051/cheapBuy/blob/main/LICENSE) for more details.

## 🍰 Contributing <a name="Contributing"></a>
Please contribute using [GitHub Flow](https://guides.github.com/introduction/flow). Create a branch, add commits, and [open a pull request](https://github.com/EZ7051/cheapBuy/compare).

Please read [`CONTRIBUTING`](CONTRIBUTING.md) for details on our [`CODE OF CONDUCT`](CODE_OF_CONDUCT.md), and the process for submitting pull requests to us.

## 👥 Team Members <a name="TeamMember"></a>
<table>
  <tr>
    <td align="center"><a href="https://github.com/EZ7051"><img src="https://avatars.githubusercontent.com/u/35006207?v=4" width="75px;" alt=""/><br /><sub><b>Ejaz</b></sub></a></td>
    <td align="center"><a href="https://github.com/shyni0201"><img src="https://avatars.githubusercontent.com/u/72161297?v=4" width="75px;" alt=""/><br /><sub><b>Shynitha</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/sumalatha-99"><img src="https://avatars.githubusercontent.com/u/26276595?v=4" width="75px;" alt=""/><br /><sub><b>Sumalatha</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/soubhagya31"><img src="https://avatars.githubusercontent.com/u/143368827?v=4" width="75px;" alt=""/><br /><sub><b>Soubhagya</b></sub></a><br /></td>
  </tr>
</table>

| Name                   | Unity ID                           |
|------------------------|------------------------------------|
| Ejaz Ahamed Shaik      | eshaik                             |
| Shynitha Muthyam       | smuthya                            |
| Soubhagya Akkena       | sakkena                            |
| Sumalatha Mashetty     | smashet                            |

## 🙏 Acknowledgements <a name="Acknowledgement"></a>
We would like to thank Professor Dr Timothy Menzies for helping us understand the process of building a good Software Engineering project. We would also like to thank the teaching assistants San Gilson, Andre Lustosa, Xueqi (Sherry) Yang, Yasitha Rajapaksha, and Rahul Yedida for their support throughout the project.
We would also like to extend our gratitude to the previous group : [https://github.com/rliu9/cheapBuy](https://github.com/rliu9/cheapBuy)
- [https://streamlit.io/](https://streamlit.io/)
- [https://shields.io/](https://shields.io/)
- [https://www.powtoon.com/](https://www.powtoon.com/)
<br>
