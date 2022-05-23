# tic_tac_toe_game
Usuing minimax algorithm and binary tree

For creating of the field I use 2D array with whitespaces in the beggining.

Method __str__ print the current field.

The user can input the wanted position from 0 to 8( it can be from 1 to 9) and make a move.

The computer uses minimax algorithm to win or have a draw. 

The algorithm: 
![mini-max-algorithm-in-ai-step1](https://user-images.githubusercontent.com/92577132/169818622-8d340b6d-8e8e-473d-b5bb-15ff1977b0e3.png)

At each step the method get_status() chesks the state of the game -> it returns 'x' if the player wins, '0' if computer, 'draw' or 'continue'


