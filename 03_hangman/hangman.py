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


word = get_word()
message = "Guess the word: "
blank_spaces = ''
lives = 10
for letter_index in word:
    blank_spaces += '_'

while lives > 0 and word != blank_spaces.lower():
    clear_terminal()
    print(word)
    letter_typed = input(message + blank_spaces + '\n  -> ')
    letter_typed = letter_typed.lower()
    if word.find(letter_typed) != -1:
        blank_spaces = replace_blanks(letter_typed, word, blank_spaces)
    else:
        lives -= 1
        print('Lives left:', lives)
    
clear_terminal()
if lives > 0:
    print("YOU WIN.")
    print('Lives left:', lives)
else:
    print("YOU LOSE.")
    

