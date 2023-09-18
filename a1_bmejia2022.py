# Name: Brenda Mejia
# Date: 9/18/23
# Assignment #: 1


import copy
import random
import math

# min-max ID's
MIN = -1
MAX = 1
INFINITY_POSITIVE = math.inf
INFINITY_NEGATIVE = -math.inf

# Global variables that represent both Human and AI players
PLAYER_HUMAN = 'X'
PLAYER_AI = 'O'
EMPTY_SLOT = ' '
WINNING_COUNT = 3

class Move:
    def __init__(self, move=0, value=0):
        self.move = move
        self.value = value

# A move will be chosen depending on the depth
def choose_move(connect, depth):
    move_result = False
    # A move will be searched until a valid one is possible
    while move_result is False:
        move_result = minmax(connect, depth, MAX, 0, INFINITY_NEGATIVE, INFINITY_POSITIVE).move
    return move_result

# minmax algorithm will help with picking the next best move
def minmax(connect, depth, min_or_max, move, alpha, beta):
    current_score = connect.get_score_for_ai()
    current_is_board_full = connect.is_board_full()

    # default move will be returned if current conditions require it
    if current_score != 0 or current_is_board_full or depth == 0:
        return Move(move, current_score)

    best_score = INFINITY_NEGATIVE * min_or_max
    best_max_move = -1

    # In this specific board size the possible moves would be from 0 - 8
    moves = random.sample(range(0, 9), 9)
    for position in moves:
        neighbor = copy.deepcopy(connect)
        move_outcome = neighbor.play_move(str(position))
        if move_outcome:
            # Recursively call minmax for the next state after playing a move
            best = minmax(neighbor, depth - 1, min_or_max * -1, str(position), alpha, beta)

            # Update the best score and best move, ignore irrelevant scores using alpha beta pruning
            if (min_or_max == MAX and best.value > best_score) or (min_or_max == MIN and best.value < best_score):
                best_score = best.value
                best_max_move = best.move
                if best_score >= alpha:
                    alpha = best_score
                if best_score <= beta:
                    beta = best_score
            if alpha >= beta:
                break
    return Move(best_max_move, best_score)

# A dictionary with human player as -1, and AI player as 1
PLAYERS = {PLAYER_HUMAN: -1,
           PLAYER_AI: 1}

# List that represents the values initially on the board
# It will help with determining if the position is available
values = ['0','1','2','3','4','5','6','7','8']
# Class that will represent a game of Tic Tac Toe
class TicTacToe:

    def __init__(self,board_size_x=3, board_size_y=3):
        self.board_size_x = board_size_x
        self.board_size_y = board_size_y
        self.player_turn = PLAYERS[PLAYER_HUMAN]
        self.board = self.generate_board(board_size_x,board_size_y)
        # print(type(self.board))
        # print(self.board)

    # Generate initial board that contains position numbers
    def generate_board(self,board_size_x, board_size_y):
        board = []
        row = []
        i = 0
        for y in range(0, board_size_y):
            for x in range(0, board_size_x):
                row.append(str(i))
                i += 1
            board.append(row)
            row = []
        return board
    
    # Print the board in the console
    def print_board(self,initial=False):
        result = ''
        if initial is True:
            for row in self.board:
                for char in row:
                    result += '| ' + char + ' '
                result += '|\n'
        else:
            for row in self.board:
                for char in row:
                    if char in values:
                        result += '|   '
                    else:
                        result += '| ' + char + ' '
                result += '|\n'
        print(result)

    # Determine if the board is full
    def is_board_full(self):
        for row in self.board:
            for char in row:
                if char in values:
                    return False
        return True
    
    # Reset board after each finished game
    def reset_board(self):
        self.board = self.generate_board(self.board_size_x,self.board_size_y)

    # check to see if there is a winner
    def has_winner(self):
        if self.has_a_row(PLAYER_HUMAN, WINNING_COUNT):
            return "X won!"
        elif self.has_a_row(PLAYER_AI, WINNING_COUNT):
            return "O won!"
        return 0
    
    # check to see if any player has a complete row
    def has_a_row(self, player, row_count):
        for x in range(self.board_size_x):
            for y in range(self.board_size_y):
                if self.has_full_row(player, row_count, x, y, 1, 0): # check horizontal row
                    return True
                elif self.has_full_row(player, row_count, x, y, 0, 1):  # check vertical row
                    return True
                elif self.has_full_row(player, row_count, x, y, 1, 1): # check diagonal row
                    return True
        return False
    
    # check to see if any player has completed a full row
    def has_full_row(self, player, row_count, x, y, offset_x, offset_y):
        total = 0
        for i in range(row_count):
            target_x = x + (i * offset_x)
            target_y = y + (i * offset_y)
            if self.bound_check(target_x,target_y):
                if self.board[target_y][target_x] == player:
                    total += 1
        if total == row_count:
            return True
        return False
             
    # Verify that a specific x,y position is within the bounds of the current board
    def bound_check(self, x, y):
        if 0 <= x < self.board_size_x and 0 <= y < self.board_size_y:
            return True
        return False
    
    # Determine if position is taken
    def position_taken(self,position):
        for row in self.board:
            if position in row:
                return False
        return True

    # Play the move if a valid position was given
    def play_move(self, position):
        if 0 <= int(position) <= 8:
            if not self.position_taken(position):
                for i, row in enumerate(self.board):
                    # Determine if position is within this row
                    if position in row:
                        # Position was found within this row so index of where that value is within this row
                        # should be calculated using index() function
                        j = row.index(position)
                        # Determine who is making this move
                        if self.player_turn == PLAYERS[PLAYER_HUMAN]:
                            self.board[i][j] = PLAYER_HUMAN
                        else:
                            self.board[i][j] = PLAYER_AI
                        self.player_turn *= -1
                        return True
            return False
        return False
    
    # Determine score for AI. Score is dependent on which player has a complete row
    def get_score_for_ai(self):
        if self.has_a_row(PLAYER_HUMAN, 4):
            return -10
        if self.has_a_row(PLAYER_AI, 4):
            return 10
        return 0
                            
                        
# Set initial variables before game play
SEARCH_DEPTH = 10
continue_play = 'Y'
# Message explaining purpose of application
print("""
        Welcome to Tic Tac Toe with AI. The purpose of this app is to play against AI with
        and implementation of the minmax algorithm, with additional alpha-beta pruning.
        """)
# Instatiate a game of TicTacToe
game = TicTacToe()
# Begin game and as long as user wishes to continue playing the game will continue
while continue_play == 'Y':
    game.print_board(True)
    while game.has_winner() == 0:
        # Player makes a move
        player_move_result = False
        while player_move_result is False:
            player_move = input("X's turn. Input move (0-8): ")
            player_move_result = game.play_move(player_move)
        game.print_board()
        if game.has_winner() != 0:
            print(game.has_winner())
            break

        # AI makes a move
        ai_move = str(choose_move(game,SEARCH_DEPTH))
        print(f"O makes a move to square {ai_move}")
        game.play_move(ai_move)
        game.print_board()
        if game.has_winner() != 0:
            print(game.has_winner())
            break
    # Board to be reset after the end of a complete game play
    game.reset_board()
    continue_play = input("Do you want to play another round?\nEnter 'Y' for yes or 'N' for no ").upper()
    print("\n")



