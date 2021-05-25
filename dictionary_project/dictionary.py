import json
import os
from difflib import get_close_matches

dic = json.load(open("C:/Users/Tomas/vscodeProjects/aprendiendoconara/diccionario/data.json"))
again = 'y'

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

def search_in_dic(word):
    word = word.lower()
    if word in dic.keys():
        return dic[word]
    else:
        return dic[closeMatches(word, dic.keys())]
    
while again == 'y':
    os.system('cls')
    palabra_ingresada = input("Type a word: ")
    definition = search_in_dic(palabra_ingresada)
    if type(definition) == list:
        for i in definition:
            print("  ->", i)
    else:
        print("  ->", definition)
    again = input("\nSearch again? [y/n] ")
    if again == "n":
        os.system('cls')
        print("Gracias, vuelvas prontos.")
