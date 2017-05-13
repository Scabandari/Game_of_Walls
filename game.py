
class Game:
    def __init__(self, board_, player_1, player_2):
        self.board_ = board_
        self.player_1 = player_1
        self.player_2 = player_2

    def prepare_match(self):
        self.board_.update_square(self.player_1.row, self.player_1.col, self.player_1.game_piece)
        self.board_.update_square(self.player_2.row, self.player_2.col, self.player_2.game_piece)
        self.player_1.opponent = self.player_2
        self.player_2.opponent = self.player_1

    def print_match(self):
        print()
        print()
        print("Player: " + '{:>16}'.format(self.player_1.name) + '{:>10}'.format(self.player_2.name))
        print("Score:" + '{:>18}'.format(self.player_1.score) + '{:>10}'.format(self.player_2.score))
        print("Moves since Point: " + '{:>5}'.format(self.player_1.moves_since_point) +
              '{:>10}'.format(self.player_2.moves_since_point))
        print()
        self.board_.print_board()

    def execute_match(self):
        i = 0
        while (self.player_1.moves_since_point < 6 or self.player_2.moves_since_point < 6) and \
                        (self.player_1.score + self.player_2.score) < self.board_.width:
            if i % 2 == 0:
                i += 1
                self.make_move(self.player_1)
                self.print_match()
            else:
                i += 1
                self.make_move(self.player_2)
                self.print_match()

    def make_move(self, player_):
        print("Player " + player_.name + "'s move.")
        while True:
            print("Enter L or R to turn left or right. Enter F to try forward:\n ")
            move = input()
            if move == 'l' or move == 'L':
                player_.turn_left()
                player_.update_game_piece()
                self.board_.update_square(player_.row, player_.col, player_.game_piece)
                break
            elif move == 'r' or move == 'R':
                player_.turn_right()
                player_.update_game_piece()
                self.board_.update_square(player_.row, player_.col, player_.game_piece)
                break
            elif move == 'f' or move == 'F':
                if player_.direction == 'U' and player_.row >= 1:
                    self.board_.update_square(player_.row, player_.col, player_.captured_square)
                    player_.row -= 1
                    if self.board_.get_square(player_.row, player_.col) == 'OO':
                        player_.score += 1
                    self.board_.update_square(player_.row, player_.col, player_.game_piece)
                    break

                elif player_.direction == 'L' and player_.col >= 1:
                    self.board_.update_square(player_.row, player_.col, player_.captured_square)
                    player_.col -= 1
                    if self.board_.get_square(player_.row, player_.col) == 'OO':
                        player_.score += 1
                    self.board_.update_square(player_.row, player_.col, player_.game_piece)
                    break

                elif player_.direction == 'D' and player_.row <= self.board_.width - 1:
                    self.board_.update_square(player_.row, player_.col, player_.captured_square)
                    player_.row += 1
                    if self.board_.get_square(player_.row, player_.col) == "OO":
                        player_.score += 1
                    self.board_.update_square(player_.row, player_.col, player_.game_piece)
                    break

                elif player_.direction == 'R' and player_.row <= self.board_.width - 1:
                    self.board_.update_square(player_.row, player_.col, player_.captured_square)
                    player_.col += 1
                    if self.board_.get_square(player_.row, player_.col) == 'OO':
                        player_.score += 1
                    self.board_.update_square(player_.row, player_.col, player_.game_piece)
                    break
                else:
                    break

            else:
                print("That is not a valid input (L, R, F)")
