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

    def print_board(self, size):
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


def game_intro():
    """
    Prints welcome message and game rules
    """

    message = """
    Weclome to the game battleship \n
    Battleship is a war-themed game for two players in which the opponents
    try to guess the location of their opponent's warships and sink them. \n
    You can choose between three game levels:
    Beginner - which will build 5 x 5 grid and allow you to choose
    location of five ships on the board.
    Intermediate - the game will take place on 10 x 10 grid with ten available
    ships.
    Expert - on this level the number of available shots is limited to 50.\n
    """
    print_out(message)


def collect_user_name():
    """
    The function will collect user name
    """

    while True:
        print_out("""
Please choose your username. The username should contain minimum 3 characters,
and maximum 15.
        """)
        global user_name
        user_name = input(f"Please provide your username: ")

        try:
            if len(user_name) >= 3 and len(user_name) < 16:
                print(f"Thank you {user_name}.\n")
                return user_name

            else:
                raise ValueError(print(f"{user_name} is not valid."))

        except ValueError:
            print(f'You entered {user_name}.')
            print(f'{user_name} has {len(user_name)} characters.')
            print_out("""
Username should have minium 3 and maximum 15 charcters. Please try again.
            """)


user_name = collect_user_name()
size = 5
# game_logo()
# game_intro()

# collect_user_name()
print(user_name)

# board_one = GameBoard(size)
# board_one.print_board(size)
