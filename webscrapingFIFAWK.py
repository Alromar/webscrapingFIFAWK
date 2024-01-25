# tut: https://www.youtube.com/watch?v=XDIscigGpGI The PyCoach
# toepassen op CL-league: https://en.wikipedia.org/wiki/UEFA_Champions_League

from bs4 import BeautifulSoup
import requests
import lxml
import pandas as pd


years = [1930, 1934, 1938,1950, 1954, 1958, 1962, 1966, 1970, 1974,
         1978, 1982, 1986, 1990, 1994,1998, 2002, 2006, 
         2010, 2014, 2018, 2022]

def get_matches(year):
    web = f'https://en.wikipedia.org/wiki/{year}_FIFA_World_Cup'

    response = requests.get(web)
    print(response.text)
    content = response.text
    soup = BeautifulSoup(content, 'lxml')

    matches = soup.find_all('div', class_='footballbox')

    home = []
    score = []
    away = []

    for match in matches:
        # print(match.find('th', class_='fhome').get_text())
        # print(match.find('th', class_='fscore').get_text())
        # print(match.find('th', class_='faway').get_text())
        home.append(match.find('th', class_='fhome').get_text())
        score.append(match.find('th', class_='fscore').get_text())
        away.append(match.find('th', class_='faway').get_text())

    dict_football = {'home': home, 'score': score, 'away': away}
    df_football = pd.DataFrame(dict_football)
    df_football['year'] = year
    return df_football


# print(get_matches('2022'))
fifa = [get_matches(year) for year in years]
df_fifa = pd.concat(fifa, ignore_index=True)
df_fifa.to_csv('fifa_WC_history.csv', index=False)

# fixtures



for year in years:
    get_matches(year)
# web = 'https://en.wikipedia.org/wiki/2014_FIFA_World_Cup'
#
# response = requests.get(web)
# print(response.text)
# content = response.text
# soup = BeautifulSoup(content, 'lxml')
#
# matches = soup.find_all('div', class_='footballbox')
#
# home = []
# score = []
# away = []
#
# for match in matches:
#     # print(match.find('th', class_='fhome').get_text())
#     # print(match.find('th', class_='fscore').get_text())
#     # print(match.find('th', class_='faway').get_text())
#     home.append(match.find('th', class_='fhome').get_text())
#     score.append(match.find('th', class_='fscore').get_text())
#     away.append(match.find('th', class_='faway').get_text())
#
# dict_football = {'home': home, 'score': score, 'away': away}
# df_football = pd.DataFrame(dict_football)
# df_football['year'] = '2014'
# print(df_football)

