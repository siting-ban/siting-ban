############################################################################
# Title: At the Bottom of Niagara Falls
# Creator: Siting Ban
# Purpose: To create cluster animation of Niagara Falls using arrays
# Last Date Modified: 11/11/2019
############################################################################

from tkinter import *
from time import *
from random import *
from math import *
tk = Tk()
screen = Canvas(tk, width = 1200, height = 800, background = "light blue")
screen.pack()

#BACKGROUND
cliffColours = ["#b9a06d", "#b09764", "#a78f5c", "#9e8754", "#957e4b", "#8d7643", "#846e3b", "#7b6532", "#725d2a", "#695522", "#614d1a"]

fallsBackground = screen.create_polygon(0, 100, 50, 110, 100, 119, 150, 127, 200, 133, 250, 138, 300, 142, 350, 145,
                                        400, 147, 450, 148, 500, 149, 550, 150, 600, 150, 650, 148, 750, 147, 800, 146, 850, 145, 850, 800, 0, 800, fill = "white")
cliffTop = screen.create_polygon(850, 140, 875,137, 900, 138, 925, 135, 950, 133, 975, 136, 1000, 132, 1025, 138,
                              1050, 131, 1075, 132, 1100, 130, 1125, 131, 1150, 133, 1175, 135, 1200, 130,
                              1200, 150, 850, 150, fill = "#3a8539")
sun = screen.create_oval(-60, -60, 60, 60, fill = "yellow", outline = "yellow")

for i in range(11): #Bottom of the Cliff as a gradient
    size1 = 50
    y1 = (size1 * i) + 150
    y2 = y1 + size1
    cliffBottom = screen.create_rectangle(850, y1, 1200, y2, fill = cliffColours[i], outline = cliffColours[i])

fallShadow = screen.create_polygon(850, 150, 1200, 800, 850, 800, fill = "black")

#WATERFALL ARRAYS
numWater = 2450

x1 = []
y1 = []
length = []
width = []
y1Speed = []
colour = []
waterDrawings = []

for i in range(numWater):
    x1.append(randint(0, 850))
    y1.append(randint(150, 650))
    y1Speed.append(randint(10, 40))
    length.append(randint(10, 50))
    width.append(randint(2, 7))
    colour.append(choice(["#3770d0", "#5f8dda", "#88aae5", "#b1c7f0", "#dae5fb", "#7cbfc5", "#8cdbd8"]))
    waterDrawings.append(0)

#STEAM ARRAYS
numSteam = 750

x2 = []
y2 = []
size = []
x2Speed = []
y2Speed = []
colourSteam = []
steamDrawings = []

for i in range(numSteam):
    x2.append(randint(0, 900))
    y2.append(randint(650, 700))
    size.append(randint(10, 40))
    x2Speed.append(randint(-20, 20))
    y2Speed.append(randint(-10, 10))
    colourSteam.append(choice(["#dae7f4", "#e3edf6", "#ecf3f9", "#f5f9fc", "#ffffff"]))
    steamDrawings.append(0)

#RAILING ARRAYS
railing2 = [] #Empty array for all the railing parts

for i in range(150): #Number of railings
    railing2.append(0) #Add to the array


#PEOPLE ARRAYS
numPeople = 40

x3 = []
y3 = []
length2 = []
width2 = []
x3Speed = []
colourShirt = []
bodyDrawings = []

size2 = []
colourHead = []
headDrawings = []

for i in range(numPeople):
    x3.append(randint(859, 1250))
    y3.append(120)
    length2.append(20)
    width2.append(randint(5, 7))
    x3Speed.append(randint(-5, 5))
    colourShirt.append(choice(["red", "orange", "yellow", "blue", "green", "purple", "pink", "white", "black"]))
    bodyDrawings.append(0)

    size2.append(5)
    colourHead.append(choice(["#f7e4d2", "#e3d0ba", "#594121", "#e7d4b0"]))
    headDrawings.append(0)

#RAINBOW ARRAYS
numArcs = 7
x4 = [500]
y4 = []
radius = [400, 380, 360, 340, 320, 300, 280]
x4Speed = []
y4Speed = []
colourArc = ["red", "orange", "yellow", "green", "turquoise", "blue", "purple"]
rainbowDrawings = []

