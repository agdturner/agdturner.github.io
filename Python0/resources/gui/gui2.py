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
    
# Create the tkinter window
root = tk.Tk()
i = 0
# Create a Label widget
label = ttk.Label(root, text=str(i))
# Create a Button widget and link this with the increment function
increment_button = ttk.Button(root, text="Increment", command=increment)
# Create a Button widget and link this with the exiting function
exit_button = ttk.Button(root, text="Exit", command=exiting)

# Pack widgets so they are visible.
label.pack()
increment_button.pack()
exit_button.pack()
 
# Start the GUI
root.mainloop()