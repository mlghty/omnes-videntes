import tkinter as tk
import time
from threading import Thread
import threading
from kids.utils import login, registration, get_windows_processes, get_all_windows
from kids.gui import create_process_tree
# abandon all hope ye who enters here

def center_window(root, w, h):

        ws = root.winfo_screenwidth()
        hs = root.winfo_screenheight()

        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)

        root.geometry('%dx%d+%d+%d' % (w, h, x, y))

class start_data():

    def __init__(self, tab_control, tab, root):
        self.tab_control = tab_control
        self.tab = create_process_tree(self.tab_control, get_windows_processes(get_all_windows()))
        self.root = root
    
    def get_processes(self):

        return get_windows_processes(get_all_windows())
    
    def get_windows(self):

        return get_all_windows()

    # generates and updates the process tree
    def _update_tree(self):

        self.tab_control.add(self.tab, text ='Applications')
        center_window(self.root, 700, 600)

        processes = start_data.get_processes(self)

        for children in self.tab.get_children():

            self.tab.delete(children)

        for process in processes:

            self.tab.insert("", "end", values=process)
        
        self.t = Thread(target=self._update_tree)
        self.t.setDaemon(True)
        self.t.start()
    
    def start_update(self):
        self.root.after(10000, self._update_tree())
    
class login_scr():

    def __init__(self, tab, tab2, tab3, tab_control, root):
        self.signin_label = tk.Label(tab, text = "Sign In", bg = 'white', font = ("Times 12"))
        self.username_field = tk.Entry(tab, bd = 2, font = ("Times 11 italic"))
        self.password_field = tk.Entry(tab, bd = 2, font = ("Times 11 italic"))
        self.login_button = tk.Button(tab, text = "Sign In", command = self.log_submit)
        self.login_error = tk.Label(tab, text = "One of the fields is incorrect. Please try again.", bg = 'white')
        self.tab_control = tab_control
        self.tab2 = tab2
        self.tab3 = tab3
        self.root = root

    # handle login requests and move to application proper
    def log_submit(self):
            
        if((self.username_field.get() == "") or self.password_field.get() == ""):

            return
        elif(self.username_field.get() == "Enter Username" and self.password_field.get() == "Enter Password"):

            return
        elif(self.username_field.get() == "Enter Username"):

            return
        elif(self.password_field.get() == "Enter Password"):

            return

        username = self.username_field.get()
        password = self.password_field.get()

        x = login(username, password)

        if(x):
            
            self.root.title("Good Time")
            self.tab_control.hide(0)
            self.tab_control.hide(1)
            
            self.make_tabs()
        else:

            self.login_error.pack(side = 'bottom')

    # generates non-login tabs 
    def make_tabs(self):

            start_data(self.tab_control, self.tab2, self.root)._update_tree()
            self.tab_control.add(self.tab3, text ='log')
            

    # clears username prompt
    def log_clear_username(self, event = None):
        self.username_field.delete(0, "end")
        self.username_field.configure(font = ("Times 12"))
    
    # clears password prompt
    def log_clear_password(self, event = None):
        self.password_field.delete(0, "end")
        self.password_field.configure(font = ("Times 12"), show = '*')

    # positions widgets for login screen
    def make_login(self):

        self.signin_label.pack(side = 'top', pady = 30)

        self.username_field.insert(0, 'Enter Username')
        self.username_field.bind("<Button-1>", self.log_clear_username)
        self.username_field.pack(side = 'top', pady = 30)

        self.password_field.insert(0, 'Enter Password')
        self.password_field.bind("<Button-1>", self.log_clear_password)
        self.password_field.pack(side = 'top')

        self.login_button.pack(side = 'bottom', pady = 70)

class register_scr():

    def __init__(self, tab, tab_control):
        self.register_label = tk.Label(tab, text = "Register", bg = 'white', font = ("Times 12"))
        self.reg_username_field = tk.Entry(tab, bd = 2, font = ("Times 11 italic"))
        self.reg_password_field = tk.Entry(tab, bd = 2, font = ("Times 11 italic"))
        self.register_button = tk.Button(tab, text = "Register", command = self.reg_submit)
        self.register_error = tk.Label(tab, text = "An account with this username already exists. Please try again.", bg = 'white')
        self.register_success = tk.Label(tab, text = "You have successfully registered!", bg = 'white')

    # handle registration requests
    def reg_submit(self):
            
        if((self.reg_username_field.get() == "") or self.reg_password_field.get() == ""):

            return
        elif(self.reg_username_field.get() == "Enter Username" and self.reg_password_field.get() == "Enter Password"):

            return
        elif(self.reg_username_field.get() == "Enter Username"):

            return
        elif(self.reg_password_field.get() == "Enter Password"):

            return

        username = self.reg_username_field.get()
        password = self.reg_password_field.get()
        x = registration(username, password)

        if(x):
            self.register_error.pack(side = 'bottom')
        else:
            self.register_success.pack(side = 'bottom')
            
    # clears username prompt
    def reg_clear_username(self, event = None):
        self.reg_username_field.delete(0, "end")
        self.reg_username_field.configure(font = ("Times 12"))

    # clears password prompt
    def reg_clear_password(self, event = None):
        self.reg_password_field.delete(0, "end")
        self.reg_password_field.configure(font = ("Times 12"), show = '*')

    # generates widgets for registration tab
    def make_register(self):
        self.register_label.pack(side = 'top', pady = 30)

        self.reg_username_field.insert(0, 'Enter Username')
        self.reg_username_field.bind("<Button-1>", self.reg_clear_username)
        self.reg_username_field.pack(side = 'top', pady = 30)

        self.reg_password_field.insert(0, 'Enter Password')
        self.reg_password_field.bind("<Button-1>", self.reg_clear_password)
        self.reg_password_field.pack(side = 'top')

        self.register_button.pack(side = 'bottom', pady = 70)