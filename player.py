import math
import random

class Player:
    def __init__(self, letter):
        #letter is X or 0
    
    # we want all player to get move
    def get_move(self, game):
        pass
    

# we have to build computer player and human player

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
        # super class which is Player
    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square
    
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input( self.letter + '\'s turn. Input move (0-9):')
            
            try:
                val = int(square)
                if val not in game.availabel_moves():
                    raie ValueError
                valid_square = True
            except ValueError:
                print('Invalid square . Try again')
        return val
     
            
    
        