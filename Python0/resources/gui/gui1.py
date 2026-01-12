# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 14:06:03 2023

@author: agdtu
"""
import tkinter as tk

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
label = tk.Label(root, text=str(i))
# Create a Button widget and link this with the increment function
increment_button = tk.Button(root, text="Increment", command=increment)
# Create a Button widget and link this with the exiting function
exit_button = tk.Button(root, text="Exit", command=exiting)

# Pack widgets so they are visible.
label.pack()
increment_button.pack()
exit_button.pack()
 
# Start the GUI
root.mainloop()
