#настройки для интерфейса

def dialog(name, text):
        
        borderLenght = 0
        textSpace = 0
        nameSpace = 0

        if len(name) > len(text):
            borderLenght = len(name)+1
            textSpace = borderLenght - len(text)-2
        elif len(name) < len(text):
            borderLenght = len(text)+2
            nameSpace = borderLenght - len(name)-1


        print(f"┌{borderLenght * "─"}┐")
        print(f'│{name}:{nameSpace * " "}│')
        print(f'├{borderLenght * "╌"}┤')
        print(f'│"{text}"{textSpace * " "}│')
        print(f"└{borderLenght * "─"}┘")

        input()


dialog("Траль", "Привет, дорогой друг! Я очень долго ждал тебя, и вот наконец-то настал момент нашего знакомства!")


