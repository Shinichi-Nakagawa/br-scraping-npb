# チームの一覧を取得してCSV保存
import csv
from requests_html import HTMLSession

URLS = {
    'PACIFIC': 'https://www.baseball-reference.com/register/league.cgi?id=30c06d74',
    'CENTRAL': 'https://www.baseball-reference.com/register/league.cgi?id=4b244907',
}

session = HTMLSession()

values = []
for league, url in URLS.items():
    resp = session.get(url)
    tbody = resp.html.find('#regular_season > tbody', first=True)
    for tr in tbody.find('tr'):
        a = tr.find('a', first=True)
        team_url = a.absolute_links.pop()
        values.append({'team': tr.text.split('\n')[0], 'url': team_url})

with open('dataset/teams.csv', 'w') as f:
    writer = csv.DictWriter(f, fieldnames=['team', 'url'])

    writer.writeheader()
    writer.writerows(values)
