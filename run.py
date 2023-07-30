import time
import sys
from random import randint


# ----variables for testing --------------------------------------
user_name = ""
size = 5
shots = size * 5
num_ships = size
computer_guess = []
ships = []
guesses = []
# ----------------------------------------------------------------


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

    def __init__(self, size, num_ships, shots, name):
        self.size = size
        self.num_ships = num_ships
        self.shots = shots
        self.name = name
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

    def add_ships(self, x, y):
        """
        Function allows to add ship to the board, by allowing
        user to choose own location of ships
        Function calls user_coordinations function to allocate the ships.
        """

        append_user_ship(self, x, y)

    def add_random_ships(self):
        """
        Function randomly allocates ships on the board
        """

        random_ship_location(self)

    def guess(self, data, shots, name):
        """
        Method collect computer and user guesses and
        append them to the guesses list. It calls helper functions
        to allow choose location by user, and randomly guess by cpu
        """

        if name == "Computer":
            random_shot(self, data, shots)
        else:
            user_shots(self, data, shots)


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

        user_name = input(f"Please provide your username: ")

        if validate_user_name(user_name):
            print_out(
                f"Thank you {user_name}. Welocome to BATTLESHIP GAME!\n"
                )
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
-- choose 'b' for beginner
-- choose 'i' for intermediate
-- or  choose 'e' for expert.\n
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


def random_ship_location(self):
    """
    Function randomly allocates ships on the board
    """

    b = 0
    while b < self.num_ships:
        x = randint(0, size - 1)
        y = randint(0, size - 1)
        pair = (x, y)
        if self.board[x][y] == "-":
            self.board[x][y] = "@"
            self.ships.append(pair)
        else:
            continue
        b += 1


def player_ship_coordinates():
    """
    Function collects ships coordinates from the user as a string
    """

    while True:
        ship_loc = input("please enter ship location: ")

        if validate_coordinates(ship_loc):
            print("Great, you chose your ship location!")
            break
    return ship_loc.upper()


def validate_coordinates(values):
    """
    Function validates users ships coardinates
    """
    alphabet = ["ABCDEFGHIJKLMNOPRTQUXYZ"]
    alphabet = ''.join(alphabet[:size])

    try:
        if len(values) > 3:
            print("bad batch")
            raise ValueError
        if len(values) == 3 and int(values[1] + values[2]) != 10:
            print("incorrect value")
            raise ValueError
        if len(values) < 2:
            print("too short")
            raise ValueError
        if values[0].upper() not in ''.join(alphabet[:size]):
            print(f"{values[0].upper()} is not a column name on the gameboard")
            raise ValueError
        if values[1].isnumeric() is False:
            print(f" '{values[1]}' not a number")
            raise ValueError
        if int(values[1]) > size:
            print(f"{values[1]} is not a row number.")
            print(f"Please choose number between 1 and {size}")
            raise ValueError

    except ValueError:
        print(f"{values} is not a valid choice.")
        return False

    return True


def return_x_value(data):
    """
    Function return x coordinate for the ship or shot
    from user input
    """
    alphabet = ["ABCDEFGHIJKLMNOPRTQUXYZ"]
    alphabet = ''.join(alphabet[:size])

    if data[0] in ''.join(alphabet[:size]):
        x = alphabet.index(data[0])
        return x


def return_y_value(data):
    """
    Function return y coordinate for the ship or shot
    """
    if len(data) == 3:
        y = int(data[1] + data[2]) - 1
        return y
    else:
        y = int(data[1]) - 1
        return y


def append_user_ship(self, x, y):
    """
    Function appends user ships to the game board
    only if the position is not occupied by ship
    """

    if self.board[x][y] == "-":
        self.board[x][y] = "@"
        pair = (x, y)
        self.ships.append(pair)
    elif self.board[x][y] == "@":
        print("You already placed ship here")


def user_ships_option():
    """
    Function allow user to choose location of the place or
    to randomly allocated ships on the board
    """

    print_out("""
You can choose the position of the ships on the board. If you wish to choose
location of your ships on the board choose "Y"  for YES or "N" for NO, if you
choose NO ships will be randomly allocated on the board.
    """)
    while True:
        answer = input(f"Would you like to place ships on the board Y/N: ")
        decision = answer.upper()

        if decision == "Y":
            print_out("Great, you can choose ships locations now.\n")
            break
        elif decision == "N":
            print_out("Great, your ships will be randomly placed.\n")
            break
        else:
            print(f"{answer} is not a valid option. Try again!\n")
            continue
    return decision


