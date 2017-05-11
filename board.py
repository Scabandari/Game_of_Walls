
class Board:

    width = 3
    board_squares = ('O', 'L', 'R', 'U', 'D' 'A', 'B')
    game_board = [['OO', 'OO', 'OO'], ['OO', 'OO', 'OO'], ['OO', 'OO', 'OO']]

    def __init__(self):
        pass

    def print_board(self):
        for i in range(self.width):
            print(self.game_board[i][0] + " " + self.game_board[i][1] + " " + self.game_board[i][2])

    def update_square(self, row, col, str_param):
        self.game_board[row][col] = str_param

 #   def reset_board(self):
 #       for i in range(self.width-1):
  #          for j in range(self.width-1):
  #              board.game_board[i][j] = 'OO'