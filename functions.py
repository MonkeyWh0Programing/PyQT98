#Функции игры
import objects
import characters

def askPlayerInput(question):

    print("+-----------------------------------+")
    print(question)
    
    answer = input(f"{characters.Player.name}: ")
    print("+-----------------------------------+\n")
    return answer

def characterAskPlayerInput(question, character):
    print("+-----------------------------------+")
    print(f"{character}: {question}")
    
    answer = input(f"{characters.Player.name}: ")
    print("+-----------------------------------+\n")
    return answer