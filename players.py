# 選手の一覧を取得してCSV保存
import csv
from requests_html import HTMLSession
from service import write_csv

with open('dataset/teams.csv', 'r') as f:
    reader = csv.DictReader(f)
    teams = [row for row in reader]

session = HTMLSession()

fieldnames = ['team', 'team_url', 'player_name', 'player_url']


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


# チームごと, 投手と野手, 分けて保存
for team in teams:
    response = session.get(team['url'])
    response.html.render(timeout=60)
    tbody = response.html.find('#team_batting > tbody', first=True)
    batters = players(tbody)
    write_csv(f'dataset/player_batter_{team["team"].replace(" ", "")}.csv', batters, fieldnames)
    tbody = response.html.find('#team_pitching > tbody', first=True)
    pitchers = players(tbody)
    write_csv(f'dataset/player_pitcher_{team["team"].replace(" ", "")}.csv', pitchers, fieldnames)
