import board
import player
import game
import math

#def initialize_board(self,Player, Board)


def main():
    print("hello cruel world!")

    p1 = player.Player("A", "L", 0, 0, 1, 0)
    p2 = player.Player("B", "R", 0, 0, math.ceil(board.Board.width/2)-1, board.Board.width-1)
    p1.print_player()
    p2.print_player()

    b1 = board.Board()
    b1.print_board()

    my_game = game.Game(b1, p1, p2);
    my_game.prepare_match()
    my_game.print_match()


if __name__ == "__main__":
    main()
