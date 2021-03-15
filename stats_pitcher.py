# 投手のstatsをひたすら保存
import csv

from service import get_page
from br.pitcher import Pitcher
from br.fielder import Fielder

with open('dataset/player_pitcher.csv', 'r') as f:
    reader = csv.DictReader(f)
    players = [row for row in reader]
# NPB通算（投球）
stats_npb_pitch = []
stats_npb_fileds = []

for player in players:
    response = get_page(url=player['player_url'])
    stats_npb_pitch.extend(Pitcher.get_player_npb_stats(
        url=player['player_url'], name=player['player_name'], response=response
    ))
    stats_npb_fileds.extend(Fielder.get_player_npb_stats(
        url=player['player_url'], name=player['player_name'], response=response
    ))
    print('test')
