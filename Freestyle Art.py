###############################################################################
#Title: Freestyle Art
#Creator: Siting Ban
#Purpose: To create a detailed picture using different techniques such as random
#           patterns, smoothed polygons, lines, text, arcs, ovals, rectangles...
#Date Last Modified:
###############################################################################

from tkinter import *
from time import *
from random import *
from math import *
tk = Tk()
screen = Canvas(tk, width=1000,height=800, background="white")
screen.pack()

y1 = 400
y2 = y1 + 50

for colour in ["#EECFA1", "#FFDEAD", "#FFE4B5", "#EEEED1", "#FFFFE0", "#E0FFFF", "#D1EEEE", "#B2DFEE","#ADD8E6", "#9AC0CD"]:
    screen.create_rectangle(0, y1, 1000, y2, fill = colour, outline = colour)
    y1 = y1 - 50
    y2 = y1 + 50
    

#Foreground
sunrise = screen.create_arc(375, 350, 625, 615, start=0, extent=180, fill="#EEC900", outline = "#EEC900")
hill3 = screen. create_polygon(-100, 260, 100, 200, 150, 150, 200, 50, 250, 170, 300, 150, 350, 300, 450, 400, 500, 500, -100, 500, fill = "#556B2F")
hill2 = screen.create_polygon(1100, 270, 900, 300, 800, 330, 700, 350, 600, 420, 500, 475, 400, 520, 400, 800, 1100, 800, fill = "#6B8E23")
hill1 = screen.create_polygon(-100, 400, 200, 420, 300, 450, 450, 480, 550, 510, 650, 500, 750, 480, 1100, 470 , 1000, 800, 0, 800, fill = "#9ACD32")
land = screen.create_rectangle(0, 600, 1000, 800, fill = "#B3EE3A", outline = "#A2CD5A", width = 10)
pond = screen.create_polygon(50, 650, 250, 670, 550, 630, 800, 680, 1000, 700, 950, 750, 50, 750, fill = "#96CDCD", smooth = True)

for n in range(30):
    x1 = randint(100,850)
    x2 = x1 + 30
    y1 = randint(670, 730)
    y2 = y1
    lines = screen.create_line(x1, y1, x2, y2, fill = "white")

#Trees
for n in range(30):
    x1 = randint(50, 950)
    x2 = x1 + 15
    y1 = randint(460, 550)
    y2 = y1 + 50
    screen.create_rectangle(x1, y1, x2, y2, fill = "#4d2600", outline = "#4d2600")

    for f in range(25):
        x3 = x1 - 20
        x4 = x2 + 20
        y3 = y1 - 40
        y4 = y1
        s = randint(7, 15)
        x5 = randint(x3, x4)
        y5 = randint(y3, y4)
        screen.create_oval(x5, y5, x5 + s, y5 + s, fill = "#009900" , outline = "#009900")

    for f in range(25):
        x3 = x1 - 20
        x4 = x2 + 20
        y3 = y1 - 40
        y4 = y1
        s = randint(7, 15)
        x5 = randint(x3, x4)
        y5 = randint(y3, y4)
        screen.create_oval(x5, y5, x5 + s, y5 + s, fill = "#008000" , outline = "#008000")

    for f in range(25):
        x3 = x1 - 20
        x4 = x2 + 20
        y3 = y1 - 40
        y4 = y1
        s = randint(7, 15)
        x5 = randint(x3, x4)
        y5 = randint(y3, y4)
        screen.create_oval(x5, y5, x5 + s, y5 + s, fill = "#006600" , outline = "#006600")
    
    for f in range(25):
        x3 = x1 - 20
        x4 = x2 + 20
        y3 = y1 - 40
        y4 = y1
        s = randint(7, 15)
        x5 = randint(x3, x4)
        y5 = randint(y3, y4)
        screen.create_oval(x5, y5, x5 + s, y5 + s, fill = "#004d00" , outline = "#004d00")

#Birds
for n in range(6):
    x1 = 30*n + 650
    y1 = 200 - 13*n
    x2 = x1 + 10
    y2 = y1 + 2
    x3 = x1 + 15
    y3 = y1 + 5
    x4 = x1 + 20
    y4 = y2
    x5 = x1 + 30
    y5 = y1
    screen.create_line(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, fill = "black", width = 2.3, smooth = True)

#Text
screen.create_text(850, 770, text = "Be at peace ~ Siting Ban", font = "Times 16 italic", fill = "black")
    
