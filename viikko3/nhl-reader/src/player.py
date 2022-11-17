class Player:
    def __init__(self, name, team, goals, assists):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.assistsandgoals = self.goals+self.assists
        #self.nationality = nationality
    def __str__(self):
        return f'{self.name:20} {self.team:3} {self.goals:3} +{self.assists:3} = {self.assistsandgoals:2}'
