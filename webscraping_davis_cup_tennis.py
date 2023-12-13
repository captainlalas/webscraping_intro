import pandas as pd
from bs4 import BeautifulSoup
import requests
import sqlite3

# This project is about the most successful tennis player in the davis cup Open Era (from 1968)
url = 'https://en.wikipedia.org/wiki/Davis_Cup_winning_players'
db_name = 'players.db'
table_name = 'Top_20'
csv_path = 'top_20_players_davis_cup_titles.csv'
df = pd.DataFrame(columns=["Player Name","Titles Won", "Years"])
count = 0

# Let's load the webpage with requests for scraping and parsing it with BS
html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser')

# Scraping the infos on the (1st) table
tables = data.find_all('tbody')
rows = tables[1].find_all('tr')
# Time now to iterate over the rows after the 1st row (header of the table)
for row in rows:
    if count < 20:
        col = row.find_all('td')
        if len(col)!=0:
            data_dict = {"Player Name": col[0].contents[2], #contents[2] because the 1st row conatins some formatting for the flags
                        "Titles Won" : col[1].contents[0],
                        "Years" : col[2].contents[0]}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)
            count += 1
    else:
        break

print(df)
# Result of the print

# Storing the data in a csv file in our project folder
df.to_csv(csv_path, index=False)

# Storing the data now as table of a db in sqlite3 and closing the connection
con = sqlite3.connect(db_name)
df.to_sql(table_name, con, if_exists='replace', index=False)
con.close()