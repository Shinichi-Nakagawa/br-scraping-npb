import glob
import pandas as pd


def concat(pattern: str) -> pd.DataFrame:
    stats = []
    for stats_file in glob.glob(f'dataset/{pattern}*.csv'):
        _df = pd.read_csv(str(stats_file))
        stats.append(_df)
    return pd.concat(stats)


# 打者一覧
dfb = concat('player_batter_')

# 投手一覧
dfp = concat('player_pitcher_')

# 投手と打者一覧をjoinして選手一覧を作る
pd.concat([dfp, dfb]).to_csv('dataset/players.csv', index=False)
#
# # 打者成績一覧
df_bs = concat('stats_batting_player_batter_')
df_bs.to_csv('dataset/stats_batting.csv', index=False)
#
# # 投手成績一覧
df_ps = concat('stats_pitching_player_pitcher_')
df_ps.to_csv('dataset/stats_pitching.csv', index=False)
#
# 守備成績
df_fs = concat('stats_filding_player_')
df_fs.to_csv('dataset/stats_filding.csv', index=False)
