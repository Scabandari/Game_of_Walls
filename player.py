

class Player:

    def __init__(self, name, direction, score, moves_since_point, row, col, captured_square, opponent=None):
        self.name = name
        self.direction = direction
        self.score = score
        self.moves_since_point = moves_since_point
        self.row = row
        self.col = col
        self.game_piece = name+direction
        self.captured_square = captured_square
        self.opponent = opponent
 #       self.captured_square = self.name.lower() + self.name.lower()

    def print_player(self):
        print("\nPlayer: " + self.name + self.direction
              + " @ (" + str(self.row) + ", " + str(self.col) + ")")

    def turn_right(self):
        if self.direction == 'L':
            self.direction = 'U'
        elif self.direction == 'U':
            self.direction = 'R'
        elif self.direction == 'R':
            self.direction = 'D'
        elif self.direction == 'D':
            self.direction = 'L'

    def turn_left(self):
        if self.direction == 'L':
            self.direction = 'D'
        elif self.direction == 'U':
            self.direction = 'L'
        elif self.direction == 'R':
            self.direction = 'U'
        elif self.direction == 'D':
            self.direction = 'R'

    def update_game_piece(self):
        self.game_piece = self.name + self.direction