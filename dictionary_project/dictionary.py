import json
import webbrowser
import platform
import os

# load dictionary file
data = json.load(open("C:/Users/Tomas/vscodeProjects/bootcampy_2021/dictionary_project/data.json"))

def clear():
    # in order to use the correct command
    # we need to know the s.o
    system = platform.system()

    if system == 'Windows':
        # Windows
        os.system("cls")
    else:
        # for Linux or MacOs
        os.system("clear")

def autocomplete(letters):
    size = len(letters)
    for word in data:
        if word[0:size] == letters:
            print(word)

def main(first_time=True):
    
    if first_time:
        print(" AYE AYE Sailor! ")
        print(" Search for any word in the ocean!")
        print(" Enter a letter and press ENTER for suggestions")
        print(" Then enter  . to set sail ( search for the word )")
    
    word = ''
    while True:
        print('\n')
        input_word = input("search for a word: {}".format(word))
        if input_word == ".":
            # search for word
            search(word)
            break
        word = word + input_word
        clear()
        print(" Enter . to set sail ( search for the word )")
        
        if(len(word) > 3):
            print("\n ______________")
            print("Suggestions")
            autocomplete(letters=word)

def search(word):
    
    if word == 'X':
        print("good bye sailor!")
        exit()
    
    if word == 'X captain':
        url = "https://www.youtube.com/watch?v=SLiNQhQr4G4"
        webbrowser.open(url, new=0, autoraise=True)
        print("""
               \_/
                |._
                |'."-._.-""--.-"-.__.-'/
                |  \       .-.        (
                |   |     (@.@)        )
                |   |   '=.|m|.='     /
                |  /    .='`"``=.    /
                |.'                 (
                |.-"-.__.-""-.__.-"-.)
                |
                |
                |
            Goodbye Pirate!
              """)
        exit()

    try:
        clear() 
        print("Definition for `{}`".format(word))
        print("\n")
        word = word.lower()
        print("".join(data[word]))
        print("\n _____________________")
        print("( enter X for closing ) \n")
    except:
        print("word not found \n")
    
    main(first_time=False)

main()


