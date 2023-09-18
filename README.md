# tic_tac_toe_game
Using the minimax algorithm and binary tree

For creating the field, I used a 2D array with whitespaces in the beginning.

Method __str__ print the current field.

The user can input the wanted position from 0 to 8( it can be from 1 to 9) and make a move.

The computer uses a minimax algorithm to win or have a draw. 

The algorithm: 

![mini-max-algorithm-in-ai-step1](https://user-images.githubusercontent.com/92577132/169818622-8d340b6d-8e8e-473d-b5bb-15ff1977b0e3.png)

At each step, the method get_status() checks the state of the game -> it returns 'x' if the player wins, '0' if the computer, 'draw' or 'continue.'


