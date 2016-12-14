
import requests
from bs4 import BeautifulSoup
import time




s = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
players_links = []
for i in s[25]:############################
    url_to_scrape = 'http://www.basketball-reference.com/players/%s/' %i
    print url_to_scrape
    r = requests.get(url_to_scrape)
    soup = BeautifulSoup(r.text)


    i = 0
    for table_row in soup.select(".sortable tr"):
        if i > 0:
            table_headers = table_row.findAll('th')
            relative_link_to_player_details = table_headers[0].find('a')['href']
            absolute_link_to_player_details = "http://www.basketball-reference.com" + relative_link_to_player_details
            players_links.append(absolute_link_to_player_details)
        i = i + 1

print players_links[0]#now players_link saves profiles url of players

players = []
j = 0
Title = ['G','GS','MP','FG','FGA','FG%','3P','3PA','3P%','2P','2PA','2P%','eFG%','FT','FTA','FT%','ORB','DRB','TRB','AST','STL','BLK','TOV','PF','PTS']
for player_link in players_links[:]:#########################
    r = requests.get(player_link)
    soup = BeautifulSoup(r.text)
    player_details = {}
    player_details['name'] = soup.find('div', id = 'meta').find(itemprop = 'name').text
    print player_details['name']
    try:
        player_details['height'] = soup.find('div', id = 'meta').find(itemprop = 'height').text
    except:
        player_details['height'] = 0
    try:
        player_details['weight'] = soup.find('div', id = 'meta').find(itemprop = 'weight').text
    except:
        player_details['weight'] = 0
    #player_profile_rows = soup.select(".row_summable tr")
    #career_row = player_profile_rows[10]#.findAll('td')[0].text
    #idex = 0
    CareerRow = soup.find('table', class_ = 'row_summable').find('tfoot').findAll('tr')[0]
    #print CareerRow
    Career_Stats = CareerRow.findAll('td')
    idex = 0
    for it in Career_Stats[4:]:
        player_details[Title[idex]] = it.text.strip()
        idex = idex + 1 
    #for item in career_row.findAll('td')[4:]:
    #    player_details[Title[idex]] = item.text.strip()
    #    idex = idex + 1        
    players.append(player_details)
    print j
    j = j + 1
    time.sleep(0.9)


id = 4724
with open('P_00z.txt', 'w') as file:
   file.write('id')
   file.write(','+'name')
   file.write(','+'height')
   file.write(','+'weight')
   for it01 in Title:
       file.write(','+it01) 
   for player in players:
        file.write('\n'+str(id))
        file.write(','+'{0}'.format(player['name']))
        file.write(','+'{0}'.format(player['height']))
        file.write(','+'{0}'.format(player['weight']))
        for it in Title:
            file.write(','+'{0}'.format(player[it]))
        id = id + 1
print 'OK'