from todo.cekTodo import viewTodo
import dataBase

def delete_todo():
    viewTodo() #untuk melihat todo terkini
    
    hapusTodo = int(input("Masukan list Todo yang mau di hapus : "))
    
    #cek kondisi terlebih dahulu
    """
    1. jika angka yang dimasukan melebihi dari kapasitas list return False
    2. jika angka yang dimasukan tidak ada return False
    3. jika ada konfirmasi terlebih dahulu nama nya jika iya maka hapus dan naikan 1 angka di bawahnya
    """
    if hapusTodo>len(dataBase.dataTodo): 
        return False
    else:
       for data in dataBase.dataTodo:
           if dataBase.dataTodo[hapusTodo-1] == data:
                cek = input(f"data yang akan dihapus adalah {data} apakah anda yakin y/n")
                if cek == "y":
                    dataBase.dataTodo.remove(data)
                    print(f"todo {data} sukses di hapu")
                
               