#настройки для интерфейса

def table(name, clas, health):
        
        title = "Ваш персонаж"
        borderLenght = 0
        textSpace = 0

        values = [name, clas, health]
        lenValue = max(values, key=len)

        borderLenght = len(lenValue)
        textSpaceName = borderLenght - len(name)
        textSpaceClas = borderLenght - len(clas)
        textSpaceHealth = borderLenght - len(health)
        textSpaceTitle =len(lenValue)-3



        print(f"╒═════════{borderLenght*"═"}╕")
        print(f"│Ваш персонаж{textSpaceTitle* " "}│")
        print(f"╞════════╤{borderLenght*"═"}╡")
        print(f"│Имя     │{name}{textSpaceName* " "}│")
        print(f"├────────┼{borderLenght*"─"}┤")
        print(f"│Класс   │{clas}{textSpaceClas* " "}│")
        print(f"├────────┼{borderLenght*"─"}┤")
        print(f"│Здоровье│{health}{textSpaceHealth* " "}│")
        print(f"└────────┴{borderLenght*"─"}┘")

        input()


