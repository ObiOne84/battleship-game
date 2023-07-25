import time
import sys
from random import randint


def print_out(data):
    """
    The function will display text as it typed in real
    time rather than dispaly all message at once
    """
    for letter in data:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)


class GameBoard:
    """
    The class holds the game board, ships position and user guesses
    """

    def __init__(self, size):
        self.size = size
        self.board = [["-" for x in range(size)] for y in range(size)]

    def print_board(self):
        """
        Function prints the game board, take size as parameter
        and sets letter at the begining of each row
        """

        alphabet = ["ABCDEFGHIJKLMNOPRTQUXYZ"]

        # if n is a paramter, take n number of characters from the alphabet
        alphabet = ''.join(alphabet[:size])

        column_values = []
        for num in range(size):
            column_values.append(num + 1)

        print(" ", *column_values)

        # with assist of Sean - Tutor
# loop over the zipped lists, row is the index, cell is the list in the loop
        for x, row in enumerate(zip(alphabet, self.board)):
            # there are two items in the list,
            # row[0] is the alphabet character, row[1] is the board row
            # the character can be printed as is
            # the board list must be joined as a string
            print(
                f'{row[0]}', ' '.join(x for x in row[1])
            )


def game_logo():
    """
    Prints game logo and game name
    """
    battleship_logo = """
|    |    |
             )_)  )_)  )_)     *     *                 __/___
            )___))___))__*)               *      _____/______|
           )____)____)_____)\\           _______/_____\_______\_____ 
         _____|____|____|____\\\__       \              < < <       |
---------\                   /-----------\     < - - < - - < - - < |
  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^  ^^^^^ ^^^^^^^^^^
    ^^^^      ^^^^     ^^^    ^^      ^^^^      ^^^^     ^^^    ^^
         ^^^^      ^^^           ^^^        ^^^^      ^^^
"""

    print_out(battleship_logo)

    print("""
- - - - B A T T L E S H I P - - - - - - - - - - - - - - - - - - - - - - - -
 ######     #    ####### ####### #       #######  #####  #     # ### ######
 #     #   # #      #       #    #       #       #     # #     #  #  #     #
 #     #  #   #     #       #    #       #       #       #     #  #  #     #
 ######  #     #    #       #    #       #####    #####  #######  #  ######
 #     # #######    #       #    #       #             # #     #  #  #
 #     # #     #    #       #    #       #       #     # #     #  #  #
 ######  #     #    #       #    ####### #######  #####  #     # ### #
- - - - - - - - - - - - - - - - - - - - - - - - - - - - ObiOne84 - - - - -
""")


size = 5
game_logo()
board_one = GameBoard(size)
board_one.print_board()
