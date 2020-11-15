import hashlib
import os
import shutil
from tkinter import *
from functools import partial



salt = os.urandom(32) # uuid is used to generate a random number

def hash_password(password):
    return password

def check_password(hashed_password, user_password):
    if user_password == hashed_password:
        return password


def login(username, password):  # Store data in file
    print("Storing data....")
    print("username entered :", username.get())
    print("password entered :", password.get())
    with open("user-data.txt", "a+") as file:
        passw = hash_password(password.get())
        file.write(f"{username.get()}-{passw}\n")
    return

def check(username, password):  # Check the password  here
    print("Password Checking....")
    print("\tusername entered :", username.get())
    print("\tpassword entered :", password.get())
    correct = False
    # Check from file
    with open("user-data.txt", "r") as file:
        for line in file.readlines(): # Read all lines
            file_line = line.split("-")
            user, hashed_pwd = file_line[0], file_line[1]
            # compare the usernames
            if user == username.get():
                if check_password(hashed_pwd, password.get()):
                    correct = True
                    break
    if correct: # Print correct or incorrect
        print("\t\tCorrect Data")
    else:
        print("Incorrect data")


# window
tkWindow = Tk()
tkWindow.geometry('400x150')
tkWindow.title('User Login Form')

# username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)

# password label and password entry box
passwordLabel = Label(tkWindow, text="Password").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)

validateLogin = partial(login, username, password)
checkPassword = partial(check, username, password)

# login button
loginButton = Button(tkWindow, text="Store Data", command=validateLogin).grid(row=4, column=0)
checkPasswordButton = Button(tkWindow, text="Check Password", command=checkPassword).grid(row=4, column=1)

tkWindow.mainloop()