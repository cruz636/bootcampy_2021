import os
import random

words_file = "words.txt"
words = open(words_file).read().splitlines()

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def get_word():
    index = random.randint(0,len(words))
    word = words[index]
    while len(word) <= 3:
        index = random.randint(0,len(words))
        word = words[index]
    return word.lower()

def replace_blanks(letter, word, old_blanks):
    blanks = ''
    index = 0
    for letter_index in word:
        if letter_index == letter:
            blanks += letter.upper()
        else:
            if old_blanks[index] != '_':
                blanks += old_blanks[index]
            else:
                blanks += '_'
        index += 1
    return blanks

hangman = {
    '0' :   "__________\n    |\n  O_| \n /|\ \n / \ ",
    '1' :   "__________\n     \n \O/  \n  |  \n / \ ",
    '2' :   "__________\n     \n \O   \n  |  \n / \ ",
    '3' :   "__________\n     \n  O   \n  |  \n / \ ",
    '4' :   "__________\n     \n  O   \n  |  \n /   ",
    '5' :   "__________\n     \n  O   \n  |  \n     ",
    '6' :   "__________\n     \n  O   \n     \n     ",
    '7' :   "__________\n     \n      \n     \n     ",
}         

word = get_word()
message = "Guess the word: "
blank_spaces = ''
lives = 7
for letter_index in word:
    blank_spaces += '_'

while lives > 0 and word != blank_spaces.lower():
    clear_terminal()
    #print(word)
    print('Lives left:', lives)
    print(hangman[str(lives)])
    letter_typed = input(message + blank_spaces + '\n  -> ')
    letter_typed = letter_typed.lower()
    if word.find(letter_typed) != -1:
        blank_spaces = replace_blanks(letter_typed, word, blank_spaces)
    else:
        lives -= 1
    
clear_terminal()
if lives > 0:
    print('Lives left:', lives)
    print(hangman[str(lives)])
    print("YOU WIN.")
else:
    print('Lives left:', lives)
    print(hangman[str(lives)])
    print("YOU LOSE.")
    