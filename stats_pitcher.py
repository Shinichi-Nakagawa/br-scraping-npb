# 投手のstatsをひたすら保存
import os
import csv
import click

from service import get_page, write_csv
from br.pitcher import Pitcher
from br.fielder import Fielder


def run(filename: str):
    with open(filename, 'r') as f:
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
    # 成績を保存
    file_pitch = f"dataset/stats_pitching_{os.path.basename(filename)}"
    write_csv(filename=file_pitch, rows=stats_npb_pitch, fieldnames=Pitcher.COLUMNS)
    file_fileding = f"dataset/stats_filding_{os.path.basename(filename)}"
    write_csv(filename=file_fileding, rows=stats_npb_fileds, fieldnames=Fielder.COLUMNS)


@click.command()
@click.option('--filename', help='player file', required=True)
def cmd(filename):
    run(filename)


if __name__ == '__main__':
    cmd()
