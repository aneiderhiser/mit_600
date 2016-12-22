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
def insert_spaces(string):
    new_string = ''    
    for e in string:
        new_string = new_string + e + ' '
    return new_string[:-1]


# your code begins here!
def hangman(word):
    print("--------------------------")
    print("--------------------------")
    print("Welcome to the game, Hangman! I am thinking of a word that is", len(word) ,"letters long.")
    print("--------------------------")
    print("--------------------------")
    
    guesses = 8
    word_list = []
    for e in word:
        word_list.append(e)
        word_list.append(' ')
    word_list = word_list[:-1]
    
    guess = insert_spaces('_'*len(word))
    guess_list = list(guess)
    alpha = 'abcdefghijklmnopqrstuvwxyz' 
        
    while guesses > 0 and guess_list != word_list:
        print("\n")        
        print("You have", guesses, "guesses left.")
        print("Current guess: ", ''.join(guess_list))
        print("Available letters: ", alpha)
        letter = input("Please guess a letter: ")
        
        if letter in word:
            index = []
            i = 0
            for e in word_list:
                if letter == e:
                    index.append(i)
                i += 1
                
            for k in index:
                guess_list[k] = letter

            print("Good guess!!")            
            alpha = alpha.replace(letter,'')

        else:          
            print("Oops! That letter is not in my word!!")            
            alpha = alpha.replace(letter,'')
            guesses -= 1
            
    if guesses > 0 and guess_list == word_list:
        print("Congratulations, you won!")
        print(word)
    else:
        print("YOU LOSE!!!!")
        print(word)
    
def main():
    print("\n")
    word = choose_word(load_words())
    print("\n")   
    hangman(word)

if __name__ == '__main__':
    main()
    
    