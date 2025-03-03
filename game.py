#Подключение файлов игры
import gameData
import characters as ch

#Главный код игры
######################################################
#               -- Н А Ч А Л О --                    #
######################################################
print("=====================================")
print("Game started")
print(f"version: {gameData.VERSION}")
print("=====================================")

print("Дайте имя вашему персонажу")
ch.Player.name = name = input("] ")
print("=====================================")

# print("Выберите класс к которому ваш персонаж будет принадлежать. Введите help для помощи.")
# choise = input("] ")

# quastion = True
# while quastion == True:
#     if choise in gameData.playebleClasses and not "help":
#         ch.Player.playerClass = choise
#         quastion = False
#         break

#     elif choise == "help":
#         for i in gameData.playebleClasses:
#             print(gameData.playebleClasses[i])
#             i += 1
#         quastion = True
#         break

#     elif choise not in gameData.playebleClasses and not "help":
#         print("Извините, такого класса нет! За помощью напишите help.")
#         quastion = True
#         break

        


# print(ch.Player.showInfo())

ch.Trall.dialog(f"Привет, {ch.Player.name}")
ch.Trall.dialog(f"Это деманстрационная версия игры! {gameData.VERSION}")
ch.Trall.dialog(f"Не забывай устанавливать последние обновления!")

print("=====================================")


