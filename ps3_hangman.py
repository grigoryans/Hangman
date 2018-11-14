# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
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
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    result = True
    for i in secretWord:
        if i not in lettersGuessed:
            result = False
            break
    return result


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    hiddenWord = ["_"]*len(secretWord)
    
    i = 0
    while i<len(lettersGuessed):
        j=0
        while j<len(secretWord):
            if lettersGuessed[i] == secretWord[j]:
                hiddenWord = list(hiddenWord)
                hiddenWord[j] = lettersGuessed[i]
                
            j+=1
        i+=1
    hiddenWord = " ".join(hiddenWord)
    print(hiddenWord)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters = "abcdefghijklmnopqrstuvwxyz"
    for i in lettersGuessed:
        if i in letters:
            letters = list(letters)
            letters.remove(i)
    letters = "".join(letters)    

    return letters


def howManyMistakes(theWord, lettersGuessed):
    count = 0
    for i in lettersGuessed:
        if i not in theWord:
            count+=1
    return count
    
    
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    guessCounter = 0
    guessedLetters = []
    getGuessedWord(secretWord, guessedLetters)
    
    while guessCounter < len(secretWord)+5:
        letter = input("Give me a letter... ")
        if(letter in guessedLetters):
            print("you have already choosen this character")
            print("Mistakes - ", howManyMistakes(secretWord,guessedLetters))
        else:
            
            guessedLetters.append(letter)
            getGuessedWord(secretWord, guessedLetters)
            guessCounter += 1
            
            print("Mistakes - ", howManyMistakes(secretWord,guessedLetters))
            
            if isWordGuessed(secretWord, guessedLetters):
                print("You won!!!")
                break
        
            
        avlLetters = getAvailableLetters("".join(guessedLetters))
        print("Available letters - ",avlLetters)

theWord = chooseWord(wordlist)
#print(theWord)
hangman(theWord)
    




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
