import chess as ch
import random as rd

class Engine:

    def __init__(self, board=None, maxLevel=None, color=None):
        self.board=board
        self.color=color
        self.maxLevel=maxLevel

    def evalFunct(self):
        compt = 0
        #Sums up the material values
        for i in range(64):
            compt=compt+self.squareResPoints(ch.SQUARES[i])
        compt = compt + self.mateOpportunity()
        compt = compt + 0.0001*rd.Random()
        return compt

    def mateOpportunity(self):
        if (self.board.legal_moves.count()==0):
            if (self.board.turn == self.color):
                return -999
            else:
                return 999
        else:
            return 0

    #Hans Berliner's point system
    #Takes a square as input and 
    #returns the value of it's resident
    def squareResPoints(self, square):
        pieceValue = 0
        if(self.board.piece_type_at(square) == ch.PAWN):
            pieceValue = 1
        elif (self.board.piece_type_at(square) == ch.ROOK):
            pieceValue = 5.1
        elif (self.board.piece_type_at(square) == ch.BISHOP):
            pieceValue = 3.33
        elif (self.board.piece_type_at(square) == ch.KNIGHT):
            pieceValue = 3.2
        elif (self.board.piece_type_at(square) == ch.QUEEN):
            pieceValue = 8.8

        if (self.board.color_at(square)!=self.color):
            return -pieceValue
        else:
            return pieceValue

        
    def engine(self, candidate, depth):
        
        #reached max depth of search or no possible moves
        if ( depth == self.maxLevel 
        or self.board.legal_moves.count() == 0):
            return self.evalFunct()
        
        else:
            moveListe = list(self.board.legal_moves)
            
            #initialise newCandidate
            newCandidate = None
            if(depth % 2 == 0):
                newCandidate = float("inf")
            else:
                newCandidate = float("-inf")
            
            #analyse board after deeper moves
            for i in moveListe:
                self.board.push(i)
        
                value = self.engine(newCandidate, depth + 1) 
                #if minimizing (human player's turn)
                if(value < newCandidate and depth % 2 == 1):
                    newCandidate = value
                #if maximizing (engine's turn)
                elif(value > newCandidate and depth % 2 != 1):
                    #need to save move played
                    if (depth == 1):
                        move=i
                    newCandidate = value
                #alpha-beta prunning cuts: 
                #for alpha-beta prunning of the 
                #first type (previous move was made 
                #by the human player)
                if (candidate != None
                 and value < candidate 
                 and depth % 2 != 1):
                    self.board.pop()
                    break
                #for alpha-beta prunning of the 
                #second type (previous move was 
                #made by the engine)
                elif (candidate != None 
                and value > candidate 
                and depth % 2 == 1):
                    self.board.pop()
                    break
                    
                self.board.pop()
            #return min or max value
            if (depth>1):
                return newCandidate
            else:
                return i



  



            
            


        


        



            






        
        




        




    
    
