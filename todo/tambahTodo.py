import dataBase
import clearComandLine 


def addTodo():

    newTodo = input("Masukan Todo Baru:")
    if len(dataBase.dataTodo) == 0:
        #data di database tidak boleh kosong, maka system akan memasukan langsung input tanpa bertanya ke user
        print("data kosong, inputan akan langsung dimasukan database")
        dataBase.dataTodo.append(newTodo)
    else:
        for data in dataBase.dataTodo:
            if newTodo  in data:
                print ("Todo yang di masukan sudah terdaftar di dataBase")   
                break 
            else:
                cek = input("Todo baru tidak terdaftar di database, apakah anda untuk menyimpan data baru y/n : ")    
                if cek == "y":
                    dataBase.dataTodo.append(newTodo)
                    break
            clearComandLine.clear()
                
                
