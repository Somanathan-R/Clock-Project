import sys
import tkinter as tk
import os
import time	
from threading import Timer



root=tk.Tk()
root.title("Digital Clock")   #the title 
holdsecs = 1.0 
cw, ch = 250, 250 
b=0
canvas = tk.Canvas(root, width=cw, height=ch, borderwidth=b,
highlightthickness=0, bg='black')

label = tk.Label(root, width = 20, height = 1, bg = 'light blue') 

def drawface(canvas, framewh=[]):
    border = 20 
    framewidth=20
    frame = (border, border, framewh[0] - border, framewh[1] - border)
    canvas.create_oval (frame, fill = 'brown')
    
    bpf = border + framewidth 
    face = (bpf, bpf, frame[2] - framewidth, frame[3] - framewidth)
    canvas.create_oval (face, fill = 'white')

def drawlabel(now=''): 
    label.config (text = now)

def dismiss():  
    os._exit(0)

def process(canvas): 
    now = timeinfo()[3]
    drawlabel(now)

def run():
    process(canvas)
    global timer
    timer.cancel()
    timer = Timer (holdsecs, run)
    timer.start()

#to display the current time in our area
def timeinfo():
    lt = time.localtime()
    year = lt[0]
    month=lt[1]
    day=lt[2]
    hour = lt[3]
    minute=lt[4]
    second=lt[5]
    hour12 = hour % 12
    
    #to see if its am or its pm
    if hour12 == 0: hour12 = 12
    ampm = (' AM', ' PM')[int(hour/12)]
    nowasc = '{0:d}:{1:02d}:{2:02d}'.format(hour12, minute, second) + ampm
    mons = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
        'Nov', 'Dec')

    date = '{0:s} {1:d}, {2:d}'.format(mons[month-1], day, year)
    nowasc = date + ' ' + nowasc
    return (hour12, minute, second, nowasc)

timer = Timer (holdsecs, run)
canvas.pack()
label.place (x = cw/2 - 70, y = ch/2 - 8) 
drawface (canvas, framewh=(cw, ch))
root.protocol('WM_DELETE_WINDOW', dismiss)

run()

root.mainloop()


