"""
Copyright (c) 2023 Group45
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

sites = st.selectbox("Select the website:", ("All Sites",
                             "amazon", "walmart", "ebay", "bjs", "costco", "bestbuy", "traderjoes", "kroger"))

st.header("Website: " + sites.capitalize() )


# Hide Footer in Streamlit
hide_menu_style = """
        <style>
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)


url = st.text_input('Enter the product')



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
        for result in results:
            # add results that only fit to selected price range :
            if result:
                try:
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
        # ''' if len(description) == len(url) == len(price) == len(site):
        #     dataframe = pd.DataFrame({'Description': description, 'Price': price, 'Link': url}, index=site)
        #     st.snow()
        #     st.markdown("<h1 style='text-align: center; color: #F6FFF8;'>RESULT</h1>", unsafe_allow_html=True)
        #     st.dataframe(dataframe.style.apply(highlight_row, axis=None))
        #     st.markdown("<h1 style='text-align: center; color: #F6FFF8;'>Visit the Website</h1>", unsafe_allow_html=True)

        # for s, u, p in zip(site, url, price):
        #     if p == min(price):
        #         if st.button('❄️  '+s+'  ❄️'):
        #             webbrowser.open(u)
        #     else:
        #         if st.button(s):
        #             webbrowser.open(u) '''
        # print(description)
        # print(price)
        if len(description) == len(url) == len(price) == len(site):
            dataframe = pd.DataFrame()
            dataframe['description'] = description
            dataframe['price']=price 
            dataframe['url'] = url
            # print(dataframe)
            dataframe.to_string(index=False, header=True)
        
        try:
            st.snow()
            st.markdown(
                "<h1 style='text-align: center; color: #F6FFF8;'>RESULT</h1>", unsafe_allow_html=True)
            # st.dataframe(dataframe, width=800, height=400, scrollable=True)
            # st.dataframe(dataframe.style.apply(highlight_row, axis=None))
            st.table(dataframe.style.highlight_max(axis=0, color='6B9080'))

            st.markdown(
                "<h1 style='text-align: center; color: #F6FFF8;'>Visit the Website</h1>", unsafe_allow_html=True)
        except:
            pass

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
