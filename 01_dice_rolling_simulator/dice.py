import random
import os

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

clear_terminal()
print('\nBienvenidos al "dice rolling simulator".\n\n')

dado = {
1 : "+-------+\n|       |\n|   0   |\n|       |\n+-------+\n",
2 : "+-------+\n|     0 |\n|       |\n| 0     |\n+-------+\n",
3 : "+-------+\n|     0 |\n|   0   |\n| 0     |\n+-------+\n",
4 : "+-------+\n| 0   0 |\n|       |\n| 0   0 |\n+-------+\n",
5 : "+-------+\n| 0   0 |\n|   0   |\n| 0   0 |\n+-------+\n",
6 : "+-------+\n| 0   0 |\n| 0   0 |\n| 0   0 |\n+-------+\n"
}

continuar = 'y'

while continuar == 'y':
    lado = random.randint(1,6)
    print(dado[lado])
    continuar = input("Quiere tirar otra vez?: y/n ")
    while continuar != 'y' and continuar != 'n':
        clear_terminal()
        continuar = input("Quiere tirar otra vez?: y/n ")
    clear_terminal()
    if continuar == "n":
        print("Gracias por jugar, volvé cuando quieras!")

