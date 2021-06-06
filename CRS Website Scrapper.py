# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 18:55:16 2021

@author: John
"""


from bs4 import BeautifulSoup
import requests
import pandas as pd
import re


url = "https://www.canada.ca/en/immigration-refugees-citizenship/corporate/mandate/policies-operational-instructions-agreements/ministerial-instructions/express-entry-rounds.html#wb-auto-4"

# Get request
r = requests.get(url).text

# Parse HTML code
soup = BeautifulSoup(r, 'lxml')
print(soup.prettify())

# search entire html for table tag, class named summary or class that equals the table (LOOK FOR TABLE TAG)
table = soup.find_all('table', {"class": "wb-tables table"})[0]


# Get headers of table, go to HTML to find tags that have the headers (th tag for headers)
headers = []

# create loop to go over headers - THIS IS UNIVERSAL CODE TO GET ALL HEADERS
for i in table.find_all('th'):
    title = i.text.strip()
    headers.append(title)
    

# Create dataframe with headers we got
df = pd.DataFrame(columns=headers)
df


# whole rows have tr TAG, use loop to find all the rows
# Within rows, the data inside the cells are in td tag
# use [1:] as we need to skip first row of headers in html
for row in table.find_all('tr')[1:]:
    data = row.find_all('td')
    
    row_data = [td.text.strip() for td in data]
    length = len(df)
    df.loc[length] = row_data
    
df.to_csv('crs data.csv', index = False)