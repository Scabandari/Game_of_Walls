

class Player:

    def __init__(self, name, direction, score, moves_since_point, row, col, brd):
        self.name = name
        self.direction = direction
        self.score = score
        self.moves_since_point = moves_since_point
        self.row = row
        self.col = col
        self.game_piece = name+direction
        self.brd = brd
        self.captured_square = self.name.lower() + self.name.lower()

    def print_player(self):
        print("\nPlayer: " + self.name + self.direction
              + " @ (" + str(self.row) + ", " + str(self.col) + ")")

    def make_move(self):
        print("Player " + self.name + "'s move. Enter L or R to turn left or right. Enter F to try forward: ")
        boolean = False
        while not boolean:
            move = input()
            if move == 'l' or move == 'L':
                self.direction = 'L'
                boolean = True
            elif move == 'r' or move == 'R':
                self.direction = 'R'
                boolean = True
            elif move == 'f' and move == 'F':
                boolean = True

                if self.direction == 'U' and self.row >= 1:
                    self.brd.update_square(self.row, self.col, self.captured_square)
                    self.row = self.row - 1
                    self.update_game_piece()
                    self.brd.update_square(self.row, self.col, self.game_piece)

                elif self.direction == 'L' and self.col >= 1:
                    self.brd.update_square(self.col, self.row, self.captured_square)
                    self.col = self.col -1
                    self.update_game_piece()
                    self.brd.update_square(self.row, self.col, self.game_piece)

                elif self.direction == 'D' and self.row <= board.width-1:
                    self.brd.update_square(self.col, self.row, self.captured_square)
                    self.row = self.row + 1
                    self.update_game_piece()
                    self.brd.update_square(self.row, self.col, self.game_piece)

                elif self.direction == 'R' and self.row <= board.width - 1:
                    self.brd.update_square(self.col, self.row, self.captured_square)
                    self.col = self.col + 1
                    self.update_game_piece()
                    self.brd.update_square(self.row, self.col, self.game_piece)

            else:
                print("That is not a valid input (L, R, U)")

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
        if self.direction == 'U':
            self.direction = 'L'
        if self.direction == 'R':
            self.direction = 'U'
        if self.direction == 'D':
            self.direction = 'R'

    def update_game_piece(self):
        self.game_piece = self.name + self.direction