#this is for calender
#calender
import tkinter
from tkinter import *
import calendar 

def showCal() : 
    cal_gui = Tk() 
    cal_gui.config(background = "white") 
    cal_gui.title("CALENDER")  
    cal_gui.geometry("600x600")  

    fetch_year = int(year_field.get())

    cal_content=calendar.calendar(fetch_year) 
    cal_year = Label(cal_gui, text = cal_content, font = "Consolas 10 bold") 
    cal_year.grid(row = 5, column = 1, padx = 20) 

    cal_gui.mainloop()


if __name__ == "__main__" : 
    gui = Tk() 
    gui.config(background = "white") 
    gui.title("CALENDER") 
    gui.geometry("250x140") 

    cal = Label(gui, text = "CALENDAR", bg = "dark gray", 

                            font = ("consolas", 28, 'bold')) 

    year = Label(gui, text = "Enter Year", bg = "light green") 

    year_field = Entry(gui) 

    Show = Button(gui, text = "Show Calendar", fg = "Black", 

                              bg = "Red", command = showCal) 

    Exit = Button(gui, text = "Exit", fg = "Black", bg = "Red", command = exit)


    cal.grid(row = 1, column = 1) 
    year.grid(row = 2, column = 1) 

    year_field.grid(row = 3, column = 1) 

    Show.grid(row = 4, column = 1) 
    Exit.grid(row = 6, column = 1)  

    gui.mainloop()