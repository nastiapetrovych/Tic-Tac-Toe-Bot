"""
Runs the process
"""

from board import Board


def main():
    board = {'0': (0, 0), '1': (0, 1), '2': (0, 2), '3': (1, 0), '4': (1, 1), '5': (1, 2), '6': (2, 0), '7': (2, 1),
             '8': (2, 2)}
    tree_obj = Board()
    while tree_obj.get_status() == 'continue':
        print(tree_obj)
        enter_inp = input('Enter the coordinates{0-8}\n')
        tree_obj.make_move(board[enter_inp], 'x')
        tree_obj.make_computer_move()
    print(tree_obj.get_status())

main()
