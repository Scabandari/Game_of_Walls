import board
import player


class Game:
    def __init__(self, board, player_1, player_2):
        self.board = board
        self.player_1 = player_1
        self.player_2 = player_2

    def prepare_match(self):
        self.board.update_square(self.player_1.row, self.player_1.col, self.player_1.game_piece)
        self.board.update_square(self.player_2.row, self.player_2.col, self.player_2.game_piece)

    def print_match(self):
        print()
        print()
        print("Player: " + '{:>16}'.format(self.player_1.name) + '{:>10}'.format(self.player_2.name))
        print("Score:" + '{:>18}'.format(self.player_1.score) + '{:>10}'.format(self.player_2.score))
        print("Moves since Point: " + '{:>5}'.format(self.player_1.moves_since_point) +
              '{:>10}'.format(self.player_2.moves_since_point))
        print()
        self.board.print_board()

    def execute_match(self):
        i = 0
        while (self.player_1.moves_since_point < 6 or self.player_2.moves_since_point < 6) and \
                        (self.player_1.score + self.player_2.score) < self.board.width:
            if i % 2 == 0:
                self.player_1.make_move()
                self.board.print_board()
            else:
                self.player_2.make_move()
                self.board.print_board()
