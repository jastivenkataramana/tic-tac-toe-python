from random import randrange


def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + board[0][0] + "   |   " + board[0][1] + "   |   " + board[0][2] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

    print("|       |       |       |")
    print("|   " + board[1][0] + "   |   " + board[1][1] + "   |   " + board[1][2] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

    print("|       |       |       |")
    print("|   " + board[2][0] + "   |   " + board[2][1] + "   |   " + board[2][2] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move: "))

            if move < 1 or move > 9:
                print("Please enter a number from 1 to 9.")
                continue

            row = (move - 1) // 3
            column = (move - 1) % 3

            if board[row][column] in ["X", "O"]:
                print("This square is already occupied.")
                continue

            board[row][column] = "O"
            break

        except ValueError:
            print("Please enter a valid number.")


def make_list_of_free_fields(board):
    free_fields = []

    for row in range(3):
        for column in range(3):
            if board[row][column].isdigit():
                free_fields.append((row, column))

    return free_fields


def victory_for(board, sign):
    for row in range(3):
        if board[row][0] == sign and board[row][1] == sign and board[row][2] == sign:
            return True

    for column in range(3):
        if board[0][column] == sign and board[1][column] == sign and board[2][column] == sign:
            return True

    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return True

    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return True

    return False


def draw_move(board):
    free_fields = make_list_of_free_fields(board)

    if free_fields:
        move = free_fields[randrange(len(free_fields))]
        board[move[0]][move[1]] = "X"


board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

board[1][1] = "X"

display_board(board)

while True:
    enter_move(board)
    display_board(board)

    if victory_for(board, "O"):
        print("You won!")
        break

    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break

    draw_move(board)
    display_board(board)

    if victory_for(board, "X"):
        print("Computer won!")
        break

    if not make_list_of_free_fields(board):
        print("It's a tie!")
        break
