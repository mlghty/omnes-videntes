import tkinter as tk
import time
from threading import Thread
import threading
from kids.utils import login, registration, push_userdata, get_windows_processes, get_all_windows, push_appdata, get_appdata, get_userdata
from kids.gui import create_process_tree
from datetime import date, datetime
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 
# abandon all hope ye who enters here

tester = get_windows_processes(get_all_windows())

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
        self.test = get_windows_processes(get_all_windows())
        self.root = root
        self.test = "test"
    
    def get_processes(self):
        
        self.test = get_windows_processes(get_all_windows())
        return self.test

    def get_windows(self):

        return get_all_windows()

    # generates and updates the process tree
    def _update_tree(self):

        self.tab_control.add(self.tab, text ='Processes')

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

    def __init__(self, tab, tab2, tab3, tab4, tab5, tab_control, root):

        self.signin_label = tk.Label(tab, text = "Sign In", bg = 'white', font = ("Times 12"))
        self.username_field = tk.Entry(tab, bd = 2, font = ("Times 11 italic"))
        self.password_field = tk.Entry(tab, bd = 2, font = ("Times 11 italic"))

        self.login_button = tk.Button(tab, text = "Sign In", command = self.log_submit)
        self.login_error = tk.Label(tab, text = "One of the fields is incorrect. Please try again.", bg = 'white')

        self.tab_control = tab_control; self.root = root
        self.tab = tab; self.tab2 = tab2; self.tab3 = tab3; self.tab4 = tab4; self.tab5 = tab5

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

        self.username = self.username_field.get()
        self.password = self.password_field.get()

        x = login(self.username, self.password)

        if(x):
            
            self.root.title("Good Time")
            self.tab_control.hide(0)
            self.tab_control.hide(1)
            
            self.make_tabs()
        else:

            self.login_error.pack(side = 'bottom')

    # generates non-login tabs 
    def make_tabs(self):

        self.error_label = tk.Label(self.tab2, text = "Invalid text in input field. Please Try Again.", bg = 'white')
        self.save_label = tk.Label(self.tab2, text = "Save", bg = 'white', font = ("Times 12") )
        self.app_graphs_label = tk.Label(self.tab3, text = "App Graphs", bg = 'white', font = ("Times 11") )
        self.user_graphs_label = tk.Label(self.tab3, text = "Work Graphs", bg = 'white', font = ("Times 11") )
        self.other_label = tk.Label(self.tab3, text = "Other", bg = 'white', font = ("Times 11") )  

        self.tab_control.add(self.tab2, text ='Save')
        self.tab_control.add(self.tab3, text = "View")
        self.tab_control.add(self.tab4, text = "Graphs")

        start_data(self.tab_control, self.tab5, self.root)._update_tree()

        self.tab_control.tab(4, state = "disabled")
        self.tab_control.tab(5, state = "disabled")

        self.input_field = tk.Entry(self.tab2, bd = 2, font = ("Times 11 italic"))
        self.push_apps = tk.Button(self.tab2, text = "Push Apps")
        self.push_user = tk.Button(self.tab2, text = "Push Input")

        self.user_one_week = tk.Button(self.tab3, text = "1 Week")
        self.user_two_weeks = tk.Button(self.tab3, text = "2 Weeks")
        self.user_one_month = tk.Button(self.tab3, text = "1 Month")

        self.app_one_week = tk.Button(self.tab3, text = "1 Week")
        self.app_two_weeks = tk.Button(self.tab3, text = "2 Weeks")
        self.app_one_month = tk.Button(self.tab3, text = "1 Month")

        self.show_processes = tk.Button(self.tab3, text = "Show Processes")
        
        self.make_widgets()

    def get_week_appgraph(self, runtimes, app_names):

        fig = Figure(figsize = (5, 5), dpi = 100)
        ax1 = fig.add_subplot(111)  

        #fig1, ax1 = plt.subplots()
        ax1.pie(runtimes, labels = app_names, autopct='%1.1f%%', shadow=True, startangle = 90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                
        canvas = FigureCanvasTkAgg(fig, master = self.tab4) 
        canvas.get_tk_widget().pack()

    def get_week_usergraph(self, times):

        fig = Figure(figsize = (5, 5), dpi = 100)
        ax1 = fig.add_subplot(111)  

        #fig1, ax1 = plt.subplots()
        ax1.pie(times, labels = ["Total Time", "Worked Time"], autopct='%1.1f%%', shadow=True, startangle = 90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                
        canvas = FigureCanvasTkAgg(fig, master = self.tab4) 
        canvas.get_tk_widget().pack()  

    # clears username prompt
    def log_clear_username(self, event = None):

        self.username_field.delete(0, "end")
        self.username_field.configure(font = ("Times 12"))
    
    # clears password prompt
    def log_clear_password(self, event = None):

        self.password_field.delete(0, "end")
        self.password_field.configure(font = ("Times 12"), show = '*')

    def clear_input(self, event = None):

        self.input_field.delete(0, "end")
        self.input_field.configure(font = ("Times 12"))
    
    def show_app_processes(self, event = None):

        self.tab_control.tab(5, state = "normal")
        center_window(self.root, 700, 600)

    def push_user_data(self, event = None):

        self.user_hours = self.input_field.get()
        
        if (self.user_hours.isnumeric() != True):

            self.error_label.pack(side = 'top', pady = 45)
            return

        self.user_hours = int(self.user_hours)

        if(self.user_hours > 24):
            
            self.error_label.pack(side = 'top', pady = 45)
            return

        self.work = self.input_field.get()
        self.work = int(self.work)

        self.error_label.pack_forget()
        self.input_field.delete(0, "end")
        
        push_userdata(self.username, self.work)

    def push_app_data(self, event = None):

        process_tuple = tester
        process_size = len(process_tuple)
        
        for j in range(0, process_size):
            x = process_tuple[j]
            time = x[1]
            app_name = x[2]

            if (app_name == "Calculator") or (app_name == "Settings") or (app_name == "Microsoft Text Input Application"):
                continue

            app_time = x[3]
        
            app_time = str(app_time)
            app_time = app_time.split(':')

            _hours = app_time[0]
            _minutes = app_time[1]

            app_time = (int(_hours) * 60) + int(_minutes)

            today_list = x[0]
            today_list = today_list.split('/')
            day = today_list[1]
            month = today_list[0]
            year = today_list[2]
        
            push_appdata(self.username, day, month, year, time, app_name, app_time)

    def get_appdata_week(self, event = None):

        self.tab_control.tab(4, state = "normal")

        center_window(self.root, 700, 600)

        graph_processes = get_appdata(self.username)

        sizeoff = len(graph_processes)
        app_names = []
        runtimes = []

        for x in range(0, sizeoff):
            iterator = graph_processes[x]

            app_names.append(iterator[4])
            runtimes.append(iterator[5])
                
        self.get_week_appgraph(runtimes, app_names)

    
    def get_appdata_weeks(self, event = None):
        self.tab_control.tab(4, state = "normal")
        center_window(self.root, 700, 600)


        graph_processes = get_appdata(self.username)

        sizeoff = len(graph_processes)
        app_names = []
        runtimes = []

        for x in range(0, sizeoff):
            iterator = graph_processes[x]

            app_names.append(iterator[4])
            runtimes.append(iterator[5])
                
        self.get_week_appgraph(runtimes, app_names)
    
    def get_appdata_month(self, event = None):
        self.tab_control.tab(4, state = "normal")

        center_window(self.root, 700, 600)
        graph_processes = get_appdata(self.username)

        sizeoff = len(graph_processes)
        app_names = []
        runtimes = []

        for x in range(0, sizeoff):
            iterator = graph_processes[x]

            app_names.append(iterator[4])
            runtimes.append(iterator[5])
                
        self.get_week_appgraph(runtimes, app_names)
    
    def get_usrdata_week(self, event = None):
        self.tab_control.tab(4, state = "normal")

        center_window(self.root, 700, 600)
        graph_processes = get_userdata(self.username)

        sizeoff = len(graph_processes)
        worked_time = 0

        for x in range(0, sizeoff):
            iterator = graph_processes[x]

            worked_time += (iterator[4])
        
        passer = [(7 * 24), worked_time]
                
        self.get_week_usergraph(passer)
    
    def get_usrdata_weeks(self, event = None):

        self.tab_control.tab(4, state = "normal")

        center_window(self.root, 700, 600)
        graph_processes = get_userdata(self.username)

        sizeoff = len(graph_processes)
        worked_time = 0

        for x in range(0, sizeoff):
            iterator = graph_processes[x]

            worked_time += (iterator[4])
        
        passer = [(14 * 24), worked_time]
                
        self.get_week_usergraph(passer)
    
    def get_usrdata_month(self, event = None):

        self.tab_control.tab(4, state = "normal")

        center_window(self.root, 700, 600)
        graph_processes = get_userdata(self.username)

        sizeoff = len(graph_processes)
        worked_time = 0

        for x in range(0, sizeoff):
            iterator = graph_processes[x]

            worked_time += (iterator[4])
        
        passer = [(28 * 24), worked_time]
                
        self.get_week_usergraph(passer)

    def make_widgets(self):

        self.save_label.pack(side = 'top', pady = 50)
        self.input_field.pack(side = 'top')
        self.input_field.insert(0, 'Hours of work today')
        self.input_field.bind("<Button-1>", self.clear_input)
        self.push_apps.bind("<Button-1>", self.push_app_data)
        self.push_apps.pack(side = 'bottom', pady = 50)
        self.push_user.bind("<Button-1>", self.push_user_data)
        self.push_user.pack(side = 'bottom')

        self.user_graphs_label.pack(side = 'top', pady = 15)
        self.user_one_week.bind("<Button-1>", self.get_usrdata_week)
        self.user_one_week.pack(side = 'top', pady = 5)
        self.user_two_weeks.bind("<Button-1>", self.get_usrdata_weeks)
        self.user_two_weeks.pack(side = 'top', pady = 5)
        self.user_one_month.bind("<Button-1>", self.get_usrdata_month)
        self.user_one_month.pack(side = 'top', pady = 5)

        self.app_graphs_label.pack(side = 'top', pady = 15)
        self.app_one_week.bind("<Button-1>", self.get_appdata_week)
        self.app_one_week.pack(side = 'top', pady = 5)
        self.app_two_weeks.bind("<Button-1>", self.get_appdata_weeks)
        self.app_two_weeks.pack(side = 'top', pady = 5)
        self.app_one_month.bind("<Button-1>", self.get_appdata_month)
        self.app_one_month.pack(side = 'top', pady = 5)

        self.other_label.pack(side = 'top', pady = 15)
        self.show_processes.bind("<Button-1>", self.show_app_processes)
        self.show_processes.pack(side = 'top')

    # positions widgets for login screen
    def make_login(self):

        self.signin_label.pack(side = 'top', pady = 30)

        self.username_field.insert(0, 'Enter Username')
        self.username_field.bind("<Button-1>", self.log_clear_username)
        self.username_field.pack(side = 'top', pady = 30)

        self.password_field.insert(0, 'Enter Password')
        self.password_field.bind("<Button-1>", self.log_clear_password)
        self.password_field.pack(side = 'top')

        self.login_button.pack(side = 'bottom', pady = 30)

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