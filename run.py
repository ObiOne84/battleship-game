import time
import sys
from random import randint


user_name = ""
size = 5
num_ships = size


def print_out(data):
    """
    The function will display text as it typed in real
    time rather than dispaly all message at once
    """
    for letter in data:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)


def print_pause(data):
    """
    The function will print text very slowly
    ather than dispaly all message at once
    """
    for letter in data:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(1)


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

    def add_ships(self):
        """
        Function allows to add ship to the board, by allowing
        user to choose own location of ships
        Function calls user_coordinations function to allocate the ships.
        """

        append_user_ship(self)

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
            random_shot(self, data, shots, name)
        else:
            user_shots(self, data, shots, name)


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
Welcome to the game BATTLESHIP\n
Battleship is a war-themed game for two players in which the opponents
try to guess the location of their opponent's warships and sink them. \n
You can choose between three game levels:
Beginner - This will build a 5 x 5 grid and allow you to choose
the location of 5 ships on the board. Additionally, you will receive
25 bullets.
Intermediate - the game will take place on a 10 x 10 grid with 10 available
ships and 75 bullets.
Expert - the game takes place on the 10 x 10 grid but, on this level
the number of available shots is limited to 50, and you must destroy 20 ships.
  S - represent the ship on the game board.
  0 - indicates missed shot.
  X - illustrates hit ship.
  You can leave the game during the battle by entering the command 'STOP.'
  into the coordination input field. The game will reload.\n
"""
    print_out(message)


def start_game():
    """
    Function prompts user to start the game, collect user's input
    and provides feedback when incorrect.
    """
    while True:
        decision = input("Please choose Y/N:\n").upper()
        if validate_decision(decision):
            print_out(f"Thank you, your choice is {decision}\n")
            break
    return decision


def validate_decision(value):
    """
    Function validates user decision, when user must choose between Y and N
    """
    try:
        if value != "N":
            if value != "Y":
                print(f"{value} is not a valid option.")
                raise ValueError
    except ValueError:
        print_out("Please choose again!\n")
        return False
    return True


def collect_user_name():
    """
    The function will collect user name
    """

    while True:
        print_out("""
Please choose your username. The username should contain minimum 3 characters
and a maximum of 10. It must only have alphabetic letters from range a to z,
upper, lower case, or a mix of both. Special characters are not allowed.
        """)

        user_name = input(f"Please provide your username:\n")

        if validate_user_name(user_name):
            print_out(
                f"Thank you {user_name}. Welcome to BATTLESHIP GAME!\n"
                )
            return user_name


def validate_user_name(name):
    """
    Functions validates user input to ensure username
    is between 3 to 10 characters
    """
    try:
        if len(name) < 3:
            print(f"{name} has {len(name)} charactes.")
            raise ValueError
        if len(name) > 10:
            print(f"{name} has {len(name)} characters.")
            raise ValueError
        if name.isalpha() is False:
            print(f"{name} must contain only alphabetic letters.")
            raise ValueError

    except ValueError:
        print_out(
            f"The username is not valid!\n"
        )
        return False
    return True


def game_level(user_name):
    """
    function checks user input and defines the size of the game board
    need to add validation here
    """

    while True:
        message = """
Please choose your gaming experience by choosing one of three options:
-- choose 'b' for beginners to set up a 5 x 5 grid, 25 shots and 5 ships.
-- choose 'i' for intermediate for a 10 x 10 grid, 75 shots, and 10 ships.
-- or choose 'e' for an expert for a 10 x 10 grid, 50 shots, and 20 ships.\n
    """
        print_out(message)

        user_input = input(f"Please indicate your game experience:\n")
        user_experience = user_input.lower()

        try:
            if user_experience == "b":
                print_out(f"""
Thank you {user_name}. Your game experience level is a beginner.\n
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
                return 15
            else:
                raise ValueError
        except ValueError:
            print_out(f"""
Invalid data. You provided '{user_experience}';
this is not a recognised value.\n
            """)