for i in range( numArcs ):
    x4.append(x4[i] - 50)
    y4.append(600)
    x4Speed.append(2)
    y4Speed.append(2)

    rainbowDrawings.append([]) #Add an array inside an array

    for n in range(200): #For the 200 lines that make up each arc
        rainbowDrawings[i].append(0) #Add a number for each array within the array of rainbowDrawings

    
#LAKE FOREGROUND
lakeForeground = screen.create_polygon(-50, 600, 1250, 700, 1250, 710, 1250, 900, -50, 950, -50, 700, fill = "#07609a", smooth = True)

while True: #To keep animation going forever
    
    #WATERFALL ANIMATION
    for i in range(numWater):
        waterDrawings[i] = screen.create_line(x1[i], y1[i], x1[i], y1[i] + length[i], fill = colour[i], width = width[i])
        y1[i] = y1[i] + y1Speed[i]

        if y1[i] > 650:
            y1[i] = 100

    #STEAM ANIMATION
    for i in range(numSteam):
        steamDrawings[i] = screen.create_oval(x2[i], y2[i], x2[i] + size[i], y2[i] + size[i], fill = colourSteam[i], outline = colourSteam[i])

        x2[i] = x2[i] + x2Speed[i]
        y2[i] = y2[i] + y2Speed[i]

        if x2[i] < -10:
            x2[i] = randint(0, 900)

        if x2[i] > 900:
            x2[i] = randint(0, 900)

        if y2[i] < 610:
            y2[i] = randint(620, 700) #So that the steam starts back somewhere near the middle, like actual steam

        if y2[i] > 710:
            y2[i] = randint(620, 700)

    #PEOPLE ANIMATION
    for i in range(numPeople):
        bodyDrawings[i] = screen.create_rectangle(x3[i], y3[i], x3[i] + width2[i], y3[i] + length2[i], fill = colourShirt[i], outline = colourShirt[i])
        headDrawings[i] = screen.create_oval(x3[i], y3[i] - size2[i], x3[i] + size2[i], y3[i], fill = colourHead[i], outline = colourHead[i])

        x3[i] = x3[i] + x3Speed[i]

        dieRoll = randint(1, 100)
        
        if dieRoll <= 5: #There's a 5% chance
            x3Speed[i] = 0 #Of people stopping to watch the falls

            for f in range(11):
                if f%10 == 0:
                    x3Speed[i] = randint(-5, 5) #After 10 frames, the person is free to move again 

        if x3[i] < 859:
            x3Speed[i] = 0 

            for f in range(6):
                if f%5 == 0:
                    x3Speed[i] = randint(0, 5)

        if x3[i] > 1220:
            x3Speed[i] = -1 * x3Speed[i]

    #RAINBOW DRAWING
    for n in range(200):
        for i in range(numArcs):
            x4[i] = 750 - radius[i] * cos (0.01 * n)
            y4[i] = 550 - radius[i] * sin (0.01 * n)

            rainbowDrawings[i][n] = screen.create_line(x4[i], y4[i], x4[i] + 50, y4[i] + 50, fill = colourArc[i])

    #SKY COVER
    skyCover = screen.create_polygon(0, 100, 50, 110, 100, 119, 150, 127, 200, 133, 250, 138, 300, 142, 350, 145,
                                        400, 147, 450, 148, 500, 149, 550, 150, 600, 150, 650, 148, 750, 147, 800, 146, 855, 145, 855, 100, 0, 100, fill = "light blue")

    #RAILING1
    railing1 = screen.create_line(854, 130, 1210, 130, fill = "black", width = 4)

    #RAILING2
    for r in range(150):
        xRail = 855 + r* 6
        yRail = 130
        railSize = 3
        railing2[r] = screen.create_line(xRail, yRail, xRail + railSize, yRail + 15, fill = "black") #Changing the values inside the railing2 array

    #UPDATE AND SLEEP
    screen.update()
    sleep(0.03) 
    
    #DELETE EVERYTHING 
    screen.delete(skyCover, railing1)

    for i in range(150):  
        screen.delete( railing2[i] ) #Delete all the railings

    for i in range(numWater):
        screen.delete(waterDrawings[i])

    for i in range(numSteam):
        screen.delete(steamDrawings[i])

    for i in range(numPeople):
        screen.delete(bodyDrawings[i])
        screen.delete(headDrawings[i])
        
    for n in range(200): 
        for i in range(numArcs): 
            screen.delete( rainbowDrawings[i][n] ) #Deletes the 200 values in the 7 arrays in the rainbowDrawings array
