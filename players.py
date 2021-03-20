# 選手の一覧を取得してCSV保存
import csv
from requests_html import HTMLSession

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


def write(filename: str, rows: list):
    with open(filename, 'w') as f:
        writer = csv.DictWriter(f, fieldnames=['team', 'team_url', 'player_name', 'player_url'])

        writer.writeheader()
        writer.writerows(rows)


# チームごと, 投手と野手, 分けて保存
for team in teams:
    response = session.get(team['url'])
    response.html.render(timeout=60)
    tbody = response.html.find('#team_batting > tbody', first=True)
    batters = players(tbody)
    write(f'dataset/player_batter_{team["team"].replace(" ", "")}.csv', batters)
    tbody = response.html.find('#team_pitching > tbody', first=True)
    pitchers = players(tbody)
    write(f'dataset/player_pitcher_{team["team"].replace(" ", "")}.csv', pitchers)
