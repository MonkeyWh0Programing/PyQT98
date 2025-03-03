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
print("Game started")
print(f"version: {gameData.VERSION}")
print(f"{gameData.DESCRIPTION}")
print("=====================================\n")

input()

print("Дайте имя вашему персонажу")
ch.Player.name = name = input("] ")
print("=====================================\n")

plc.Forest.showInfo()

func.askPlayerInput("Как дела?")


ch.Trall.dialog(f"Привет, {ch.Player.name}")
ch.Trall.dialog(f"Это деманстрационная версия игры! {gameData.VERSION}")
ch.Player.dialog(f"Чудесненько!")
ch.Trall.dialog(f"Не забывай устанавливать последние обновления!")

func.characterAskPlayerInput("Тебе нравится?", ch.Trall.name)

print("=====================================")


