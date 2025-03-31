import random

def roll_dice():
   
    roll = input ("Roll the Dice? (Yes /No)")
    
    while roll.lower() == "yes":
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        
        print("dice rolled: {} and {}".format(dice1,dice2))
        print("")
        roll = input("Roll again? (yes/No)")
roll_dice()