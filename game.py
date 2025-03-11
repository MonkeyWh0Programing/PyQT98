#Подключение файлов игры
import gameData
import characters as ch
import places as plc
import functions as func
import random


#Главный код игры
######################################################
#               -- Н А Ч А Л О --                    #
######################################################
print("╔═══════════════════════════════════╗")
print("║    И Г Р А    Н А Ч А Л А С Ь     ║")
print("╚═══════════════════════════════════╝")
print(gameData.TITILE)
print(gameData.GAMENAME)
print(f"version: {gameData.VERSION}")
print(f"{gameData.DESCRIPTION}")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

input()
answ = ""

while answ == "":
    answ = func.askPlayerInput("Дайте имя вашему персонажу").title().strip()

    if answ != "":
        ch.Player.name = answ
        break
    elif answ == "":
        print("Ввведите значение!")
        continue

    continue

while answ not in gameData.playebleClasses:
    answ = func.askPlayerInput("Какой класс у ващешего персонажа?").title().strip()

    if answ in gameData.playebleClasses and not answ == "Help":
        ch.Player.playerClass = answ
        ch.Player.showInfo()
        break
    
    elif answ == "":
            print("Ввведите значение!")
            continue

    elif answ not in gameData.playebleClasses and not answ == "Help":
        print("Такого класса нет в игре!")
        continue

    elif answ == "Help" and not answ in gameData.playebleClasses:
        print("Игровые классы доступные в игре:")
        print(gameData.playebleClasses)
    
    continue

func.dialog(plc.Forest.name, f"{plc.Forest.about}")

func.dialog(ch.Trall.name, f"Привет, {ch.Player.name}")
func.dialog(ch.Trall.name, f"Это деманстрационная версия игры! {gameData.VERSION}")
func.dialog(ch.Player.name, f"Чудесненько!")
func.dialog(ch.Trall.name, f"Не забывай устанавливать последние обновления!")

func.dialog(ch.Trall.name, f"Итак, давай покажу тебе кое что!")
func.dialog(ch.Trall.name, f"В игре есть очки лояльности.")
func.dialog(ch.Trall.name, f"Она влияет на отношение персонажей к тебе.")
func.dialog(ch.Trall.name, f"У каждого персонажа он свой!")
func.dialog(ch.Trall.name, f"Моя лояльность к тебе равна {ch.Trall.loyalty}")
func.dialog(ch.Trall.name, f"Сейчас я позову сюда {ch.Obb.name}a.")
func.dialog(ch.Trall.name, f"Ей, {ch.Obb.name}, иди-ка сюда!")
func.dialog(ch.Obb.name, f"*пришёл*. Чё надо?")

func.dialog(ch.Obb.name, f"Его лояльность к тебе равна {ch.Obb.loyalty}")
func.dialog(ch.Obb.name, f"Обзови его, {ch.Player.name}.")




print(gameData.ENDING)

print("╔═══════════════════════════════════╗")
print("║    И Г Р А    О К О Н Ч Е Н А     ║")
print("╚═══════════════════════════════════╝")

input()


