import nflgame as ng

class teams():

    def __init__(self):
        self.teams = ng.teams
    
    def teamNumber(self, team):
        for i in range(len(self.teams)):
            if team in self.teams[i]:
                return i
        return -1
        