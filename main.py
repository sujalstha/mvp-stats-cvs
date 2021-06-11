import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://www.basketball-reference.com/friv/mvp.html'
response = requests.get(URL)
soup = BeautifulSoup(response, 'xml.parser')

columns = ['Rank', 'Player', 'Team', 'W', 'L', 'W/S%', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG7%', '3P', '3P%', '2P', '2P%',
           'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'Probability%']

df = pd.DataFrame(columns=columns)

table = soup.find('table', attrs={'class': 'sortable stats_table now_sortable', 'id': 'players'}).tbody

trs = table.find_all('tr')