def random_ship_location(self):
    """
    Function randomly allocates ships on the board,
    for the Computer, the ships are added to the list, but not on the board
    for the user, the ships will be displayed on the board.
    """

    b = 0
    while b < self.num_ships:
        x = randint(0, size - 1)
        y = randint(0, size - 1)
        pair = (x, y)
        if pair not in self.ships:
            self.ships.append(pair)
            # don't forget to remove line below to hide computer ships
            # self.board[x][y] = "S"
            if self.name != "Computer":
                self.board[x][y] = "S"
        else:
            continue
        b += 1


def player_ship_coordinates():
    """
    Function collects ships coordinates from the user as a string
    """

    while True:
        print_out("""
Please enter coordinates in format 'A1', where 'A' represents the row
name, and '1' indicates the column number. Only enter the coordinates displayed
on your Battleship game board.
        """)
        ship_loc = input("Please enter your coordinates:\n")

        if validate_coordinates(ship_loc, size):
            print_out(f"Your coordinates are: '{ship_loc.upper()}'!\n")
            break
    return ship_loc.upper()


def validate_coordinates(values, size):
    """
    Function validates users ships coordinates
    and user shot coordinates
    """
    alphabet = ["ABCDEFGHIJKLMNOPRTQUXYZ"]
    alphabet = ''.join(alphabet[:size])

    try:
        if values.upper() == "STOP":
            print_out("Sorry to see you go!\n")
            print_out("Thank you for playing BATTLESHIP!\n")
            print(" \n" * 3)
            main()
        if len(values) > 3:
            print("The coordinates can have a maximum of 3 characters.")
            raise ValueError
        if len(values) == 3 and int(values[1] + values[2]) != 10:
            print(f"{values[1] + values[2]} is not a column number.")
            print(f"Please choose a number between 1 and {size}")
            raise ValueError
        if len(values) < 2:
            print("The coordinates must have a minimum of 2 characters.")
            raise ValueError
        if values[0].upper() not in ''.join(alphabet[:size]):
            print(f"{values[0].upper()} is not a row name on the gameboard")
            raise ValueError
        if values[1].isnumeric() is False:
            print(f" '{values[1]}' is not a column number")
            raise ValueError
        if int(values[1]) > size:
            print(f"{values[1]} is not a column number.")
            print(f"Please choose a number between 1 and {size}")
            raise ValueError
        if int(values[1]) == 0:
            print(f"{values[1]} is not a column number.")
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
    from user input
    """
    if len(data) == 3:
        y = int(data[1] + data[2]) - 1
        return y
    else:
        y = int(data[1]) - 1
        return y


def append_user_ship(self):
    """
    Function appends user ships to the game board
    only if the position is not occupied by ship
    """

    while True:
        coordinates = player_ship_coordinates()
        x = return_x_value(coordinates)
        y = return_y_value(coordinates)
        pair = (x, y)
        if pair not in self.ships:
            self.board[x][y] = "S"
            self.ships.append(pair)
            break
        else:
            print("You already placed ship here")
            continue
    return True


def user_ships_option():
    """
    Function allow user to choose location of the place or
    to randomly allocated ships on the board
    """

    print_out("""
