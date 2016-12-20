# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = r"C:\Users\aaron.neiderhiser\Documents\repos\mit_600\ps2\words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    #wordlist = string.split(line)
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program


# your code begins here!
def hangman(word):
    
    print("Welcome to the game, Hangman! I am thinking of a word that is", len(word) ,"letters long.")
    print("--------------------------")
    
    guesses = 8
    available_letters = 'abcdefghijklmnopqrstuvwxyz' 
    
    word_letters = []
    for b in word:
        word_letters.append(b)
    
    while guesses > 0 and len(word_letters) > 0:
        print("You have", guesses, "left.")  
        print(available_letters)
        guess = input("Please guess a letter: ")
        
        if guess not in word_letters:
            available_letters = available_letters.replace(guess,'')
            guesses -= 1
        else:
            letters.remove(guess)
            
   
    
def main():
    wordlist = load_words()
    word = choose_word(wordlist)

if __name__ == '__main__':
    main()