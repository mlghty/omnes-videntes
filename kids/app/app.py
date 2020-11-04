import tkinter
import time

from tkinter import ttk

from kids.utils import get_all_windows,  get_windows_processes
from kids.widgets import create_process_tree


class App:
    def __init__(self):
        """ Creates a new window"""
        self.root = tkinter.Tk()

        self.root.title("Spy Kids 5")
        self.root.geometry("600x600")

        self._create_widgets()

    def _create_widgets(self):
        self.notebook = ttk.Notebook(self.root)

        processes = get_windows_processes(get_all_windows())

        self.tree = create_process_tree(self.notebook, processes)

        self.notebook.add(self.tree, text="Apps")
        self.notebook.pack(expand=True, fill="both")

    def _update_tree(self):
        """ Updates every second. """
        processes = get_windows_processes(get_all_windows())

        for children in self.tree.get_children():
            self.tree.delete(children)

        for process in processes:
            self.tree.insert("", "end", values=process)

        self.root.after(1000, self._update_tree)

    def start(self):
        self.root.after(1000, self._update_tree)
        self.root.mainloop()
