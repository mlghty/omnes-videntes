# main control file
# 29 November, 2020
import tkinter as tk
from tkinter import ttk

from kids.gui import login_scr, register_scr, center_window

class start_screen:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SK Authentication")
        self.root.geometry("400x800")
        self.notebook()

    def notebook(self):

        # initializing tabs
        self.tab_control = ttk.Notebook(self.root)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab3 = ttk.Frame(self.tab_control)
        self.tab4 = ttk.Frame(self.tab_control)
        self.tab5 = ttk.Frame(self.tab_control)
        self.tab6 = ttk.Frame(self.tab_control)

        # notebook style
        noteStyler = ttk.Style()
        noteStyler.configure("TNotebook", background='white', borderwidth=0)
        noteStyler.configure("TNotebook.Tab", background='white')
        noteStyler.configure("TFrame", background='white')

        # Frame Control
        self.notebook = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text ='Login')
        self.tab_control.add(self.tab2, text ='Register')
        self.tab_control.pack(expand = 1, fill ="both")

        # call login and register tabs
        login_scr(self.tab1, self.tab3, self.tab4, self.tab5, self.tab6, self.tab_control, self.root).make_login()
        register_scr(self.tab2, self.tab_control).make_register()

    def start(self):
        
        center_window(self.root, 400, 450)
        self.root.mainloop()

start_screen().start()