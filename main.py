import pygame

class Player:
    # to be completed
    pass


class Board:
    def __init__(self):
        self.board = {'7': ' ', '8': ' ', '9': ' ',
                      '4': ' ', '5': ' ', '6': ' ',
                      '1': ' ', '2': ' ', '3': ' '}


    def display_board(self):
        print(self.board['7'] + '|' + self.board['8'] + '|' + self.board['9'])
        print('-+-+-')
        print(self.board['4'] + '|' +            self.board['5'] + '|' + self.board['6'])
        print('-+-+-')
        print(self.board['1'] + '|' + self.board['2'] + '|' + self.board['3'])


    def update_board(self, position, symbol):
        self.board[position] = symbol


    def is_position_available(self, position):
        # to be completed




class GameState:
    def __init__(self):
        self.board = Board()
        # to be completed


    def switch_player(self):
        # to be completed


    def check_winner(self):
        b = self.board.board
        winning_conditions = [
            (b['7'], b['8'], b['9']),  # across the top
            (b['4'], b['5'], b['6']),  # across the middle
            (b['1'], b['2'], b['3']),  # across the bottom
            (b['7'], b['4'], b['1']),  # down the left side
            (b['8'], b['5'], b['2']),  # down the middle
            (b['9'], b['6'], b['3']),  # down the right side
            (b['7'], b['5'], b['3']),  # diagonal
            (b['1'], b['5'], b['9'])   # diagonal
        ]
        for condition in winning_conditions:
            if condition[0] == condition[1] == condition[2] != ' ':
                self.game_over = True
                return True
        return False


    def check_tie(self):
        # to be completed


class Game:
    def __init__(self):
        self.game_state = GameState()
