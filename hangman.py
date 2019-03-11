import string
from words import get_secret_word
from images import IMAGES
import random

# End of helper code
# -----------------------------------

def is_word_guessed(secret_word, guessed_word):
    if str(secret_word) == guessed_word:
        return True
    return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: ek string word jo ki user ko guess kar raha hai
    letters_guessed: ek list hai, jisme wo letters hai jo ki user nai abhi tak guess kare hai
    returns: ek string return karni hai jisme wo letters ho jo sahi guess huye ho and baki jagah underscore ho.
    eg agar secret_word = "kindness", letters_guessed = [k,n, s]
    to hum return karenge "k_n_n_ss"
    '''

    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    
    return guessed_word


def get_available_letters(letters_guessed):
    letters = string.ascii_lowercase
    letters_left  = ""
    for letter in letters:
        if letter not in letters_guessed:
            letters_left = letters_left + letter

    return letters_left

def get_hint(secret_word,letters_guessed):
    hint_list = []
    for i in secret_word:
        if i not in letters_guessed:
            hint_list.append(i)
    return random.choice(hint_list)


def hangman(secret_word):
    
    print("Welcome to the game, Hangman!")
    difficulty = input("Please choose the difficulty of the game:\neasy\nmediun\nhard\n>")
    if difficulty == 'easy':
        lives = 8
    elif difficulty == 'medium':
        lives = 6
    elif difficulty == 'hard':
        lives = 4
    else:
        lives = 4
        print('Hard chosen by default!\n')
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("")
    if difficulty == 'easy':
        lives = 8
    elif difficulty == 'medium':
        lives = 6
    elif difficulty == 'hard':
        lives = 4
    else:
        lives = 4
        print('Hard chosen by default!')
    letters_guessed = []

    while True:
        if lives == 0:
            print("Remaining Lives : " , lives)
            print("You are Dead!!!\nThe word was " + str(secret_word) +".")
            break
        
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: " + available_letters)
        print("Remaining Lives : " , lives)
        print("Type 'hint' for help.")
        guess = input("Please guess a letter: ")

        letter = guess.lower()
        if (guess.isalpha() and len(guess) == 1):
            if letter in secret_word:
                letters_guessed.append(letter)
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
                print("")

                if is_word_guessed(secret_word, guessed_word) == True:
                    print(" * * Congratulations, you won! * * ")
                    print("")
                    exit()

            else:
                print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
                print(IMAGES[8-lives])
                lives = lives - 1
                letters_guessed.append(letter)
                print ("")
        elif guess == "hint":
            print("\nHint: " + get_hint(secret_word,letters_guessed) + "\n")
        
        else:
            print("\nINVALID INPUT!!!\nPlease make a proper guess!!!\n")
            
    
secret_word = get_secret_word()
hangman(secret_word)