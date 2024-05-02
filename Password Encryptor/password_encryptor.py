import os

from cryptography.fernet import Fernet

def write_key():
    key=Fernet.generate_key()
    with open("\Password Encryptor\key.key","wb") as key_file:
        key_file.write(key)

def load_key():
    file=open("\Password Encryptor\key.key","rb")
    key=file.read()
    file.close()
    return key

if os.path.exists("\Password Encryptor\key.key")==False:
    write_key()

key=load_key()
fer=Fernet(key)

def view():
    with open("\Password Encryptor\passwords.txt","r") as f:
        for lines in f.readlines():
            data=lines.rstrip()
            user,passw=data.split("|")
            print("\tUser:",user,"\n","\tPassword:",fer.decrypt(passw.encode()).decode())

def add():
    name=input("Account Name: ")
    pwd=input("Password: ")

    with open('\Password Encryptor\passwords.txt','a') as f:
        f.write(name+"|"+fer.encrypt(pwd.encode()).decode()+"\n")

while True:
    mode=input("Would you like to add a new password or view existing ones (view/add) or would you like to quit(q)").lower()

    if mode=="q":
        break

    if mode=="view":
        view()
    elif mode=="add":
        add()

    else:
        print("Invalid mode.")
        continue