import requests
from bs4 import BeautifulSoup
import time

url_to_scrape = 'http://www.basketball-reference.com/players/b/'
r = requests.get(url_to_scrape)
soup = BeautifulSoup(r.text, "html.parser")

players_links = []

i = 0
for table_row in soup.select(".sortable tr"):
    if i > 0:
        table_headers = table_row.findAll('th')
        relative_link_to_player_details = table_headers[0].find('a')['href']
        absolute_link_to_player_details = "http://www.basketball-reference.com" + relative_link_to_player_details
        players_links.append(absolute_link_to_player_details)
    i = i + 1

print players_links[24]#now players_link saves profiles url of players

players = []
for player_link in players_links[:]:
    r = requests.get(player_link)
    soup = BeautifulSoup(r.text, "html.parser")
    player_details = {}
    player_details['name'] = soup.find('div', id = 'meta').find(itemprop = 'name').text
    player_details['height'] = soup.find('div', id = 'meta').find(itemprop = 'height').text
    player_details['weight'] = soup.find('div', id = 'meta').find(itemprop = 'weight').text
    p1 = soup.find('div', class_ = "stats_pullout").find('div', class_ = 'p1').text
    player_details['summary_G'] = p1.strip().split('\n')[1]
    player_details['summary_PTS'] = p1.strip().split('\n')[6]
    player_details['summary_TRB'] = p1.strip().split('\n')[11]
    player_details['summary_AST'] = p1.strip().split('\n')[16] 
    players.append(player_details)
    time.sleep(0.5)


id = 1
with open('P_A.txt', 'w') as file:
   for player in players:
        file.write('\n'+str(id))
        file.write(','+'{0}'.format(player['name']))
        file.write(','+'{0}'.format(player['height']))
        file.write(','+'{0}'.format(player['weight']))
        file.write(','+'{0}'.format(player['summary_G']))
        file.write(','+'{0}'.format(player['summary_PTS']))
        file.write(','+'{0}'.format(player['summary_TRB']))
        file.write(','+'{0}'.format(player['summary_AST']))
        id = id + 1
print 'OK'
