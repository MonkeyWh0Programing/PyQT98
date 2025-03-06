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

def dialog(name, text):
        
        borderLenght = 0
        textSpace = 0
        nameSpace = 0

        if len(name) > len(text):
            borderLenght = len(name)+1
            textSpace = borderLenght - len(text)
        elif len(name) < len(text):
            borderLenght = len(text)
            nameSpace = borderLenght - len(name)


        print(f"╒{borderLenght * "═"}╕")
        print(f'│{name}{nameSpace * " "}│')
        print(f'├{borderLenght * "┄"}┤') 
        print(f'│{text}{textSpace * " "}│')
        print(f"└{borderLenght * "─"}┘")

        input()