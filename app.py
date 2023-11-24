from flask import Flask, render_template, request, session, redirect, url_for
from source.web_scrappers.WebScrapper import WebScrapper
import source.database as db
import pandas as pd

db.initiate_database()

app = Flask(__name__)
app.secret_key = 'y2904c194hfoadpcascfeff4fv'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        url = request.form['url']
        sites = request.form['sites']

        webScrapper = WebScrapper(url)
        results = webScrapper.call_scrapper(sites)

        description, url, price, site = [], [], [], []

        if sites == "All Sites":
            for result in results:
                if result:
                    try:
                        description.append(result['description'])
                        url.append(result['url'])
                        price.append(
                            float(result['price'].strip('$').rstrip('0')))
                        site.append(result['site'])
                    except Exception as e:
                        print(e)
        else:
            for result in results:
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
            dataframe = pd.DataFrame({
                'description': description,
                'price': price,
                'url': url,
                'site': site
            })

            # Add a column for the link to the website
            dataframe['website_link'] = dataframe.apply(lambda row: f"/visit/{row['url']}/{row['site']}", axis=1)

            return render_template('result.html', dataframe=dataframe.to_dict(orient='records'))

@app.route('/create-account', methods=['POST'])
def create_account():
    username = request.form['username']
    password = request.form['password']
    result = db.create_user(username, password)
    if result == True:
        session['username'] = username # if account created, then login automatically
        return redirect(url_for('index')) # should be changed to user homepage redirect
    elif result == False:
        return render_template('index.html', error="User already exists") # index page error feedback
    else:
        return render_template('index.html', error="Something is wrong, try again later") # index page error feedback
 
if __name__ == '__main__':
    app.run(debug=True)
