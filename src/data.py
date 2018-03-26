import nflgame as ng
import teams
import pprint

teams = teams.teams()

year = 2017

data = [[[], [], [], []] for _ in range(32)]

for week in range(1,18):
    games = ng.games(year, week)
    plays = ng.combine_plays(games)
    for p in plays:
        tNum = teams.teamNumber(p.team)
        if p.down not in [1,2,3,4]:
            continue
        data = p.data
        #pprint.pprint(data)
        print data
        raw_input()
       
