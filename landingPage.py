import logins #ambil module di file logins

import os #import os untuk clear cmd
from todo.cekTodo import viewTodo
from todo.tambahTodo import addTodo
from todo.hapustodo import delete_todo
from todo.editTodo import editTodo
import clearComandLine
"""
membuat CRUD system todo, yang mana user akan login login terlebih dahulu agar masuk ke laman
Todo Page
"""


def todo():
    #membersihkan Command line
    clearComandLine.clear()
    while True:
        print("==============================================")
        print("==========Selamat Datang di TodoList==========")
        print("==============================================")
    
     
        print("1. lihat Todo terkini")
        print("2. tambah Todo")
        print("3. hapus Todo")
        print("4. edit Todo")
        pilihan = input("masukan pilihan kamu: ")
        if pilihan == "1":
            viewTodo()
        elif pilihan == "2":
            addTodo()
        elif pilihan == "3":
            delete_todo()
        elif pilihan == "4":
            editTodo()
        else:
            print("input yang anda masukan salah")
        
    
    

def main():
    print("==================================")
    print("==========Selamat Datang==========")
    print("==================================")
    
    cek = True
    while cek:
        print("silahkan login!!")
        username = input("Username: ")
        password  = input("Password: ")     
        
        if(logins.login_account(username,password)):
            print("berhasil logins")
            todo()
            cek = False
        else:
            print("data kosong")
            daftar = input("apakah ingin mendaftar y/n : ")
            logins.create_account(username,password) if daftar == 'y' else "gagal logins"
            
main()