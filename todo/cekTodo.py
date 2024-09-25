import dataBase
from clearComandLine import clear

def viewTodo():
    if len(dataBase.dataTodo) == 0:
        print("data Kosong")
    else:
        clear()
        print("Todo Terkini: ")
        for x in range(len(dataBase.dataTodo)):
            print(f"{x + 1}. {dataBase.dataTodo[x]} ")