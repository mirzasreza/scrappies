from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():

    page_no = 1
    proceed = True

    while(proceed):
        url = 'https://books.toscrape.com/catalogue/page-"+str(page_no)+".html'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        if soup.title.text == "404 Not Found":
            proceed = False
        else:

        page_no += 1

    # Example: Extracting table data
    table = soup.find('table', {'id': 'example'})
    rows = table.find_all('tr')
"""
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])  # Get rid of empty values

    df = pd.DataFrame(data, columns=['Column1', 'Column2', 'Column3']) # Adjust column names as needed

    return render_template('index.html', tables=[df.to_html(classes='data')], titles=df.columns.values)
"""

if __name__ == '__main__':
    app.run(debug=True)
