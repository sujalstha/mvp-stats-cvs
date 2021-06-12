import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://www.basketball-reference.com/friv/mvp.html'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

columns = ['Rank', 'Player', 'Team', 'W', 'L', 'W/S%', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P',
           '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS',
           'Probability %']

df = pd.DataFrame(columns=columns)

table = soup.find('table', attrs={'class': 'sortable', 'id': 'players'}).tbody
trs = table.find_all('tr')

for tr in trs:
    tds = tr.find_all('td')
    row = [td.text.replace('\n', '') for td in tds]
    df = df.append(pd.Series(row, index=columns), ignore_index=True)

### Uncomment the code on line 24 and run it ###
# df.to_csv('nba mvp stats.csv', index=False)
