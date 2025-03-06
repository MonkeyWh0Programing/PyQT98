

#Шаблоны для объектов из игры

# 
# Шаблон NPC. Описвает и хранит свойсва того или иного NPC. 
# Хранится Имя и Здоровье
#
class NPC:
    def __init__(self, name):
        self.name = name   

    def showInfo(self):
        print(f"Имя: {self.name}")

        input()
    
    # def dialog(self, text):
    #     print("┌───────────────────┐")
    #     print(f'│{self.name}:│')
    #     print(f'├╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┤')
    #     print(f'│"{text}"│')
    #     print("└───────────────────┘")

    #     input()

class Character(NPC):
    def __init__(self, name, loyalty):
        super().__init__(name)
        self.loyalty = int(loyalty)
    
    def showInfo(self):
        print(f"Имя: {self.name}")   
        print(f"Лояльность: +{self.loyalty}")

        input()

class Player1(NPC):
    def __init__(self, name, playerClass):
        super().__init__(name)
        self.playerClass = playerClass
    
    def showInfo(self):
        print(f"Ваш персонаж:")
        print(f"Имя: {self.name}")
        print(f"Класс: {self.playerClass}")

        input()

# 
# Шаблон мест. Описвает и хранит свойсва мест. 
# Название и описание.
#
class Place:
    def __init__(self, name, about):
        self.name = name   
        self.about = about

    def showInfo(self):
        print("+-----------------------------------+")
        print(f'[{self.name}]')
        print(f'"{self.about}"')
        print("+-----------------------------------+")
        
        input()