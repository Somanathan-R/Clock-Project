import turtle 
import time
from tkinter import *
#from digital import *
import analog

root= Tk()
root.title("Choose your option")
root.geometry("400x400")



Button1 = Button(root, text="Digital",command=open(analog.draw_clock))
Button1.pack()

mainloop()