"""
Class for creation of board
"""
from btree import BTree


class Board:
    """
    Generates the game board
    """
    def __init__(self):
        self.field = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.x_val = None
        self.y_val = None
        self.coord = None
        self.turn = None
        self.tree = BTree()

    def get_status(self):
        """
        Returns the status of game
        """
        for row in range(3):
            if self.field[row][0] == self.field[row][1] == self.field[row][2] and\
                    self.field[row][0] != ' ':
                return self.field[row][0]
        for col in range(3):
            if self.field[0][col] == self.field[1][col] == self.field[2][col] and\
                    self.field[0][col] != ' ':
                return self.field[0][row]
        """
        Checking the diagonal
        """
        if self.field[0][0] == self.field[1][1] == self.field[2][2] and self.field[0][0] != ' ':
            return self.field[0][0]
        if self.field[0][2] == self.field[1][1] == self.field[2][0] and self.field[0][2] != ' ':
            return self.field[0][2]
        for element in range(3):
            if self.field[element].count(' ') > 1:
                return 'continue'
        else:
            return 'draw'

    def get_number(self, coord):
        """
        Converts the coordinates to the number for a binary tree
        """
        if coord[0] == 0:
            coef = coord[0] + coord[1]
        elif coord[0] == 1:
            coef = coord[0] + coord[1] + 2
        else:
            coef = coord[0] + coord[1] + 4
        return int(coef)

    def is_position_taken(self, coord):
        """
        Returns bool if the position is taken
        """
        return self.field[coord] != ' '

    def make_move(self, position, turn):
        """
        Makes a move
        :param position: tuple
        :param turn: str
        :return: None
        """
        x_val = position[0]
        y_val = position[1]
        if x_val > 2 and y_val > 2 or self.field[x_val][y_val] != ' ':
            raise IndexError
        self.coord = position
        self.field[x_val][y_val] = turn
        self.turn = turn
        self.tree.add(self.get_number(self.coord))

    def make_computer_move(self):
        """
        Generates a move
        """
        best_score = -1000
        best_move = 0
        for row in range(3):
            for col in range(3):
                if self.field[row][col] == ' ':
                    self.field[row][col] = '0'
                    score = self.minimax(0, False)
                    self.field[row][col] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)
        self.tree.add(self.get_number(best_move))
        self.make_move(best_move, '0')
        return

    def __str__(self):
        result = ''
        for row in range(3):
            if row != 2:
                result += str(self.field[row]) + '\n'
            else:
                result += str(self.field[row])
        return result

    def minimax(self, depth, is_maximizing):
        """
        Implementation of minimax algorithm
        """
        if self.get_status() == 'x':
            return -1
        elif self.get_status() == '0':
            return 1
        elif self.get_status() == 'draw':
            return 0
        if is_maximizing:
            best_score = -1000
            for row in range(3):
                for col in range(3):
                    if self.field[row][col] == ' ':
                        self.field[row][col] = '0'
                        score = self.minimax(depth + 1, False)
                        self.field[row][col] = ' '
                        if score > best_score:
                            best_score = score
            return best_score
        else:
            best_score = 1000
            for row in range(3):
                for col in range(3):
                    if self.field[row][col] == ' ':
                        self.field[row][col] = 'x'
                        score = self.minimax(depth + 1, True)
                        self.field[row][col] = ' '
                        if score < best_score:
                            best_score = score
            return best_score
