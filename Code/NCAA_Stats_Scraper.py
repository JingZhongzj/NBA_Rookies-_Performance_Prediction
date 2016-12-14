
from bs4 import BeautifulSoup
import requests

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for letter in letters:
    url = "http://www.basketball-reference.com/cbb/players/%s-index.html" %letter
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    links = soup.find('div', id="content" ).find_all('a')

    player_links = []
    player_names = []
    for link in links:
        if "players" in str(link):
            player_links.append("http://www.basketball-reference.com" + str(link.get('href')))
            print(link.text)

    players = []
    for player_link in player_links:
        r = requests.get(player_link)
        soup = BeautifulSoup(r.text, "html.parser")
        player_details = {}
        player_details['name'] = soup.find('div', id = 'meta').find(itemprop = 'name').text
        player_details['G'] = soup.find('tfoot').find('td', {'data-stat': 'g'}).text
        player_details['MP'] = soup.find('tfoot').find('td', {'data-stat': 'mp_per_g'}).text
        player_details['FG'] = soup.find('tfoot').find('td', {'data-stat': 'fg_per_g'}).text
        player_details['FGA'] = soup.find('tfoot').find('td', {'data-stat': 'fga_per_g'}).text
        player_details['FG%'] = soup.find('tfoot').find('td', {'data-stat': 'fg_pct'}).text
        player_details['2P'] = soup.find('tfoot').find('td', {'data-stat': 'fg2_per_g'}).text
        player_details['2PA'] = soup.find('tfoot').find('td', {'data-stat': 'fg2a_per_g'}).text
        player_details['2P%'] = soup.find('tfoot').find('td', {'data-stat': 'fg2_pct'}).text
        player_details['3P'] = soup.find('tfoot').find('td', {'data-stat': 'fg3_per_g'}).text
        player_details['3PA'] = soup.find('tfoot').find('td', {'data-stat': 'fg3a_per_g'}).text
        player_details['3P%'] = soup.find('tfoot').find('td', {'data-stat': 'fg3_pct'}).text
        player_details['FT'] = soup.find('tfoot').find('td', {'data-stat': 'ft_per_g'}).text
        player_details['FTA'] = soup.find('tfoot').find('td', {'data-stat': 'fta_per_g'}).text
        player_details['FT%'] = soup.find('tfoot').find('td', {'data-stat': 'ft_pct'}).text
        player_details['TRB'] = soup.find('tfoot').find('td', {'data-stat': 'trb_per_g'}).text
        player_details['AST'] = soup.find('tfoot').find('td', {'data-stat': 'ast_per_g'}).text
        player_details['STL'] = soup.find('tfoot').find('td', {'data-stat': 'stl_per_g'}).text
        player_details['BLK'] = soup.find('tfoot').find('td', {'data-stat': 'blk_per_g'}).text
        player_details['TOV'] = soup.find('tfoot').find('td', {'data-stat': 'tov_per_g'}).text
        player_details['PF'] = soup.find('tfoot').find('td', {'data-stat': 'pf_per_g'}).text
        player_details['PTS'] = soup.find('tfoot').find('td', {'data-stat': 'pts_per_g'}).text
        players.append(player_details)
        print(soup.find('div', id = 'meta').find(itemprop = 'name').text)

    id = 1    
    with open('NCAA_%s.txt' %letter, 'w') as file:
        for player in players:
            file.write('\n'+str(id))
            file.write(','+'{0}'.format(player['name']))
            file.write(','+'{0}'.format(player['G']))
            file.write(','+'{0}'.format(player['MP']))
            file.write(','+'{0}'.format(player['FG']))
            file.write(','+'{0}'.format(player['FGA']))
            file.write(','+'{0}'.format(player['FG%']))
            file.write(','+'{0}'.format(player['2P']))
            file.write(','+'{0}'.format(player['2PA']))
            file.write(','+'{0}'.format(player['2P%']))
            file.write(','+'{0}'.format(player['3P']))
            file.write(','+'{0}'.format(player['3PA']))
            file.write(','+'{0}'.format(player['3P%']))
            file.write(','+'{0}'.format(player['FT']))
            file.write(','+'{0}'.format(player['FTA']))
            file.write(','+'{0}'.format(player['FT%']))
            file.write(','+'{0}'.format(player['TRB']))
            file.write(','+'{0}'.format(player['AST']))
            file.write(','+'{0}'.format(player['STL']))
            file.write(','+'{0}'.format(player['BLK']))
            file.write(','+'{0}'.format(player['TOV']))
            file.write(','+'{0}'.format(player['PF']))
            file.write(','+'{0}'.format(player['PTS']))
            id = id + 1
    print 'OK_%s' %letter




