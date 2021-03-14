# 投手のstatsをひたすら保存
import csv
from requests_html import HTMLSession

with open('dataset/player_pitcher.csv', 'r') as f:
    reader = csv.DictReader(f)
    players = [row for row in reader]

session = HTMLSession()
# NPB通算（投球）
stats_npb_pitch = []

for player in players:
    response = session.get(player['player_url'])
    response.html.render(timeout=60)
    # 打撃
    standard_pitching = response.html.find('#standard_pitching > tfoot', first=True)
    for tr in standard_pitching.find('tr'):
        level = tr.find('td:nth-child(3)', first=True)
        if level.text == 'NPB':
            row = {
                'url': player['player_url'],
                'name': player['player_name'],
                'W': tr.find('td:nth-child(5)', first=True).text,
                'L': tr.find('td:nth-child(6)', first=True).text,
                'W_per': tr.find('td:nth-child(7)', first=True).text,
                'ERA': tr.find('td:nth-child(8)', first=True).text,
                'RA9': tr.find('td:nth-child(9)', first=True).text,
                'G': tr.find('td:nth-child(10)', first=True).text,
                'GS': tr.find('td:nth-child(11)', first=True).text,
                'GF': tr.find('td:nth-child(12)', first=True).text,
                'CG': tr.find('td:nth-child(13)', first=True).text,
                'SHO': tr.find('td:nth-child(14)', first=True).text,
                'SV': tr.find('td:nth-child(15)', first=True).text,
                'IP': tr.find('td:nth-child(16)', first=True).text,
                'H': tr.find('td:nth-child(17)', first=True).text,
                'R': tr.find('td:nth-child(18)', first=True).text,
                'ER': tr.find('td:nth-child(19)', first=True).text,
                'HR': tr.find('td:nth-child(20)', first=True).text,
                'BB': tr.find('td:nth-child(21)', first=True).text,
                'IBB': tr.find('td:nth-child(22)', first=True).text,
                'SO': tr.find('td:nth-child(23)', first=True).text,
                'HBP': tr.find('td:nth-child(24)', first=True).text,
                'BK': tr.find('td:nth-child(25)', first=True).text,
                'WP': tr.find('td:nth-child(26)', first=True).text,
                'BF': tr.find('td:nth-child(27)', first=True).text,
                'WHIP': tr.find('td:nth-child(28)', first=True).text,
                'H9': tr.find('td:nth-child(29)', first=True).text,
                'HR9': tr.find('td:nth-child(30)', first=True).text,
                'BB9': tr.find('td:nth-child(31)', first=True).text,
                'SO9': tr.find('td:nth-child(32)', first=True).text,
                'SO_per_BB': tr.find('td:nth-child(33)', first=True).text,
            }
            stats_npb_pitch.append(row)
            print(row)