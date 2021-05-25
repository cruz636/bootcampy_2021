import json
import os
from difflib import get_close_matches

dictionary_data = json.load(open("data.json"))
again = 'y'

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def closeMatches(word, lista):
    condition = word in lista
    while condition == False:
        posibles = get_close_matches(word, lista)
        print("Sorry, I couldn't find that word. Try one of the following: ")
        for p in posibles:
            print("  ->", p)
        word = input("Type a word: ")
        condition = word in lista
    return word

def search_in_dictionary_data(word):
    word = word.lower()
    if word in dictionary_data.keys():
        return dictionary_data[word]
    else:
        return dictionary_data[closeMatches(word, dictionary_data.keys())]
    
while again == 'y':
    clear_terminal()
    word_typed = input("Type a word: ")
    definitions = search_in_dictionary_data(word_typed)
    if type(definitions) == list:
        for definition in definitions:
            print("  ->", definition)
    else:
        print("  ->", definitions)
    again = input("\nSearch again? [y/n] ")
    if again == "n":
        clear_terminal()
        print("Gracias, vuelvas prontos.")
