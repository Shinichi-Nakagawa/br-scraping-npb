# 野手のstatsをひたすら保存
import csv
from requests_html import HTMLSession

with open('dataset/player_batter.csv', 'r') as f:
    reader = csv.DictReader(f)
    players = [row for row in reader]

session = HTMLSession()
# NPB通算（打撃）
stats_npb_bats = []

# NPB通算（守備）
stats_npb_fileds = []
for player in players:
    response = session.get(player['player_url'])
    response.html.render(timeout=60)
    # 打撃
    standard_batting = response.html.find('#standard_batting > tfoot', first=True)
    for tr in standard_batting.find('tr'):
        level = tr.find('td:nth-child(3)', first=True)
        if level.text == 'NPB':
            row = {
                'url': player['player_url'],
                'name': player['player_name'],
                'G': tr.find('td:nth-child(5)', first=True).text,
                'PA': tr.find('td:nth-child(6)', first=True).text,
                'AB': tr.find('td:nth-child(7)', first=True).text,
                'R': tr.find('td:nth-child(8)', first=True).text,
                'H': tr.find('td:nth-child(9)', first=True).text,
                '2B': tr.find('td:nth-child(10)', first=True).text,
                '3B': tr.find('td:nth-child(11)', first=True).text,
                'HR': tr.find('td:nth-child(12)', first=True).text,
                'RBI': tr.find('td:nth-child(13)', first=True).text,
                'SB': tr.find('td:nth-child(14)', first=True).text,
                'CS': tr.find('td:nth-child(15)', first=True).text,
                'BB': tr.find('td:nth-child(16)', first=True).text,
                'SO': tr.find('td:nth-child(17)', first=True).text,
                'BA': tr.find('td:nth-child(18)', first=True).text,
                'OPS': tr.find('td:nth-child(19)', first=True).text,
                'TB': tr.find('td:nth-child(20)', first=True).text,
                'GIDP': tr.find('td:nth-child(21)', first=True).text,
                'HBP': tr.find('td:nth-child(22)', first=True).text,
                'SH': tr.find('td:nth-child(23)', first=True).text,
                'SF': tr.find('td:nth-child(24)', first=True).text,
                'IBB': tr.find('td:nth-child(25)', first=True).text,
            }
            stats_npb_bats.append(row)
            print(row)
    # 守備
    standard_fielding = response.html.find('#standard_fielding > tfoot', first=True)
    for tr in standard_fielding.find('tr'):
        level = tr.find('td:nth-child(3)', first=True)
        if level.text == 'NPB':
            row = {
                'url': player['player_url'],
                'name': player['player_name'],
                'POS': tr.find('td:nth-child(5)', first=True).text,
                'G': tr.find('td:nth-child(6)', first=True).text,
                'GS': tr.find('td:nth-child(7)', first=True).text,
                'CG': tr.find('td:nth-child(8)', first=True).text,
                'Inn': tr.find('td:nth-child(9)', first=True).text,
                'Ch': tr.find('td:nth-child(10)', first=True).text,
                'PO': tr.find('td:nth-child(11)', first=True).text,
                'A': tr.find('td:nth-child(12)', first=True).text,
                'E': tr.find('td:nth-child(13)', first=True).text,
                'DP': tr.find('td:nth-child(14)', first=True).text,
                'Fld_per': tr.find('td:nth-child(15)', first=True).text,
                'RF9': tr.find('td:nth-child(16)', first=True).text,
                'RFG': tr.find('td:nth-child(17)', first=True).text,
                'PB': tr.find('td:nth-child(18)', first=True).text,
                'WP': tr.find('td:nth-child(19)', first=True).text,
                'SB': tr.find('td:nth-child(20)', first=True).text,
                'CS': tr.find('td:nth-child(21)', first=True).text,
                'CS_per': tr.find('td:nth-child(22)', first=True).text,
                'lg_CS_per': tr.find('td:nth-child(23)', first=True).text,
                'PickOff': tr.find('td:nth-child(24)', first=True).text,
            }
            stats_npb_fileds.append(row)
            print(row)

# 年度成績（打撃）
# TODO あとでやる

# 年度成績（守備）
# TODO あとでやる
