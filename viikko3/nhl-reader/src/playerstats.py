from player import Player

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = []

    def top_scorers_by_nationality(self, nationality):
        for player_dict in self.reader.response:
            if player_dict['nationality']==nationality:
                player = Player(
                    player_dict['name'], 
                    player_dict['team'], 
                    player_dict['goals'], 
                    player_dict['assists'],
                )
                self.players.append(player)
        print(f"Players from {nationality}")
        self.players=sorted(self.players, key=lambda h:(h.assistsandgoals),reverse=True)
        return self.players