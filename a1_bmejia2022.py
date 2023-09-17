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
        print(self.board)

    # Generate initial board that contains position numbers
    def generate_board(self,board_size_x, board_size_y):
        board = []
        result = ''
        i = 0
        for y in range(0, board_size_y):
            for x in range(0, board_size_x):
                result += str(i)
                i += 1
            board.append(result)
            result = ''
        return board
    
    # Print the board in the console
    def print_board(self,initial=True):
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
    



game = TicTacToe()
game.print_board(True)