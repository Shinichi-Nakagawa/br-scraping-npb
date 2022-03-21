from glob import glob
from multiprocessing import Pool
import time

from stats_batter import run

filelist = [file for file in glob('dataset/player_batter_*.csv')]
for f in filelist:
    print(f'start: {f}')
    run(f)
    print(f'end: {f}')
