# Global variables that represent both Human and AI players
PLAYER_HUMAN = 'X'
PLAYER_AI = 'O'
EMPTY_SLOT = ' '
WINNING_COUNT = 3

# A dictionary with human player as -1, and AI player as 1
PLAYERS = {PLAYER_HUMAN: -1,
           PLAYER_AI: 1}


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
        values = ['0','1','2','3','4','5','6','7','8']
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
                            
                        


game = TicTacToe()
game.print_board(True)
while game.has_winner() == 0:
    player_move = input("X's turn. Input move (0-8): ")
    game.play_move(player_move)
    game.print_board()
    print(game.has_winner())

    # AI makes a move



