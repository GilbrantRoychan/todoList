import dataBase

def login_account(user,pas):
    for x,y in dataBase.dataLogin:
        if user == x and pas == y:
            return True
        else:
            return False

def create_account(user,pas):
    dataBase.dataLogin.append([user,pas])
    print("Akun sudah di buat !!")
            
        