import ChessEngine as ce
import chess as ch

#get the human's move
def getHumanMove(board):
    print(board.legal_moves)
    print("""To undo your last move, type "undo".""")
    play = input("Your move: ")
    if (play=="undo"):
        board.pop()
        board.pop()
        getHumanMove(board)
        return
    board.push_san(play)
    return board


#get engine's move
def play(board, depth, color):
    engine = ce.Engine(board, depth, color)
    return engine.engine()

#start a game
def main():
    board = ch.Board()
    #get human player's color
    color=None
    while(color!="b" and color!="w"):
        color = input("""Play as (type "b" or "w"): """)
    depth=None
    while(isinstance(depth, int)==False):
        depth = int(input("""Choose depth: """))
    if color=="b":
        while (board.is_checkmate()==False):
            print("The engine is thinking...")
            board.push_uci(play(board, depth, ch.WHITE))
            print(board)
            board=getHumanMove(board)
            print(board)
        print(board.outcome())    
    elif color=="w":
        while (board.is_checkmate()==False):
            print(board)
            board=getHumanMove(board)
            print(board)
            print("The engine is thinking...")
            board.push_uci(play(board, depth, ch.BLACK))
        print(board.outcome())
    board.reset
    main()
main()
