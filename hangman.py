import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)#choose randomly from a list of words
    while '-' in word or ' ' in word:
        word = random.choice(words)
        #It will  stop choosing when a word dose't have a space or -
        
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # a varable that saves all the words letter in sets
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    lives = 7
    
    
    # getting user input
    while len(word_letters) > 0 and lives > 0:
        #letter used
        print('you have ',lives , 'lives left \n used  letters are: ', ' '.join(used_letters))
        
        #what the current word is
        word_list = [ letter  if letter in used_letters else '-' for letter in word ]
        print("current word : ",' '.join(word_list))
        
        user_letter = input('Guess a letter:').upper()
        if user_letter in alphabet - used_letters: # If this is valid char in alphabet  and i haven't used then i will add this to the used letter list
            used_letters.add(user_letter)
            if user_letter in word_letters:# If i gussed that letter form word that i alreddy used then i will remove it form the wordletter
                word_letters.remove(user_letter)
            else:
                lives = lives - 1   # takes away a life if wrong
                print(" letter is not in the word")
        elif user_letter in used_letters: # User enter a letter that is already present used before and therefore no wrong guess but choose another unused letter
            print("you have already used that character:)")
        else:
            print('Invalid Character')
    if lives == 0:
        print(' you died , sorry. The word was ', word)
    else:
        print('you gussed the wrong word ', word,' !!')
        
        
            # An empty set in order to record the used letters by the user
hangman()   
user_input = input('Type Something:')
print(user_input)
