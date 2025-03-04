#Подключение файлов игры
import gameData
import characters as ch
import places as plc
import functions as func

#Главный код игры
######################################################
#               -- Н А Ч А Л О --                    #
######################################################
print("=====================================")
print("    И Г Р А    Н А Ч А Л А С Ь       ")
print("=====================================")
print(f"version: {gameData.VERSION}")
print(f"{gameData.DESCRIPTION}")
print("=====================================")

input()

answ = func.askPlayerInput("Дайте имя вашему персонажу")
ch.Player.name = answ

while answ not in gameData.playebleClasses:

    answ = func.askPlayerInput("Какой класс у ващешего персонажа?")

    if answ in gameData.playebleClasses and not answ == "help":
        ch.Player.playerClass = answ
        ch.Player.showInfo()
        break

    elif answ not in gameData.playebleClasses and not answ == "help":
        print("Такого класса нет в игре!")
        continue

    elif answ == "help":
        print("Игровые классы доступные в игре:")
        print(gameData.playebleClasses)
    
    continue
    
    



plc.Forest.showInfo()

ch.Trall.dialog(f"Привет, {ch.Player.name}")
ch.Trall.dialog(f"Это деманстрационная версия игры! {gameData.VERSION}")
ch.Player.dialog(f"Чудесненько!")
ch.Trall.dialog(f"Не забывай устанавливать последние обновления!")
func.characterAskPlayerInput("Тебе нравится?", ch.Trall.name)

ch.Trall.dialog(f"Итак, давай покажу тебе кое что!")
ch.Trall.dialog(f"В игре есть очки лояльности.")
ch.Trall.dialog(f"Она влияет на отношение персонажей к тебе.")
ch.Trall.dialog(f"У каждого персонажа он свой!")
ch.Trall.dialog(f"Моя лояльность к тебе равна {ch.Trall.loyalty}")
ch.Trall.dialog(f"Сейчас я позову сюда {ch.Obb.name}a.")
ch.Trall.dialog(f"Ей, {ch.Obb.name}, иди-ка сюда!")
ch.Obb.dialog(f"*пришёл*. Чё надо?")
ch.Trall.dialog(f"Его лояльность к тебе равна {ch.Obb.loyalty}")
ch.Trall.dialog(f"Согласись, не очень то и хорошо он к тебе относится!")




print("=====================================")
print("    И Г Р А    О К О Н Ч Е Н А       ")
print("=====================================")


