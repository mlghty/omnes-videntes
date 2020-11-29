<<<<<<< HEAD
import tkinter as tk
from tkinter import ttk
import time

from threading import Thread
import threading

from kids.utils import get_all_windows,  get_windows_processes
from kids.gui import create_process_tree

# processes = get_windows_processes(get_all_windows()) //  case 1
# windows = get_all_windows() // case 2


class app:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("I Over C") # Change name eventually
        self.root.geometry("400x700") # Change window size or fix the expand fill for tab1
        self.notebook()
        #self._create_widgets()
     
    def notebook(self):
        self.tabControl = ttk.Notebook(self.root)
        processes = get_windows_processes(get_all_windows())
        
        # Tabs
        self.tab1 = create_process_tree(self.tabControl, processes)
        self.tab2 = ttk.Frame(self.tabControl)

        # Style
        noteStyler = ttk.Style()
        noteStyler.configure("TNotebook", background='white', borderwidth=0)
        noteStyler.configure("TNotebook.Tab", background='white')
        noteStyler.configure("TFrame", background='white')

        # Frame Control
        self.notebook = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab1, text ='Duration')
        self.tabControl.add(self.tab2, text ='Graphs') 
        self.tabControl.pack(expand = 1, fill ="both")

        # Labels
        label = tk.Label(self.tab2, width=60)
        label.configure(text="time remaining: %d seconds")        
        label.place(x=0, y=650)
  
    def center_window(self,w,h):
        ws = self.root.winfo_screenwidth()
        hs = self.root.winfo_screenheight()
        x = (ws / 2) - (w / 2)
        y = (hs / 2) - (h / 2)
        self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
  
    # Think lag comes from this function
    def _update_tree(self):
        processes = get_windows_processes(get_all_windows())
        for children in self.tab1.get_children():
            self.tab1.delete(children)
        for process in processes:
            self.tab1.insert("", "end", values=process)
        
        #self.root.after(10000, self._update_tree) # updates after 10 seconds, current refresh rate is about 17-23 seconds
        self.t = Thread(target=self._update_tree)
        self.t.setDaemon(True)
        self.t.start()

    def start(self):
        #self.t = Thread(target=self._update_tree)
        #self.t.setDaemon(True)
        #self.t.start()

        self.root.after(1000, self._update_tree)
        #self.root.after(10000, self.t)
        self.center_window(400, 700)
        self.root.mainloop()




app().start()
print(threading.activeCount())

#print(processes)  // test output case1
#print(windows)  // test output case2
=======
# main control file
# 29 November, 2020
from threading import Thread
import threading
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
        login_scr(self.tab1, self.tab3, self.tab4, self.tab_control, self.root).make_login()
        register_scr(self.tab2, self.tab_control).make_register()

    def start(self):
        
        center_window(self.root, 400, 450)
        self.root.mainloop()

start_screen().start()
>>>>>>> f9b881fda5c433f3e404458e58b9043eb3f64158
