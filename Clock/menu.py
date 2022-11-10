import tkinter as tk
from tkinter import *
root=Tk()
root.title("CLOCK")
root.configure(bg='purple')

tk.Button(root, text = "STOPWATCH",height =2,width=50,fg="black",bg="light green").grid(row=1, column=0, pady = (0,5))
tk.Button(root, text = "ANALOG CLOCK",height =2,width=50,fg="red",bg="light blue").grid(row=2, column=0,pady = (0,5))
tk.Button(root, text = "COUNT DOWN",height =2,width=50,fg="dark blue",bg="orange").grid(row=3, column=0,pady = (0,5))
tk.Button(root, text = "DATE PICKER",height =2,width=50,).grid(row=4, column=0,pady = (0,5))
tk.Button(root, text = "ALARM CLOCK",height =2,width=50,fg="dark blue",bg= "orange").grid(row=5, column=0,pady = (0,5))
tk.Button(root, text = "DIGITAL CLOCK",height =2,width=50,fg="red",bg="light blue").grid(row=6, column=0,pady = (0,5))
tk.Button(root, text = "CALCULATOR",height =2,width=50,fg="black",bg="light green").grid(row=7, column=0,pady = (0,5))
root.mainloop()