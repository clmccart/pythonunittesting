def tennis_score(player1_points, player2_points):
    game = TennisGame("Player 1", "Player 2")
    game.player1_points = player1_points
    game.player2_points = player2_points
    return game.score()

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def score(self):
        result = ""
        temp_score = 0
        if (self.player1_points == self.player2_points):
            result = {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All"
            }.get(self.player1_points, "Deuce")
        elif (self.player1_points >= 4 or self.player2_points >= 4):
            minus_result = self.player1_points - self.player2_points
            if (minus_result == 1):
                result = "Advantage " + self.player1_name
            elif (minus_result == -1):
                result = "Advantage " + self.player2_name
            elif (minus_result >= 2):
                result = "Win for " + self.player1_name
            else: 
                result = "Win for " + self.player2_name
        else:
            for i in range(1,3):
                if (i==1):
                    temp_score = self.player1_points
                else: 
                    result += "-"
                    temp_score = self.player2_points
                result += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty"
                }[temp_score]
        return result

    def won_point(self, player_name): # pragma: no cover
        if player_name == self.player1_name:
            self.player1_points += 1
        else:  
            self.player2_points += 1
        