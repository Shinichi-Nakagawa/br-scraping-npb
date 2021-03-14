# 選手の一覧を取得してCSV保存
import csv
from requests_html import HTMLSession

teams = []
with open('dataset/teams.csv', 'r') as f:
    reader = csv.DictReader(f)
    teams = [row for row in reader]

session = HTMLSession()


def players(tbody) -> list:
    result = []
    for tr in tbody.find('tr'):
        a = tr.find('a', first=True)
        if a is None:
            continue
        url = a.absolute_links.pop()
        name = tr.text.split('\n')[1].replace('*', '')
        result.append({'team': team['team'], 'team_url': team['url'], 'player_name': name, 'player_url': url})
    return result


# 投手と野手, 分けて保存
batters = []
pitchers = []
for team in teams:
    response = session.get(team['url'])
    response.html.render(timeout=60)
    tbody = response.html.find('#team_batting > tbody', first=True)
    batters.extend(players(tbody))
    tbody = response.html.find('#team_pitching > tbody', first=True)
    pitchers.extend(players(tbody))

# 書き込む
fieldnames = ['team', 'team_url', 'player_name', 'player_url']
with open('dataset/player_batter.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(batters)

with open('dataset/player_pitcher.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(pitchers)
