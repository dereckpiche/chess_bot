# chessEngine

Date of completion: January 06, 2022.
Creator: Dereck Piche.

The computing core of this basic chess engine is located in the ChessEngine.py file.
The function getBestMove() takes the board of the instance and
makes the move i. It then gets the value of the move with the function
engine(). It returns the i'th move with the biggest value.

Engine() is a recursive function that takes a board state after an engine move
and returns a value corresponding to this moves's strength.
The value of the move is determined by the minmax algorithm (with alpha-beta prunning).

While engine() remains an implementation of the minmax algorithm with alpha-beta prunning, it is 
not an implementation that employs a direct recreation of the decision tree commonly used to explain
the concept of this algorithm. 

Because of this, instead of just using alpha-beta prunning to determine if it will have to calculate the 
value of a branch, the engine() function will instead skip it's construction entirely.

In order to do this, the engine() function will apply backpropagation as soon as it finalises the creation of
a branch.

Note that it is difficult to clearly explain the innerworkings of engine(). One must study it's 
code toroughly in order to understand it. It's not that complicated :).