def user_shots(self, data, shots):
    """
    Function record user shots, and check against board
    reduce the number of shots after each round
    and ships after each hit
    """

    while True:
        coordinates = player_ship_coordinates()
        x = return_x_value(coordinates)
        y = return_y_value(coordinates)
        pair = (x, y)

        if pair in self.guesses:
            print(f"You already shot at {coordinates}!")
        else:
            if pair not in data.ships:
                data.board[x][y] = "0"
                print("miss\n")
                self.guesses.append(pair)
                self.shots -= 1
                break
            else:
                data.board[x][y] = "X"
                print("Hit\n")
                self.guesses.append(pair)
                data.num_ships -= 1
                self.shots -= 1
                break
    return True


def random_shot(self, data, shots):
    """
    Function randomly shots at the ships
    """
    while True:
        x = randint(0, size - 1)
        y = randint(0, size - 1)
        pair = (x, y)

        if pair in self.guesses:
            continue
        else:
            if pair not in data.ships:
                data.board[x][y] = "0"
                print("miss\n")
                self.guesses.append(pair)
                self.shots -= 1
                break
            else:
                data.board[x][y] = "#"
                print("Hit\n")
                self.guesses.append(pair)
                data.num_ships -= 1
                self.shots -= 1
                break
    return True


def play_game():
    """
    Function calls out other functions to enable user to play the game
    it sets the game parameter like board size, num_ships, user_name
    """

    # game_logo()
    # game_intro()

    user_name = collect_user_name()
    size = game_level()
    num_ships = size
    shots = size * 5

    user_board = GameBoard(size, num_ships, shots, name=user_name)
    computer_board = GameBoard(size, num_ships, shots, "Computer")

    print(f"..." * size)
    print(f" {user_name}'s Game Board")
    user_board.print_board(size)
    print(f"..." * size)

    print(f"..." * size)
    print(f" Computer's Game Board")
    computer_board.print_board(size)
    print(f"..." * size)

    ship_location = user_ships_option()
    if ship_location == "Y":
        while len(user_board.ships) < num_ships:
            coordinates = player_ship_coordinates()
            x = return_x_value(coordinates)
            y = return_y_value(coordinates)
            user_board.add_ships(x, y)
            print(f"..." * size)
            print(f" {user_name}'s Game Board")
            user_board.print_board(size)
            print(f"..." * size)
            print(f"""
{user_name}, you placed {len(user_board.ships)} out of {num_ships} ships.
                """)
            print(f"..." * size)
    else:
        user_board.add_random_ships()
        print(f"..." * size)
        print(f" {user_name}'s Game Board")
        user_board.print_board(size)
        print(f"..." * size)

    print_out(f"""
Great {user_name}, you placed all {len(user_board.ships)} ships on the board.\n
        """)

# ----------------------Code Call-Out Zone------------------------

# game_logo()
# game_intro()

# define variables in this order
# user_name = collect_user_name()
# size = game_level()
# num_ships = size
# name = user_name
# x = 0

# print(f" {user_name}'s Game Board")
# print(f"..." * size)
# board_two = GameBoard(size, num_ships, shots, name)
# board_one = GameBoard(size, num_ships, shots, "Computer")
# board_two.print_board(size)
# board_two.add_random_ships()
# board_two.print_board(size)
# print("..." * size)
# while x < 100:
#     board_one.guess(board_two, shots, "Computer")
#     x += 1
# print("..." * 20)
# board_two.print_board(size)
# print("..." * 20)
# print(board_one.guesses)
# print(board_two. guesses)
# print(board_one.name)
# print(board_two.name)
# print(len(board_one.guesses))
# print(ships)
# print(computer_guess)
# print(num_ships)
# random_ship_location(board_one)
# board_one.print_board(size)
# random_shot(board_one)
# board_one.print_board(size)
# print(ships)
# print(computer_guess)
# print(num_ships)

# code for user to choose the ships
# while len(board_one.ships) < num_ships:
#     z = player_ship_coordinates()
#     x = return_x_value(z)
#     y = return_y_value(z)
#     board_one.add_ships(x, y)
#     board_one.print_board(size)
# while shots > 0 and num_ships > 0:
#     z = player_ship_coordinates()
#     x = return_x_value(z)
#     y = return_y_value(z)
#     user_shots(board_one, x, y)
#     board_one.print_board(size)
#     print(f"You have {shots} shots left.")
#     print(f"You still need to find {num_ships} ships.")
# else:
#     print("Game Over")


play_game()
