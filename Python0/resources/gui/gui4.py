# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 12:22:13 2023

@author: Andy Turner
"""
import tkinter as tk
import tkinter.ttk as ttk
import csv
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def read_data(path):
    """
    Read data.

    Parameters
    ----------
    path : String
        Path of the file to be read. The file is expected to be a rectangular 
        2D CSV format data with numerical values. 

    Returns
    -------
    data : List of lists
        The data in row major order.

    """
    f = open(path)
    data = []
    for line in csv.reader(f, quoting=csv.QUOTE_NONNUMERIC):
        row = []
        for value in line:
            row.append(value)
        data.append(row)
    f.close()
    #print(data)
    return data

def plot(p):
    """
    Redraws the canvas if there is a new power.

    Parameters
    ----------
    p : int
        The power to raise values to.

    Returns
    -------
    None.

    """
    global p0
    if p0 != p:
        figure.clear()
        #print(p)
        data_p = []
        #data.reverse()
        for row in data:
            row_p = []
            for val in row:
               row_p.append(val ** p)
            data_p.append(row_p)
        plt.imshow(data_p)
        plt.show()
        p0 = p
        canvas.draw()

def exiting():
    """
    Exit the program.
    """
    root.quit()
    root.destroy()
    """
    Exit the program.
    """
    root.quit()
    try:
        root.destroy()
    except Exception:
        pass

def update(x):
    """
    Updates scale_label and canvas.

    Parameters
    ----------
    x : str.
        Number.

    Returns
    -------
    None.

    """
    #print(x)
    #print(type(x))
    #print(scale.get())
    #print(int(float(scale.get())))
    # Integerise p
    p = int(float(scale.get()))
    scale_label.config(text='power=' + str(p))
    plot(p)

# Initialise figure
figure = matplotlib.pyplot.figure(figsize=(7, 7))
#ax = figure.add_axes([0, 0, 1, 1])

# Initialise data
data = read_data('../../data/input/in.txt')

# Initialise p0
p0 = None

# Create the tkinter window
root = tk.Tk()

# Create a canvas to display the figure
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(figure, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create a scale
scale = ttk.Scale(root, from_=1, to=10, command=update)
scale.pack()

# Create a Label widget to display scale value
scale_label = ttk.Label(root, text='Move the scale slider to choose a power and see an image.')
scale_label.pack()

# Create a Button widget and link this with the exiting function
exit_button = ttk.Button(root, text="Exit", command=exiting)
exit_button.pack()

# Exit if the window is closed.
root.protocol('WM_DELETE_WINDOW', exiting)

# Start the GUI
root.mainloop()