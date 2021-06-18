import uuid


class Tracker:
    def __init__(self, player1, player2, game_id=uuid.uuid1):
        self.game_id = game_id
        self.player1 = player1
        self.player2 = player2
        self.player1_score = 0
        self.player2_score = 0

    def update_score(self, player, new_score):
        if player == self.player1:
            self.player1_score = new_score
        elif player == self.player2:
            self.player2_score = new_score
        else:
            print("Player not valid")
