# CSC6003 Second Coding Project - Battleship Game
# Kevin Cyr

import random

# Capitalized these because they are constants - 
# best practice taken from Python Crash Course by Eric Matthes
BOARD_SIZE = 10
NUM_SHIPS = 5

# drawBoard function begins - create 10x10 board 
# Creating a player 'visible' board

def drawBoard(board):

    print("  ", end="")
    for col in range(BOARD_SIZE):
        print(col, end=" ")
    print()

    for row in range(BOARD_SIZE):
        print(row, end=" ")
        for col in range(BOARD_SIZE):
            print(board[row][col], end=" ")
        print()


# setupBoard function begings - set up board and place ships randomly 
# creating a player board and hidden board to fix issue of S being visible in earlier code examples

def setupBoard():
    
    hidden_board = [['.' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    player_board = [['.' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    ships_placed = 0
    while ships_placed < NUM_SHIPS:
        row = random.randint(0, BOARD_SIZE - 1)
        col = random.randint(0, BOARD_SIZE - 1)

        if hidden_board[row][col] == '.':
            hidden_board[row][col] = 'S'
            ships_placed += 1

    return hidden_board, player_board


# isGameOver function begins - checks if all ships have been sunk and ends game
# Returns True if all ships are hit

def isGameOver(hidden_board):

    for row in hidden_board:
        if 'S' in row:
            return False
    return True


# checkHitOrMiss function begins - updates based on user input to do the following
# if ship is hit update the board to an X and return 'HIT'#
# if square already sunk return 'HIT'#
# otherwise the board should update to O and return 'MISS'#

def checkHitOrMiss(hidden_board, player_board, row, col):
    
    if hidden_board[row][col] == 'S':
        hidden_board[row][col] = 'X'
        player_board[row][col] = 'X'
        return "HIT"
    elif player_board[row][col] == 'X':
        return "HIT"
    else:
        player_board[row][col] = 'O'
        return "MISS"


# main function begins - Battleship game starts

def main():
    hidden_board, player_board = setupBoard()

    print("Welcome to Battleship!")
    print("There are five hidden ships. Good luck!\n")

    while not isGameOver(hidden_board):
        drawBoard(player_board)

        row = int(input("Enter row (the #'s up and down) between 0-9: "))
        col = int(input("Enter column (the #'s left and right) between 0-9: "))

        if row < 0 or row >= BOARD_SIZE or col < 0 or col >= BOARD_SIZE:
            print("Invalid coordinates. Please enter an integer between 0-9.\n")
            continue

        result = checkHitOrMiss(hidden_board, player_board, row, col)
        print(result, "\n")

    
    drawBoard(player_board)
    print("Game Over!")


main()