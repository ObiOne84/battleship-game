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
        self.ships = []
        self.guesses = []

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

    message = ("""
     |    |    |                         *   *
             )_)  )_)  )_)           *            *
            )___))___))___)      *                   *__/_____
           )____)____)_____)*                    ____/_______\\
         _____|____|____|_____           _______/_____\\_______\\____
---------\\                   /-----------\\              < < <      |
  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^ ^^^^^ ^^^^^^^^^^^^^^^^^^^^^ ^^^^^ ^^^^^
     ^^^^      ^^^^     ^^^    ^^^   ^^^^      ^^^^     ^^^    ^^
         ^^^^      ^^^     ^^^^      ^^^         ^^^^      ^^^
    """)

    print_out(message)

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
        # global user_name
        user_name = input(f"Please provide your username: ")

        if validate_user_name(user_name):
            print("Great")
            return user_name


def validate_user_name(name):
    """
    Functions validates user input to ensure username
    is between 3 to 15 characters
    """
    try:
        if len(name) < 3:
            print(f"{name} has {len(name)} charactes.")
            raise ValueError
        if len(name) > 15:
            print(f"{name} has {len(name)} characters.")
            raise ValueError
    except ValueError:
        print(
            f"The username is not valid!\n"
        )
        return False
    return True


def game_level():
    """
    function checks user input and defines the size of the game board
    need to add validation here
    """

    while True:
        message = """
Please choose your gaming experience by choosing one of three options:
choose 'b' for beginner
choose 'i' for intermediate
or  choose 'e' for expert.\n
    """
        print_out(message)
        # global user_name
        # user_name = input(f"Please enter username: ")
        user_input = input(f"Please indicate your game experience: ")
        user_experience = user_input.lower()

        try:
            if user_experience == "b":
                print_out(f"""
Thank you {user_name}. Your game experience level is beginner.\n
                """)
                return 5
            elif user_experience == "i":
                print_out(f"""
Thank you {user_name}. Your game experience level is intermediate.\n
                """)
                return 10
            elif user_experience == "e":
                print_out(f"""
Thank you {user_name}. Your game experience level is expert.\n
                """)
                return 10
            else:
                raise ValueError
        except ValueError:
            print_out(f"""
Invalid data. You provided '{user_experience}', this is not recognised value.\n
            """)


def random_ship_location(data):
    """
    Function randomly allocates ships on the board
    """

    b = 0
    while b < num_ships:
        x = randint(0, size - 1)
        y = randint(0, size - 1)
        if data.board[x][y] == "-":
            data.board[x][y] = "@"
            pair = (x, y)
            # data.append(pair)
            ships.append(pair)
        else:
            continue
        b += 1


def player_choose_ships():
    """
    Function collects ships coordinates from the user as a string
    """

    ship_loc = input("please enter ship location: ")
    return ship_loc


# ----variables for testing --------------------------------------
user_name = "Adam"
size = 10
num_ships = size

# ----------------------------------------------------------------
# ----------------------Code Call-Out Zone------------------------

# game_logo()
# game_intro()

# define variables in this order
# user_name = collect_user_name()
# size = game_level()
# num_ships = size
ships = []
# print(f" {user_name}'s Game Board")
# print(f"..." * size)
# board_one = GameBoard(size)
# board_one.print_board(size)
# random_ship_location(board_one)
# board_one.print_board(size)
# print(ships)
player_choose_ships()
