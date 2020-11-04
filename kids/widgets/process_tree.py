import tkinter

from tkinter import ttk
from tkinter.font import Font


def create_process_tree(container, processes):
    process_columns = ("PID", "NAME", "STATUS", "CPU", "MEMORY", "THREADS")

    tree = ttk.Treeview(container, columns=process_columns, show="headings")

    tree.grid(column=0, row=0, sticky="nsew", in_=container)

    for column in process_columns:
        tree.heading(column, text=column.title())
        tree.column(column, width=Font().measure(column.title()))

    for process in processes:
        tree.insert("", "end", values=process)

    container.grid_columnconfigure(0, weight=1)
    container.grid_rowconfigure(0, weight=1)

    return tree
