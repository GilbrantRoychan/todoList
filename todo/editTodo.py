import dataBase
from todo.cekTodo import viewTodo


def editTodo():
    #akan menampilkan todo terkini
    viewTodo()  
    inputUser = int(input("masukan list yang akan kamu masukan : "))
    
    for data in dataBase.dataTodo:
        #lakukan pencarian dan edit data baru
        if dataBase.dataTodo[inputUser-1] == data:
            #confrim dari user untuk memasukan databaru
            newTodo = input(f"data di database di temukan, ingin Ganti ke TodoBaru: ")
            
            #confirm untuk melanjutkan
            cek = input(f"data lama di database adalah {data} ingin ke data baru {newTodo}? y/n : ")
            if cek == "y":
                try:
                    dataBase.dataTodo[inputUser-1] = newTodo
                except Exception as e:
                    print(str(e))
            else:
                pass