You can choose the position of the ships on the board. If you wish to choose
the location of your ships on the board, choose "Y"  for YES or "N" for NO;
if you choose NO, ships will be randomly allocated on the board.\n
    """)
    while True:
        answer = input(f"Would you like to place ships on the board Y/N:\n")
        decision = answer.upper()

        if decision == "Y":
            print_out("Great, you can choose ship locations now.\n")
            break
        elif decision == "N":
            print_out("Great, your ships will be randomly placed.\n")
            break
        else:
            print(f"{answer} is not a valid option. Try again!\n")
            continue
    return decision


def user_shots(self, data, shots, name):
    """
    Function records user shots, and checks against board
    reduce the number of shots after each round
    and ships after each hit
    """

    while True:
        coordinates = player_ship_coordinates()
        x = return_x_value(coordinates)
        y = return_y_value(coordinates)
        pair = (x, y)

        if pair in self.guesses:
            print_out(f"{name}, you already shot at {coordinates}!\n")
        else:
            if pair not in data.ships:
                data.board[x][y] = "0"
                print_out(f"Sorry {name} that's a miss!\n")
                self.guesses.append(pair)
                self.shots -= 1
                break
            else:
                data.board[x][y] = "X"
                print_out(f"Well done {name}, you just HIT a ship!\n")
                self.guesses.append(pair)
                data.num_ships -= 1
                self.shots -= 1
                break
    return True


def random_shot(self, data, shots, name):
    """
    Function randomly shots at the ships, and validates the shot
    if computer shot location, the function calls for another shot
    """

    alphabet = ["ABCDEFGHIJKLMNOPRTQUXYZ"]
    alphabet = ''.join(alphabet[:size])
    numbers = [*range(1, size + 1)]

    while True:
        x = randint(0, size - 1)
        y = randint(0, size - 1)
        pair = (x, y)
        coordinates = alphabet[x] + str(numbers[y])

        if pair in self.guesses:
            continue
        else:
            if pair not in data.ships:
                data.board[x][y] = "0"
                print_out(f"{name} gueesed {coordinates}\n")
                print_out(f"{name} missed!\n")
                self.guesses.append(pair)
                self.shots -= 1
                break
            else:
                data.board[x][y] = "X"
                print_out(f"{name} gueesed {coordinates}\n")
                print_out(f"{name}, that's a HIT\n")
                self.guesses.append(pair)
                data.num_ships -= 1
                self.shots -= 1
                break
    return True


def game_battle(board_one, board_two, shots, user_name):
    """
    Function controls the game battle, and identifies winner
    and looser, it prints the boards after each round, round number,
    number of ships and shots lefts.
    """

    b = 1
    while board_two.num_ships > 0:
        if board_one.shots > 0:
            if board_one.num_ships > 0:
                print_out(
                    f"----------------Round {b}-----------------\n"
                )
                print("-" * 60)
                print(f"\t {user_name}", end="")
                print("\t\t\t Computer")
                print(f"  Shots: {board_one.shots}", end="")
                print(f"\t\t\t {board_two.shots}")
                print(f"  Ships: {board_one.num_ships}", end="")
                print(f"\t\t\t {board_two.num_ships}")
                print("-" * 60)
                print("=" * 60)
                print(f"{board_two.name}'s Board")
                board_two.print_board(size)
                print("=" * 60)
                board_one.guess(board_two, shots, name=user_name)
                print("=" * 60)
                print_out("          \n")
                print(f"{board_two.name}'s Board")
                board_two.print_board(size)
                print("\n")
                print("=" * 60)
                board_two.guess(board_one, shots, "Computer")
                print("=" * 60)
                print(f"{board_one.name}'s Board")
                board_one.print_board(size)
                print("=" * 60)
                print_out(f"-------------End of round {b}-------------\n")
                print("=" * 60)
                print("\n")
                b += 1
            else:
                print_out(f"Sorry {user_name}. All your ships are sunk!\n")
                print("""
     #####     #    #     # #######
    #     #   # #   ##   ## #
    #        #   #  # # # # #
    #  #### #     # #  #  # #####
    #     # ####### #     # #
    #     # #     # #     # #
     #####  #     # #     # #######

    ####### #     # ####### ######  ###
    #     # #     # #       #     # ###
    #     # #     # #       #     # ###
    #     # #     # #####   ######   #
    #     #  #   #  #       #   #
    #     #   # #   #       #    #  ###
    #######    #    ####### #     # ###
                    """)
                break
        else:
            print_out(f"Sorry {user_name}. You don't have any bullets!\n")
            print("""
     #####     #    #     # #######
    #     #   # #   ##   ## #
    #        #   #  # # # # #
    #  #### #     # #  #  # #####
    #     # ####### #     # #
    #     # #     # #     # #
     #####  #     # #     # #######

    ####### #     # ####### ######  ###
    #     # #     # #       #     # ###
    #     # #     # #       #     # ###
    #     # #     # #####   ######   #
    #     #  #   #  #       #   #
    #     #   # #   #       #    #  ###
    #######    #    ####### #     # ###
                    """)
            break
    else:
        print_out(f"Congratulations {user_name}! You destroyed all ships!\n")
        print("""
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMWXK00000000KXNWMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMXo'....     ....:OMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMWkdKWMK,              .xWMNkdKMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMX: .:ol.               :dl, .kMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMN: ,ooc.               ;loc..OMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMWo.oWMX:              .OMMO',KMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMk.cNMNc              '0MMk.cNMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMX:;KMWo              ,KMNl.kMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMWk,lNMx.             :XMO,cNMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMWx;oX0'             dNk;lXMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMW0ood,            .ldlkNMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMWX0d.           cOKNMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMWk.         cXMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMWO:.     'dNMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMWO;. .dXMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMK:  .kWMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMO;.oWMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMNKOl..;kKNWMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMW0l,.      .':xNMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMWOc;,''...',;:dXMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMWWNNNNNNWWMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMM #    #  ###  #   #  #      # @ #    #   MMMMMMMMMM
    MMMMMMMMM  #  #  #   # #   #  #  #   # # # #  #   MMMMMMMMMM
    MMMMMMMMM   #    #   # #   #   # # #   # #  # #   MMMMMMMMMM
    MMMMMMMMM   #     ###   ###     # #    # #    #   MMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
    MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n
        """)


def play_game(user_name):
    """
    Function calls out other functions to enable user to play the game
    it sets the game parameters like board size, num_ships, user_name
    allows user to place the ships on the board, provides feedback to
    users actions.
    """

    global size
    difficulity_level = game_level(user_name)
    size = 0
    num_ships = 0
    shots = 0
    if difficulity_level == 5:
        size = 5
        num_ships = 5
        shots = 25
    elif difficulity_level == 10:
        size = 10
        num_ships = 10
        shots = 75
    else:
        size = 10
        num_ships = 20
        shots = 50

    user_board = GameBoard(size, num_ships, shots, name=user_name)
    computer_board = GameBoard(size, num_ships, shots, "Computer")
    print_out("Please wait! We are setting your game board.\n")
    print_pause("." * 8)
    print_out("10%")
    print_out("." * 16)
    print_pause("." * 8)
    print_out("50%")
    print_pause("." * 4)
    print_out("." * 28)
    print_pause("100%\n")
    print_out("Board set up: Completed!\n")

    print("")
    print("=" * 60)
    print(f"{user_board.name}'s Board")
    user_board.print_board(size)
    print("=" * 60)

    ship_location = user_ships_option()
    if ship_location == "Y":
        while len(user_board.ships) < num_ships:
            user_board.add_ships()
            print("=" * 60)
            print(f" {user_name}'s Game Board")
            user_board.print_board(size)
            print("=" * 60)
            print(f"""
Well done, you placed {len(user_board.ships)} out of {num_ships} ships.\n
                """)
            print("=" * 60)
    else:
        user_board.add_random_ships()
        print("=" * 60)
        print(f" {user_name}'s Game Board")
        user_board.print_board(size)
        print("=" * 60)

    print_out(f"""
Great {user_name}, you placed all {len(user_board.ships)} ships on the board.\n
        """)

    computer_board.add_random_ships()
    print("\n")

    game_battle(user_board, computer_board, shots, user_name)

    print_out(f"{user_name} would you like to continue the game?\n")
    decision = start_game()

    if decision == "Y":
        play_game(user_name)
    else:
        print_out(f"Thank you {user_name} for playing BATTLESHIP GAME!\n")
        print(" \n" * 4)


def main():
    """
    Functions controls entire game, by calling all functions
    """
    while True:
        # game_logo()
        # game_intro()
        print("Would you like to start the game?")
        print_out("Choose 'Y' to start the game or 'N' to leave now.\n")
        decision = start_game()
        if decision == "Y":
            user_name = collect_user_name()
            play_game(user_name)
        else:
            print_out("Thank you for playing BATTLESHIP GAME!\n")


main()
