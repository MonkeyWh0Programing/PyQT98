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
    
    def dialog(self, text):
        print("=====================================")
        print(f'{self.name}: ')
        print("------------------------------------")
        print(f'"{text}"')
        print("------------------------------------")
        print("=====================================")



# 
# Шаблон мест. Описвает и хранит свойсва мест. 
# Название и описание.
#
class Place:
    def __init__(self, name, about):
        self.name = name   
        self.age = about

    def showInfo(self):
        pass