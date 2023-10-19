"""
Copyright (c) 2021 Anshul Patel
This code is licensed under MIT license (see LICENSE.MD for details)

@author: cheapBuy
"""

# Import Libraries
import webbrowser
import pandas as pd
from source.web_scrappers.WebScrapper import WebScrapper
import os
import streamlit as st
import sys
sys.path.append('../')


# title = '<p style="font-family:Apple Chancery, cursive; color:#2F184B; font-size: 157px;">CheapBuy</p>'
title = '<p style="font-family:Apple Chancery, cursive; color:#6B9080; font-size: 157px;">CheapBuy</p>'
st.markdown(title, unsafe_allow_html=True)

# Add tagline just below the title and to the right
tagline = '<p style="color: #6B9080; font-size: 24px; text-align: right;">Your One-Stop Shop for the Best Deals</p>'
st.markdown(tagline, unsafe_allow_html=True)
# st.title("CheapBuy")
# st.markdown(title, unsafe_allow_html=True)
# st.image("media/saveMoney2.gif")
#url_sidebar = st.sidebar.text_input('Quick Action: Open a new page')

# st.sidebar.image("media/cheapBuy_Banner.gif")
#st.sidebar.image("media/saveMoney2.gif")
# st.sidebar.title("Customize Options Here:")
sites = st.selectbox("Select the website:", ("All Sites",
                             "amazon", "walmart", "ebay", "bjs", "costco", "bestbuy", "traderjoes", "kroger"))

#price_range = st.sidebar.selectbox("Select the price range:", (
 #   "all", "Under $50", "[$50, $100)", "[$100, $150)", "[$150, $200)", "$200 & Above"))
st.header("Website: " + sites.capitalize() )
          # '| |' + "Price Range: " + price_range)
#st.header("Price Range: " + price_range)


# if url_sidebar:
#     webbrowser.open(url_sidebar)

# Hide Footer in Streamlit
hide_menu_style = """
        <style>
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


# Display Image

# st.sidebar.write("cheapBuy provides you ease to buy any product through your favourite website's like Amazon, Walmart, Ebay, Bjs, Costco, etc, by providing prices of the same product from all different websites")
#st.write("cheapBuy provides you ease to buy any product through your favourite website's like Amazon, Walmart, Ebay, Bjs, Costco, etc, by providing prices of the same product from all different websites")
url = st.text_input('Enter the product')
# # Create a list of options for the dropdown
# options = ["Option 1", "Option 2", "Option 3"]
#
# # Create the dropdown
# selected_option = st.selectbox("Select an option:", options)
#
# # Display the selected option
# st.write("You selected:", selected_option)


# def price_filter(price_range):
#     #price_min, price_max = 0.0, 0.0
#     if price_range == "Under $50":
#         price_min, price_max = 0.0, 49.99
#     elif price_range == "[$50, $100)":
#         price_min, price_max = 50.0, 99.99
#     elif price_range == "[$100, $150)":
#         price_min, price_max = 100.0, 149.99
#     elif price_range == "[$150, $200)":
#         price_min, price_max = 150.0, 199.99
#     elif price_range == "$200 & Above":
#         price_min, price_max = 200.0, float('inf')
#     else:
#         price_min, price_max = 0.0, float('inf')
#     return price_min, price_max
#
#
# price_min, price_max = price_filter(price_range)

# Pass url to method
if url:
    webScrapper = WebScrapper(url)
    results = webScrapper.call_scrapper(sites)

    # Use st.columns based on return values
    description, url, price, site = [], [], [], []

    if sites == "All Sites":
        for result in results:
            # add results that only fit to selected price range :
            if result:
                try:
                    # if price_min <= float(result['price'][1:]) <= price_max:
                        description.append(result['description'])
                        url.append(result['url'])
                        price.append(
                            float(result['price'].strip('$').rstrip('0')))
                        site.append(result['site'])
                except Exception as e:
                    print(e)

    else:
        # if sites not in site:
        #st.error('Sorry, there is no same product in your selected website.')

        # else:
        for result in results:
            # add results that only fit to selected price range :
            if result:
                try:
                    # if price_min <= float(result['price'][1:]) <= price_max:
                        # print(result['site'])
                        if result['site'].strip() == sites:
                            description.append(result['description'])
                            url.append(result['url'])
                            price.append(
                                float(result['price'].strip('$').rstrip('0')))
                            site.append(result['site'])
                except Exception as e:
                    print(e)

    if len(price):

        def highlight_row(dataframe):
            # copy df to new - original data are not changed
            df = dataframe.copy()
            minimumPrice = df['Price'].min()
            # set by condition
            mask = df['Price'] == minimumPrice
            df.loc[mask, :] = 'background-color: #F6FFF8'
            df.loc[~mask, :] = 'background-color: #CCE3DE'
            return df

        dataframe = pd.DataFrame(
            {'Description': description, 'Price': price, 'Link': url}, index=site)
        st.snow()
        st.markdown(
            "<h1 style='text-align: center; color: #F6FFF8;'>RESULT</h1>", unsafe_allow_html=True)
        st.dataframe(dataframe.style.apply(highlight_row, axis=None))
        st.markdown(
            "<h1 style='text-align: center; color: #F6FFF8;'>Visit the Website</h1>", unsafe_allow_html=True)

        for s, u, p in zip(site, url, price):
            if p == min(price):
                if st.button('❄️  '+s+'  ❄️'):
                    webbrowser.open(u)
            else:
                if st.button(s):
                    webbrowser.open(u)

    elif not description or not url or not price or not site:
        st.error('Sorry, there is no product on your selected options.')
    else:
        st.error('Sorry, there is no other website with same product.')


# Add footer to UI
footer = """<style>
a:link , a:visited{
color: #6B9080;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: #F6FFF8;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0%;
width: 100%;
background-color: #CCE3DE;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p><a style='display: block; text-align: center;' href="https://github.com/EZ7051/cheapBuy" target="_blank">Developed with ❤ by CheapBuy</a></p>
<p><a style='display: block; text-align: center;' href="https://github.com/EZ7051/cheapBuy/blob/main/LICENSE" target="_blank">MIT License Copyright (c) 2021 cheapBuy</a></p>
<p>Contributors: 

<a href="https://github.com/EZ7051" target="_blank">Ejaz</a>,
<a href="https://github.com/shyni0201" target="_blank">Shynitha</a>,
<a href="https://github.com/sumalatha-99" target="_blank">Sumalatha</a>,
<a href="https://github.com/soubhagya31" target="_blank">Soubhagya</a>

</div>
"""

st.markdown(footer, unsafe_allow_html=True)
