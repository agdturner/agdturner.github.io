# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 12:22:13 2023

@author: agdtu
"""
import tkinter as tk
import tkinter.ttk as ttk

def increment():
    global i
    i = i + 1
    label.config(text=str(i))

def exiting():
    """
    Exit the program.
    """
    root.quit()
    root.destroy()
    #sys.exit(0)


def update_scale_label(val):
    #print(val)
    #print(scale.get())
    #print(str(int(float(scale.get()))))
    scale_label.config(text=str(int(float(scale.get()))))
    
# Create the tkinter window
root = tk.Tk()

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
increment_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Options", menu=increment_menu)
increment_menu.add_command(label="Increment", command=increment)
exit_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Exit", menu=exit_menu)
exit_menu.add_command(label="Exit", command=exiting)

i = 0
# Create a scale
scale = ttk.Scale(root, from_=0, to=100,command=update_scale_label)
# Create a Label widget to display scale value
scale_label = ttk.Label(root, text=str(scale.get()))
# Create a Label widget
label = ttk.Label(root, text=str(i))
# Create a Button widget and link this with the increment function
increment_button = ttk.Button(root, text="Increment", command=increment)
# Create a Button widget and link this with the exiting function
exit_button = ttk.Button(root, text="Exit", command=exiting)

# Pack widgets so they are visible.
scale.pack()
scale_label.pack()
label.pack()
increment_button.pack()
exit_button.pack()

# Exit if the window is closed.
root.protocol('WM_DELETE_WINDOW', exiting)

# Start the GUI
root.mainloop()