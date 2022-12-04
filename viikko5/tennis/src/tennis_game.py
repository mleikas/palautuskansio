class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_score = 0
        self.p2_score = 0
        self.p_names = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty",
            4: "All",
            5: "Deuce"
        }

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1_score += 1
        else:
            self.p2_score += 1

    def get_score(self):
        self.score = ""
        if self.p1_score == self.p2_score:
            self.tie()
        elif self.p1_score >= 4 or self.p2_score >= 4:
            self.advantage()
        else:
            self.print_score()

        return self.score

    def tie(self):
        if self.p1_score == 0:
            self.score = "Love-All"
        elif self.p1_score == 1:
            self.score = "Fifteen-All"
        elif self.p1_score == 2:
            self.score = "Thirty-All"
        elif self.p1_score == 3 and self.p2_score == 3:
            self.score = "Forty-All"
        else:
            self.score = "Deuce"

    
    def advantage(self):
        minus_result = self.p1_score - self.p2_score

        if minus_result == 1:
            self.score = f"Advantage {self.player1_name}"
        elif minus_result == -1:
            self.score = f"Advantage {self.player2_name}"
        elif minus_result >= 2:
            self.score = f"Win for {self.player1_name}"
        else:
            self.score = f"Win for {self.player2_name}"

    
    def print_score(self):
        temp_score = 0
        for player in range(1, 3):
            if player == 1:
                temp_score = self.p1_score
            else:
                self.score = self.score + "-"
                temp_score = self.p2_score

            if temp_score == 0:
                self.score += "Love"
            elif temp_score == 1:
                self.score += "Fifteen"
            elif temp_score == 2:
                self.score += "Thirty"
            elif temp_score == 3:
                self.score += "Forty"
