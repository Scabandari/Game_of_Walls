

class Player:

    def __init__(self, name, direction, score, moves_since_point, row, col):
        self.name = name
        self.direction = direction
        self.score = score
        self.moves_since_point = moves_since_point
        self.row = row
        self.col = col
        self.game_piece = name+direction

    def print_player(self):
        print("\nPlayer: " + self.name + self.direction
              + " @ (" + str(self.row) + ", " + str(self.col) + ")")


