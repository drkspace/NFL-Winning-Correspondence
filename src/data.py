import nflgame as ng


year = 2017

data = [[[], [], [], []] for _ in range(32)]

for week in range(1,18):
    games = ng.games(year, week)
    
