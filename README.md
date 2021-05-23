# br-scraping-npb
Baseball Reference Scraping for NPB

## Python Version

3.9+

## install

```bash
$ poetry install
```

## use 

### player list

```bash
$ python playesr.py
```

### stats batting + batter fielding

```bash
$ python stats_batter.py --filename dataset/player_batter_HokkaidoNipponHamFighters.csv
```

### stats pitching + pitcher fielding

```bash
$ python stats_pitcher.py --filename dataset/player_pitcher_HokkaidoNipponHamFighters.csv
```