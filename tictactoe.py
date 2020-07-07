"""
File Name: tictactoe.py
Author: Maya Warren
Description: This file contains the entire tic tac toe game
including instructions, game board, and call to computer moves
Last Date Changed: 04/20/2020
"""
import comp
import re
from time import sleep


def game():
    # welcome message and instructions
    print("Welcome to Tic Tac Toe. The rules are simple. Pick your player X or O, then use the "
          "numbers shown below to place your marker where you want. \nYou get the first "
          "move. Continue placing markers back and forth with the computer "
          "until you get three and a row and win. Good Luck.")

    # prints board to show the numbers that correspond with the spaces
    printExBoard()

    play = True
    while play:
        choice = input("Choose your marker X or O : ")

        while not inputMark(choice):
            choice = input("Choose your marker X or O : ")

        choice = choice.upper()

        # sets marker after player makes choice
        if choice == "X":
            player = "X"
            computer = "O"

        else:
            player = "O"
            computer = "X"

        # creates a dic that holds the board and all of the moves
        board = {7: ' ', 8: ' ', 9: ' ',
                 4: ' ', 5: ' ', 6: ' ',
                 1: ' ', 2: ' ', 3: ' '}

        winner = ""  # variable that holds the winner
        # beginning of game play - runs until there is a winner or board is full
        while comp.isMoveLeft(board):
            move = (input("Enter your move: "))

            # checks in player move is valid
            while not moveValid(board, move):
                move = (input("Move invalid. Enter your move: "))

            # convert move to integer
            numMove = int(move)

            # plays move for player
            board[numMove] = player

            # prints board after player move
            printBoard(board)

            # checks for a winner after move and if there is a move left
            winner = checkWin(board, computer, player)
            if winner != ' ' or not comp.isMoveLeft(board):
                break

            # gets best possible move for computer to make
            compMove = comp.getbestMove(board, player, computer)

            # plays computer move
            board[compMove] = computer

            # pause for computer to "think"
            print("Thinking......")
            sleep(1.5)

            # prints board after computer move
            printBoard(board)

            # checks for a winner after move
            winner = checkWin(board, computer, player)
            if winner != ' ':
                break

        # prints if player wins
        if winner == player:
            print("Congradulations, YOU WIN!")
        # prints if computer wins
        elif winner == computer:
            print("Sorry, better luck next time.")
        # prints if no one wins
        else:
            print("It's a Tie.")

        response = str(input("Do you want to play again? "))
        play = playAgain(response)


def playAgain(response):
    """
    Checks the user response to the prompt to play again and
    then return a boolean value to reflect the user's response

    :param response: user response to the prompt to play again
    :return: True if user wants to play again and false if they don't
    """
    if re.search("y(es)?", response, re.IGNORECASE):
        return True
    elif re.search("n(ope)?", response, re.IGNORECASE):
        return False
    else:
        return False


def checkWin(board, computer, player):
    """
    Checks to see if there is a win on the board and returns either the winner marker
    or a blank space

    :param board: playing board - dictionary
    :param computer: computer marker
    :param player: player maker
    :return: winning marker or blank space
    """
    if comp.win(board) == computer:
        return computer
    elif comp.win(board) == player:
        return player
    else:
        return ' '


def moveValid(board, move):
    """
     Takes user choice and verifies if it is valid ( A number between 1 - 9
     and a space that is not already taken )

    :param board: playing board - dictionary
    :param move: user inp
    :return:
    """
    # input needs to be one character
    if len(move) != 1:
        return False
    # input needs to be a number
    elif not move.isnumeric():
        return False
    numMove = int(move)
    # move needs to be in the board
    if numMove > 9 or numMove < 1:
        return False

    # User input (move) needs to be an open square on the board
    elif board[numMove] != ' ':
        return False
    return True


def printBoard(board):
    """
    Prints current playing board and updates with each turn

    :param board: playing board - dictionary
    """
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[1] + "|" + board[2] + "|" + board[3])


def printExBoard():
    """
    Prints a board with the keys showing to explain to the user
    how to play the game
    """
    print("7 | 8 | 9")
    print("- + - + -")
    print("4 | 5 | 6")
    print("- + - + -")
    print("1 | 2 | 3")


def inputMark(choice):
    """
    Takes user choice and verifies if it is valid ( one letter x or o not
    case sensitive)

    :param choice: user input on the console
    :return: True if input is valid; False if input is not valid
    """

    # user should only input one character
    if len(choice) != 1:
        return False

    # input needs to be a letter
    elif not choice.isalpha():
        return False

    # input should only be either x or o
    elif choice.upper() != "X" and choice.upper() != "O":
        return False
    return True


game()
