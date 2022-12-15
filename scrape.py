from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pymongo
from pymongo import MongoClient

cluster = pymongo.MongoClient("mongodb+srv://hans:rupwTH9cVbCgGZht@nodecluster.gknsvxa.mongodb.net/?retryWrites=true&w=majority")

url = "https://www.basketball-reference.com/leagues/NBA_2023_per_game.html"
browser = webdriver.Chrome()
browser.get(url)
time.sleep(3)
html = browser.page_source
soup = BeautifulSoup(html, 'html.parser')

results = soup.find_all("tr", {"class":"full_table"})

def convertString(str):
    if not str:
        return -1
    else:
        num = float(str)
        return num

data = []
fantasy_stats = []
for result in results:
    datum = {}

    nameBox = result.find("td", {"data-stat": "player"})
    name = nameBox.find("a").get_text()

    pos = result.find("td", {"data-stat": "pos"}).get_text()
    age = int(result.find("td", {"data-stat": "age"}).get_text())

    teamBox = result.find("td", {"data-stat": "team_id"})
    team = teamBox.find("a").get_text()

    games = int(result.find("td", {"data-stat": "g"}).get_text())
    games_started = int(result.find("td", {"data-stat": "gs"}).get_text())
    minutes = convertString(result.find("td", {"data-stat": "mp_per_g"}).get_text())
    makes = convertString(result.find("td", {"data-stat": "fg_per_g"}).get_text())
    attempts = convertString(result.find("td", {"data-stat": "fga_per_g"}).get_text())
    fg_pct = convertString(result.find("td", {"data-stat": "fg_pct"}).get_text())
    fg3_makes = convertString(result.find("td", {"data-stat": "fg3_per_g"}).get_text())
    fg3_att = convertString(result.find("td", {"data-stat": "fg3a_per_g"}).get_text())
    fg3_pct = convertString(result.find("td", {"data-stat": "fg3_pct"}).get_text())
    fg2_makes = convertString(result.find("td", {"data-stat": "fg2_per_g"}).get_text())
    fg2_att = convertString(result.find("td", {"data-stat": "fg2a_per_g"}).get_text())
    fg2_pct = convertString(result.find("td", {"data-stat": "fg2_pct"}).get_text())
    efg = convertString(result.find("td", {"data-stat": "efg_pct"}).get_text())
    ft_makes = convertString(result.find("td", {"data-stat": "ft_per_g"}).get_text())
    ft_att = convertString(result.find("td", {"data-stat": "fta_per_g"}).get_text())
    ft_pct = convertString(result.find("td", {"data-stat": "ft_pct"}).get_text())
    orb = convertString(result.find("td", {"data-stat": "orb_per_g"}).get_text())
    drb = convertString(result.find("td", {"data-stat": "drb_per_g"}).get_text())
    reb = convertString(result.find("td", {"data-stat": "trb_per_g"}).get_text())
    ast = convertString(result.find("td", {"data-stat": "ast_per_g"}).get_text())
    stl = convertString(result.find("td", {"data-stat": "stl_per_g"}).get_text())
    blk = convertString(result.find("td", {"data-stat": "blk_per_g"}).get_text())
    to = convertString(result.find("td", {"data-stat": "tov_per_g"}).get_text())
    fouls = convertString(result.find("td", {"data-stat": "pf_per_g"}).get_text())
    pts = convertString(result.find("td", {"data-stat": "pts_per_g"}).get_text())
    
    datum['name'] = name
    datum['pos'] = pos
    datum['team'] = team
    datum['fg_pct'] = fg_pct
    datum['ft_pct'] = ft_pct
    datum['pts'] = pts
    datum['fg3_makes'] = fg3_makes
    datum['reb'] = reb
    datum['ast'] = ast
    datum['stl'] = stl
    datum['blk'] = blk
    datum['to'] = to

    fantasy_stats.append(datum)

    datum['age'] = age
    datum['games'] = games
    datum['games_started'] = games_started
    datum['minutes'] = minutes
    datum['makes'] = makes
    datum['attempts'] = attempts 
    datum['fg3_att'] = fg3_att
    datum['fg3_pct'] = fg3_pct
    datum['fg2_makes'] = fg2_makes
    datum['fg2_att'] = fg2_att
    datum['fg2_pct'] = fg2_pct
    datum['efg'] = efg
    datum['ft_makes'] = ft_makes
    datum['ft_att'] = ft_att
    datum['orb'] = orb
    datum['drb'] = drb
    datum['fouls'] = fouls

    data.append(datum)

db = cluster["basketball-data"]
collection = db["stats"]
#  collection.insert_many(fantasy_stats, {ordered: false})
collection.insert_many(data)


    

