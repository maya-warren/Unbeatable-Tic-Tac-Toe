"""
File Name: comp.py
Author: Maya Warren
Description: Computer moves for the tic tac toe game
Last Date Changed: 04/20/2020
"""

def getbestMove(board, player, computer):
    """
    This method checks for every open space and computes
    the best move for computer.

    :param board: playing board - dictionary
    :param player: player's marker
    :param computer: computer's marker
    :return: best possible move
    """
    bestScore = -100
    bestMove = -1

    for i in range(1, len(board) + 1):
        if board[i] == ' ':
            # make a move for the computer
            board[i] = computer

            # find value for potential move
            curScore = valueOfBoard(board, False, 0, player, computer)
            # clear move
            board[i] = ' '

            if curScore > bestScore:
                bestMove = i
                bestScore = curScore

    return bestMove


# minimax algorithn
def valueOfBoard(board, compTurn, depth, player, computer):
    """
    This method checks for open position on the board and gives it a score
     for the possible outcomes

    :param compTurn: boolean - is it the computer's turn
    :param board: playing board - dictionary
    :param depth: level of game play value board is looking at
    :param player: player's marker
    :param computer: computer's marker
    :return: best score 10 - for a win, -10 for a loss, 0 for a tie
    """
    tally = win(board)
    score = interpretWin(tally, player, computer)

    # return score if is 10 best computer has won
    if score == 10:
        return score

    # return score if is -10 player has won
    if score == -10:
        return score

    # return zero if there are no possible moves left
    if not isMoveLeft(board):
        return 0

    if compTurn:  # computers turn
        best = -100
        # make sure that current place is empty
        for i in range(1, len(board) + 1):
            if board[i] == ' ':
                # make the computer's move
                board[i] = computer

                # recursively call valueOfBoard to find the next best possible move
                best = max(best, valueOfBoard(board, not compTurn, depth + 1, player, computer))

                # set space back to empty
                board[i] = ' '

        return best
    else:  # players turn
        best = 100
        # Checks that current  space is empty
        for i in range(1, len(board) + 1):
            if board[i] == ' ':
                # make the player's move
                board[i] = player

                # recursively call valueOfBoard to find the next best possible move
                best = min(best, valueOfBoard(board, not compTurn, depth + 1, player, computer))

                # set space back to empty
                board[i] = ' '

        return best


def isMoveLeft(board):
    """
    Function checks to see if there are any possible moves left on the board.

    :param board:  playing board - dictionary
    :return: True if there is an empty cell; False if the board is full
    """
    # loop iterates through playing board
    for i in range(1, len(board) + 1):
        if board[i] == ' ':
            return True
    return False


def interpretWin(tally, player, computer):
    """
    Takes variable returned from function win and then returns if it is a win
    for the computer or a win for the player

    :param tally: return value from function win
    :param player: marker player chose
    :param computer: marker computer chose
    :return: either positive in computer won, negative if player won, and zero
            if no one has won
    """
    if tally == computer:
        return 10
    elif tally == player:
        return -10
    else:
        return 0


def win(board):
    """
    Checks all possible win combinations and returns true if either the user or the
    computer has won

    :param board: playing board - dictionary
    :return: True if a player has three in row; False if no one has won yet
    """
    # COLUMNS
    if board[7] == board[4] == board[1] != ' ':  # first column down
        return board[7]
    elif board[8] == board[5] == board[2] != ' ':  # second column down
        return board[8]
    elif board[9] == board[6] == board[3] != ' ':  # third column down
        return board[9]

    # ROWS
    if board[7] == board[8] == board[9] != ' ':  # first row across
        return board[7]
    elif board[4] == board[5] == board[6] != ' ':  # second row across
        return board[4]
    elif board[1] == board[2] == board[3] != ' ':  # third row across
        return board[1]

    # DIAGONALS
    if board[7] == board[5] == board[3] != ' ':  # diagonal staring on left
        return board[7]
    elif board[9] == board[5] == board[1] != ' ':  # diagonal starting on right
        return board[9]

    # else no winner
    return "No"
