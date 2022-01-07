import ChessEngine as ce
import chess as ch

class Main:

    def __init__(self, board=ch.Board):
        self.board=board

    #play human move
    def playHumanMove(self):
        try:
            print(self.board.legal_moves)
            print("""To undo your last move, type "undo".""")
            #get human move
            play = input("Your move: ")
            if (play=="undo"):
                self.board.pop()
                self.board.pop()
                self.playHumanMove()
                return
            self.board.push_san(play)
        except:
            self.playHumanMove()

    #play engine move
    def playEngineMove(self, maxDepth, color):
        engine = ce.Engine(self.board, maxDepth, color)
        self.board.push(engine.getBestMove())

    #start a game
    def startGame(self):
        #get human player's color
        color=None
        while(color!="b" and color!="w"):
            color = input("""Play as (type "b" or "w"): """)
        maxDepth=None
        while(isinstance(maxDepth, int)==False):
            maxDepth = int(input("""Choose depth: """))
        if color=="b":
            while (self.board.is_checkmate()==False):
                print("The engine is thinking...")
                self.playEngineMove(maxDepth, ch.WHITE)
                print(self.board)
                self.playHumanMove()
                print(self.board)
            print(self.board)
            print(self.board.outcome())    
        elif color=="w":
            while (self.board.is_checkmate()==False):
                print(self.board)
                self.playHumanMove()
                print(self.board)
                print("The engine is thinking...")
                self.playEngineMove(maxDepth, ch.BLACK)
            print(self.board)
            print(self.board.outcome())
        #reset the board
        self.board.reset
        #start another game
        self.startGame()

#create an instance and start a game
newBoard= ch.Board()
game = Main(newBoard)
bruh = game.startGame()
