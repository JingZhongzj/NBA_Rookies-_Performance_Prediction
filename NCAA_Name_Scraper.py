
from bs4 import BeautifulSoup
import requests


letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for letter in letters:
    url = "http://www.cbssports.com/collegebasketball/playersearch?last_name_begins=%s&print_rows=9999" %letter
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    players = []
    
    tr = soup.find('table', {'class': "data"}).find_all('tr', {'align': "right"})
    for i in tr:
        player_details = {}
        Name_list = list(reversed(i.find('a').text.split(',')))
        player_details['name'] = Name_list[0] + " " + Name_list[1]
        players.append(player_details)
        print(player_details['name'])
        
    
id = 1
with open('NCAA_Names.txt', 'w') as file:
    for player in players:
        file.write('\n'+str(id))
        file.write(','+'{0}'.format(player['name']))
        id = id + 1
print('OK')




