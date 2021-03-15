# 野手のstatsをひたすら保存
import csv

from service import get_page
from br.batter import Batter
from br.fielder import Fielder

with open('dataset/player_batter.csv', 'r') as f:
    reader = csv.DictReader(f)
    players = [row for row in reader]
# NPB通算（打撃, 守備）
stats_npb_bats = []
stats_npb_fileds = []

for player in players:
    response = get_page(url=player['player_url'])
    stats_npb_bats.extend(Batter.get_player_npb_stats(
        url=player['player_url'], name=player['player_name'], response=response
    ))
    stats_npb_fileds.extend(Fielder.get_player_npb_stats(
        url=player['player_url'], name=player['player_name'], response=response
    ))
    print('test')

# 年度成績（打撃）
# TODO あとでやる

# 年度成績（守備）
# TODO あとでやる
