################################################################################
# Title: Rainbow Run
# Creator: Siting Ban
# Purpose: To create an obstacle game where the player starts with a certain number
#           of lives, which decreases when the player hits an obstacle. The objective
#           is to not hit 0 lives to gain a higher score
# Last Date Modified: 22/01/2020
################################################################################

from tkinter import *
from time import *
from random import *
from math import *

root = Tk()
screen = Canvas(root, width = 1000, height = 800, background = "light blue")


################################# SET & CREATE VALUES ##############################

def setInitialValues(): #Set empty or initial values of all objects in the game

#GENERAL VALUES
    global score, QPressed, gameRun, bar

    score = 0
    bar = 0
    QPressed = False
    gameRun = True

#BACKGROUND COLOURS
    global sideBarColours

    sideBarColours = ["#0c10bb", "#1517cb", "#1f1edb", "#2825eb", "#322dfb"]

#PLAYER VALUES
    global xPlayer, yPlayer, xSpeedPlayer, playerDrawing, playerLives

    xPlayer = 500
    yPlayer = 600
    xSpeedPlayer = 0
    playerDrawing = 0
    playerLives = 0

#DECREASE BOX VALUES
    global xDecreaseBox1, yDecreaseBox1, xDecreaseBox2, yDecreaseBox2, xDecreaseBox3, yDecreaseBox3
    global decreaseNum1, decreaseNum2, decreaseNum3, dNumDrawing1, dNumDrawing2, dNumDrawing3
    global numDecreaseBox1, numDecreaseBox2, numDecreaseBox3
    global decreaseBoxDrawing1, decreaseBoxDrawing2, decreaseBoxDrawing3
    global xChoicesOriginal, xChoices, decreaseBoxColours

    xDecreaseBox1 = []          #Positional values of row 1 of decrease boxes
    yDecreaseBox1 = []
    xDecreaseBox2 = []          #Positional values of row 2 of decrease boxes
    yDecreaseBox2 = []
    xDecreaseBox3 = []          #Positional values of row 3 of decrease boxes
    yDecreaseBox3 = []

    decreaseNum1 = []           #The number of lives that the player would decrease by if they hit the box
    decreaseNum2 = []
    decreaseNum3 = []
    dNumDrawing1 = []
    dNumDrawing2 = []
    dNumDrawing3 = []
    
    numDecreaseBox1 = randint(minNumDecreaseBox1, maxNumDecreaseBox1)
    numDecreaseBox2 = randint(minNumDecreaseBox2, maxNumDecreaseBox2)
    numDecreaseBox3 = randint(minNumDecreaseBox3, maxNumDecreaseBox3)

    decreaseBoxDrawing1 = []
    decreaseBoxDrawing2 = []
    decreaseBoxDrawing3 = []

    decreaseBoxColours = ["#ffb1b0", "#ffdfbe", "#ffffbf", "#b4f0a7", "#97f6dc", "#a9d1f7", "#cc99ff"]

    xChoicesOriginal = [100, 200, 300, 400, 500, 600, 700]          #Possible values for the x position of the box
    xChoices = xChoicesOriginal.copy()

#INCREASE CIRCLE VALUES
    global xIncreaseCircle, yIncreaseCircle
    global numIncreaseCircle, increaseCircleDrawing

    xIncreaseCircle = []
    yIncreaseCircle = []
    
    numIncreaseCircle = randint(minNumIncreaseCircle, maxNumIncreaseCircle)
    increaseCircleDrawing = []


def createInitialObjects(): #Create initial values for array objects (Decrease Boxes, Increase Circle)

#DECREASE BOX
    global decreaseBoxDrawing1, xDecreaseBox1, yDecreaseBox1, xDecreaseBox2, yDecreaseBox2
    global decreaseNum1, decreaseNum2, decreaseNum3, dNumDrawing1, dNumDrawing2, dNumDrawing3
    global decreaseBoxDrawing2, xDecreaseBox3, yDecreaseBox3, decreaseBoxDrawing3, xChoices

    for i in range(numDecreaseBox1):                            #For the number of decrease boxes in that row
        xDecreaseBox1.append(choice(xChoices))                  #Add a random x value for the box
        yDecreaseBox1.append(-100)                              #Add the same y value so it stays in a row
        decreaseNum1.append(randint(1, 20))                     #Add a random number to decrease the lives by if the box is hit
        dNumDrawing1.append(0)
        decreaseBoxDrawing1.append(0)

        xChoices.remove(xDecreaseBox1[i])                       #Remove the choice of the x value so that boxes don't overlap

    xChoices = xChoicesOriginal.copy()                          #Reset the xChoices into the copy of the original

    for i in range(numDecreaseBox2):
        xDecreaseBox2.append(choice(xChoices))
        yDecreaseBox2.append(-350)
        decreaseNum2.append(randint(1, 20))
        dNumDrawing2.append(0)
        decreaseBoxDrawing2.append(0)

        xChoices.remove(xDecreaseBox2[i])

    xChoices = xChoicesOriginal.copy()

    for i in range(numDecreaseBox3):
        xDecreaseBox3.append(choice(xChoices))
        yDecreaseBox3.append(-600)
        decreaseNum3.append(randint(1, 20))
        dNumDrawing3.append(0)
        decreaseBoxDrawing3.append(0)

        xChoices.remove(xDecreaseBox3[i])

    xChoices = xChoicesOriginal.copy()

#INCREASE CIRCLE
    global increaseCircleDrawing, xIncreaseCircle, yIncreaseCircle

    for i in range(numIncreaseCircle):
        xIncreaseCircle.append(choice([130, 230, 330, 430, 530, 630]))
        yIncreaseCircle.append(-200)
        increaseCircleDrawing.append(0)



################################# DRAW OBJECTS #################################

def drawBackground(): #Draw the game background
    global clouds, leftBar, rightBar, leftBorder, rightBorder, qText

    clouds = []         #Create arrays for the objects to be drawn
    leftBar = []
    rightBar = []
    leftBorder = []
    rightBorder = []
    
    for i in range(300):    #Fill the arrays with the drawings
        x = randint(50, 900)
        y = randint(700, 800)
        size = randint(20, 70)
        clouds.append(screen.create_oval(x, y, x+size, y+size, fill = "white", outline = choice(["#e0e0e0", "#e6faf9"])))

    for i in range(int(800/50)):
        for n in range(2):
            leftBar.append(screen.create_rectangle(49*n, 50*i, 49+50*n, 50+50*i, fill = choice(sideBarColours), outline = choice(sideBarColours)))
        for n in range(4):
            rightBar.append(screen.create_rectangle(800+50*n, 50*i, 850+50*n, 50+50*i, fill = choice(sideBarColours), outline = choice(sideBarColours)))
            
        leftBorder.append(screen.create_rectangle(45, 50*i, 95, 50+50*i, fill = "yellow", outline = "white", width = 10))
        rightBorder.append(screen.create_rectangle(805, 50*i, 855, 50+50*i, fill = "yellow", outline = "white", width = 10))

    qText = screen.create_text(930, 200, text = "Press Q \n to Quit", font = "System 20", fill = "white")


def drawPlayer(): #Draw the player and the lives of the player
    global playerDrawing, playerLives

    playerDrawing = screen.create_oval(xPlayer, yPlayer, xPlayer + 60, yPlayer + 60, fill = "blue")
    playerLives = screen.create_text(xPlayer + 30, yPlayer + 30, text = str(lives), font = "Georgia 15", fill = "white")


def drawDecreaseBox(): #Draw the decrease boxes and the numbers on them
    global decreaseBoxDrawing1, decreaseBoxDrawing2, decreaseBoxDrawing3
    global dNumDrawing1, dNumDrawing2, dNumDrawing3

    for i in range(numDecreaseBox1):
        decreaseBoxDrawing1[i] = screen.create_rectangle(xDecreaseBox1[i], yDecreaseBox1[i], xDecreaseBox1[i] + 100, yDecreaseBox1[i] + 100, fill = decreaseBoxColours[i],
                                                         outline = "white", width = 4)
        dNumDrawing1[i] = screen.create_text(xDecreaseBox1[i] + 50, yDecreaseBox1[i] + 50, text = str(decreaseNum1[i]), font = "Georgia 20", fill = "black")

    for i in range(numDecreaseBox2):
        decreaseBoxDrawing2[i] = screen.create_rectangle(xDecreaseBox2[i], yDecreaseBox2[i], xDecreaseBox2[i] + 100, yDecreaseBox2[i] + 100, fill = decreaseBoxColours[i],
                                                          outline = "white", width = 4)
        dNumDrawing2[i] = screen.create_text(xDecreaseBox2[i] + 50, yDecreaseBox2[i] + 50, text = str(decreaseNum2[i]), font = "Georgia 20", fill = "black")

    for i in range(numDecreaseBox3):
        decreaseBoxDrawing3[i] = screen.create_rectangle(xDecreaseBox3[i], yDecreaseBox3[i], xDecreaseBox3[i] + 100, yDecreaseBox3[i] + 100, fill = decreaseBoxColours[i],
                                                          outline = "white", width = 4)
        dNumDrawing3[i] = screen.create_text(xDecreaseBox3[i] + 50, yDecreaseBox3[i] + 50, text = str(decreaseNum3[i]), font = "Georgia 20", fill = "black")


def drawIncreaseCircle(): #Draw the increase circles
    global increaseCircleDrawing

    for i in range(numIncreaseCircle):
        increaseCircleDrawing[i] = screen.create_oval(xIncreaseCircle[i], yIncreaseCircle[i], xIncreaseCircle[i] + 40, yIncreaseCircle[i] + 40, fill = "green")


################################## UPDATE OBJECTS ################################

def updatePlayer():
    global xPlayer, yPlayer, xSpeedPlayer

    if xPlayer < 107:           #If the x value of the player is less than the border value
        xSpeedPlayer = 0        #Make the speed of the player 0
        xPlayer = 108           #And return them to 1 more than the border value

    elif xPlayer > 737:
        xSpeedPlayer = 0
        xPlayer = 736

    xPlayer = xPlayer + xSpeedPlayer        #Update the x value of the player


def updateDecreaseBox():
    global decreaseBoxDrawing1, xDecreaseBox1, yDecreaseBox1, xDecreaseBox2, yDecreaseBox2
    global decreaseNum1, decreaseNum2, decreaseNum3, dNumDrawing1, dNumDrawing2, dNumDrawing3
    global decreaseBoxDrawing2, xDecreaseBox3, yDecreaseBox3, decreaseBoxDrawing3, xChoices
    global numDecreaseBox1, numDecreaseBox2, numDecreaseBox3

    if yDecreaseBox1[0] > 600:                                              #If the y value of the row touches the bottom (clouds)
        for i in range(numDecreaseBox1):                                    #Delete the drawing of those boxes
            screen.delete(decreaseBoxDrawing1[i])
            screen.delete(dNumDrawing1[i])
        
        numDecreaseBox1 = randint(minNumDecreaseBox1, maxNumDecreaseBox1)   #Assign a new number of boxes in the row
        xDecreaseBox1 = []                                                  #Set the arrays for the boxes back to nothing
        yDecreaseBox1 = []
        decreaseNum1 = []
        decreaseBoxDrawing1 = []
        dNumDrawing1 = []
        
        for i in range(numDecreaseBox1):                                    #Reassign new x + y values, decrease numbers according to the number of decrease boxes in that row
            xDecreaseBox1.append(choice(xChoices))                              #This is like the loop in createInitialValues()
            yDecreaseBox1.append(-100)
            decreaseNum1.append(randint(1, 20))
            
            decreaseBoxDrawing1.append(0)
            dNumDrawing1.append(0)
            xChoices.remove(xDecreaseBox1[i])

        xChoices = xChoicesOriginal.copy()

    if yDecreaseBox2[0] > 600:
        for i in range(numDecreaseBox2):
            screen.delete(decreaseBoxDrawing2[i])
            screen.delete(dNumDrawing2[i])
            
        numDecreaseBox2 = randint(minNumDecreaseBox2, maxNumDecreaseBox2)
        xDecreaseBox2 = []
        yDecreaseBox2 = []
        decreaseNum2 = []
        decreaseBoxDrawing2 = []
        dNumDrawing2 = []
        
        for i in range(numDecreaseBox2):
            xDecreaseBox2.append(choice(xChoices))
            yDecreaseBox2.append(-100)
            decreaseNum2.append(randint(1, 20))
            
            decreaseBoxDrawing2.append(0)
            dNumDrawing2.append(0)
            xChoices.remove(xDecreaseBox2[i])

        xChoices = xChoicesOriginal.copy()
        
    if yDecreaseBox3[0] > 600:
        for i in range(numDecreaseBox3):
            screen.delete(decreaseBoxDrawing3[i])
            screen.delete(dNumDrawing3[i])
            
        numDecreaseBox3 = randint(minNumDecreaseBox3, maxNumDecreaseBox3)
        xDecreaseBox3 = []
        yDecreaseBox3 = []
        decreaseNum3 = []
        decreaseBoxDrawing3 = []
        dNumDrawing3 = []
        
        for i in range(numDecreaseBox3):
            xDecreaseBox3.append(choice(xChoices))
            yDecreaseBox3.append(-100)
            decreaseNum3.append(randint(1, 20))
            
            decreaseBoxDrawing3.append(0)
            dNumDrawing3.append(0)
            xChoices.remove(xDecreaseBox3[i])

        xChoices = xChoicesOriginal.copy()
        
    for i in range(numDecreaseBox1):    #Updates the y values of the decrease boxes
        yDecreaseBox1[i] = yDecreaseBox1[i] + ySpeedGeneral

    for i in range(numDecreaseBox2):
        yDecreaseBox2[i] = yDecreaseBox2[i] + ySpeedGeneral

    for i in range(numDecreaseBox3):
        yDecreaseBox3[i] = yDecreaseBox3[i] + ySpeedGeneral


def updateIncreaseCircle():
    global increaseCircleDrawing, xIncreaseCircle, yIncreaseCircle, numIncreaseCircle

    if yIncreaseCircle[0] > 660:                                                #If the y value of the increase circle touches the bottom (clouds)
        for i in range(numIncreaseCircle):                                      #Delete the present circle
            screen.delete(increaseCircleDrawing[i])
            
        numIncreaseCircle = randint(minNumIncreaseCircle,maxNumIncreaseCircle)  #Reset a number of increase circles
        xIncreaseCircle = []                                                    #Reset the arrays
        yIncreaseCircle = []
        increaseCircleDrawing = []
        
        for i in range(numIncreaseCircle):                                      #Add values to the array according to the number of increase circles
            xIncreaseCircle.append(choice([130, 230, 330, 430, 530, 630]))          #This is like the loop in createInitialValues
            yIncreaseCircle.append(yDecreaseBox1[i] - 95)
            increaseCircleDrawing.append(0)

    for i in range(numIncreaseCircle):  #Updates the y values of the increase circles
        yIncreaseCircle[i] = yIncreaseCircle[i] + ySpeedGeneral


def collisionUpdate():
#DECREASE BOX
    global decreaseBoxDrawing1, decreaseBoxDrawing2, decreaseBoxDrawing3, lives, ySpeedGeneral, xSpeedPlayer

    rangeNum = 0
    
    for i in range(numDecreaseBox1):    #Checks all the boxes in the row
        #If the player's y value is between the y value of the decrease box and that y value plus the speed (so that it is always able to catch the player)
        #AND the player's middle point is inbetween the x values of the box
        if yDecreaseBox1[i] + 100 + ySpeedGeneral > yPlayer >= yDecreaseBox1[i] + 100 and xDecreaseBox1[i] < xPlayer + 30 < xDecreaseBox1[i] + 100:
            while rangeNum < decreaseNum1[i]:       #Then the player's lives gets decreased by the number on the box
                lives = lives - 1
                rangeNum = rangeNum + 1

    rangeNum = 0
    
    for i in range(numDecreaseBox2):
        if yDecreaseBox2[i] + 100 + ySpeedGeneral > yPlayer >= yDecreaseBox2[i] + 100 and xDecreaseBox2[i] < xPlayer + 30 < xDecreaseBox2[i] + 100:
            while rangeNum < decreaseNum2[i]:
                lives = lives - 1
                rangeNum = rangeNum + 1

    rangeNum = 0

    for i in range(numDecreaseBox3):
        if yDecreaseBox3[i] + 100 + ySpeedGeneral > yPlayer >= yDecreaseBox3[i] + 100 and xDecreaseBox3[i] < xPlayer + 30 < xDecreaseBox3[i] + 100:
            while rangeNum < decreaseNum3[i]:
                lives = lives - 1
                rangeNum = rangeNum + 1

    rangeNum = 0

#INCREASE CIRCLE
    for i in range(numIncreaseCircle):  #Checks all the circles that are on screen
        #If the distance between the center point of the player and the circle is under 11
        if getDistance(xIncreaseCircle[i] + 20, yIncreaseCircle[i] + 20, xPlayer + 30, yPlayer + 30) < 11:
            lives = lives + 1                   #Then the player's lives increase while the distance is under 11
            rangeNum = rangeNum + 1


#################################### LEVELS ######################################

def easyLevel():    #Set values for the easy level
    global maxNumDecreaseBox1, maxNumDecreaseBox2, maxNumDecreaseBox3, minNumDecreaseBox1, minNumDecreaseBox2, minNumDecreaseBox3
    global maxNumIncreaseCircle, minNumIncreaseCircle, ySpeedGeneral, lives
    global easyButton, mediumButton, hardButton, intro, introBoxes, introBorder

    minNumDecreaseBox1 = 3      #The minimum number of decrease boxes in a row
    minNumDecreaseBox2 = 3
    minNumDecreaseBox3 = 3

    maxNumDecreaseBox1 = 6      #The maximum number of decrease boxes in a row
    maxNumDecreaseBox2 = 6
    maxNumDecreaseBox3 = 6

    minNumIncreaseCircle = 1    #The minimum number of increase circles in a row
    maxNumIncreaseCircle = 3    #The maximum number of increase circles in a row
    ySpeedGeneral = 4           #How fast the boxes/circles are coming down
    lives = 100                 #How many lives the player starts with

    #Destroy Buttons
    easyButton.destroy()
    mediumButton.destroy()
    hardButton.destroy()

    #Delete the introduction screen
    screen.delete(intro, introBorder)
    for i in range(320):
        screen.delete(introBoxes[i])

    runGame()   #Proceed to run the game


def mediumLevel():  #Set values for the medium level
    global maxNumDecreaseBox1, maxNumDecreaseBox2, maxNumDecreaseBox3, minNumDecreaseBox1, minNumDecreaseBox2, minNumDecreaseBox3
    global maxNumIncreaseCircle, minNumIncreaseCircle, ySpeedGeneral, lives
    global easyButton, mediumButton, hardButton, intro, introBoxes, introBorder

    minNumDecreaseBox1 = 4
    minNumDecreaseBox2 = 4
    minNumDecreaseBox3 = 4

    maxNumDecreaseBox1 = 7
    maxNumDecreaseBox2 = 7
    maxNumDecreaseBox3 = 7

    minNumIncreaseCircle = 1
    maxNumIncreaseCircle = 2
    ySpeedGeneral = 4
    lives = 75

    #Destroy Buttons
    easyButton.destroy()
    mediumButton.destroy()
    hardButton.destroy()

    #Delete the introduction screen
    screen.delete(intro, introBorder)
    for i in range(320):
        screen.delete(introBoxes[i])

    runGame()   #Proceed to run the game


def hardLevel():    #Sets values for the hard level
    global maxNumDecreaseBox1, maxNumDecreaseBox2, maxNumDecreaseBox3, minNumDecreaseBox1, minNumDecreaseBox2, minNumDecreaseBox3
    global maxNumIncreaseCircle, minNumIncreaseCircle, ySpeedGeneral, lives
    global easyButton, mediumButton, hardButton, intro, introBoxes, introBorder

    minNumDecreaseBox1 = 5
    minNumDecreaseBox2 = 5
    minNumDecreaseBox3 = 5

    maxNumDecreaseBox1 = 7
    maxNumDecreaseBox2 = 7
    maxNumDecreaseBox3 = 7

    minNumIncreaseCircle = 1
    maxNumIncreaseCircle = 1
    ySpeedGeneral = 5
    lives = 50

    #Destroy Buttons
    easyButton.destroy()
    mediumButton.destroy()
    hardButton.destroy()

    #Delete the introduction screen
    screen.delete(intro, introBorder)
    for i in range(320):
        screen.delete(introBoxes[i])
        
    runGame()   #Proceed to run the game


############################### INTRO SCREEN ###################################

def startScreen():  #The introduction screen
    global intro, introImage, playButton, instructionButton, introColours, introBoxes, introBorder, replayButton

    #Intro Image
    introColours = ["#0c10bb", "#1517cb", "#1f1edb", "#2825eb", "#322dfb"]
    introBoxes = []

    for i in range(int(800/50)):                #Draws the background blue boxes 
        for n in range(int(1000/50)):
            introBoxes.append(screen.create_rectangle(50*n, 50*i, 50 + 50*n, 50 + 50*i, fill = choice(introColours), outline = choice(introColours)))

    introBorder = screen.create_rectangle(70, 25, 930, 770, fill = "yellow", outline = "yellow")
    introImage = PhotoImage(file = "Intro.gif")
    intro = screen.create_image(500, 400, image = introImage, anchor = CENTER)      #Draws the main image

    #Play Button
    playButton = Button(root, text = "Play", bg = "white", fg = "black", font = "System 26 bold",
                        command = playButtonPressed,anchor = CENTER)
    playButton.pack()                                                   #Creates button
    playButton.place(x = 250, y = 550, width = 200, height = 100)       #Places button

    #Instruction Button
    instructionButton = Button(root, text = "Instructions", bg = "white", fg = "black",
                               font = "System 26 bold", command = instructionButtonPressed, anchor = CENTER)
    instructionButton.pack()
    instructionButton.place(x = 560, y = 550, width = 200, height = 100)


def instructionButtonPressed(): #The procedure that happens when the instruction button is pressed
    global playButton, instructionButton, returnButton, instructionImage, instruction, intro

    #Delete/destroy the intro screen/buttons
    screen.delete(intro)
    playButton.destroy()
    instructionButton.destroy()

    #Instruction Page
    instructionImage = PhotoImage(file = "Instruction.gif")
    instruction = screen.create_image(500, 400, image = instructionImage, anchor = CENTER)

    #Return to Intro Screen Button
    returnButton = Button(root, text = "Return", bg = "white", fg = "black", font = "System 26 bold",
                          command = returnButtonPressed, anchor = CENTER)
    returnButton.pack()
    returnButton.place(x = 400, y = 630, width = 200, height = 100)


def returnButtonPressed():  #The procedure that happens when the return button is pressed
    global returnButton, instruction, introBorder, introBoxes

    #Delete/destroy the instruction screen/buttons
    returnButton.destroy()
    screen.delete(instruction, introBorder)

    for i in range(320):
        screen.delete(introBoxes[i])

    startScreen()   #Run start screen again


def playButtonPressed():    #The procedure that happens when the play button is pressed
    global playButton, instructionButton, easyButton, mediumButton, hardButton

    #Destroy the buttons
    playButton.destroy()
    instructionButton.destroy()

    #Easy Button
    easyButton = Button(root, text = "EASY", bg = "white", fg = "black", font = "System 26 bold",
                        command = easyLevel, anchor = CENTER)   #Calls the easyLevel() procedure
    easyButton.pack()
    easyButton.place(x = 150, y = 550, width = 200, height = 100)

    #Medium Button
    mediumButton = Button(root, text = "MEDIUM", bg = "white", fg = "black", font = "System 26 bold",
                        command = mediumLevel, anchor = CENTER) #Calls the mediumLevel() procedure
    mediumButton.pack()
    mediumButton.place(x = 400, y = 550, width = 200, height = 100)

    #Hard Button
    hardButton = Button(root, text = "HARD", bg = "white", fg = "black", font = "System 26 bold",
                        command = hardLevel, anchor = CENTER)   #Calls the hardLevel() procedure
    hardButton.pack()
    hardButton.place(x = 650, y = 550, width = 200, height = 100)


##################$################# END GAME ####################################

def endGame():  #Gets called when game ends
    global gameOver, yourScore, replayButton

    #Draws game over and tells player their score
    gameOver = screen.create_text(450, 250, text = "GAME OVER", font = "System 58 bold", fill = "black")
    yourScore = screen.create_text(450, 350, text = "Your score is: " + str(score), font = "System 30 bold", fill = "black", anchor = CENTER)

    #Replay Button
    replayButton = Button(root, text = "Replay", bg = "white", fg = "black", font = "System 26 bold",
                        command = replayButtonPressed, anchor = CENTER)
    replayButton.pack()
    replayButton.place(x = 350, y = 450, width = 200, height = 100)

    screen.update()


def replayButtonPressed():
    global replayButton, gameOver, yourScore

    #Delete the background of the game screen/Destroy replayButton
    screen.delete(gameOver, yourScore, qText)
    for i in range(int(800/50)):
        screen.delete(leftBorder[i], rightBorder[i])
    for i in range(300):
        screen.delete(clouds[i])
    for i in range(int(800/50*2)):
        screen.delete(leftBar[i])
    for i in range(int(800/50*4)):
        screen.delete(rightBar[i])

    replayButton.destroy()

    startScreen()   #Goes back to the introduction screen


################################### GENERAL ######################################

def scoreBar(): #Tracks scores and draws it on screen
    global score, lives, bar

    if gameRun == True: #While the player still has lives, the score increases by 1 every time the screen updates
        score = score + 1

    bar = screen.create_text(925, 100, text = score, font = "System 36 bold", fill = "white")


def getDistance(x1, y1, x2, y2):    #Calculates distance
    distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance


def checkLives():   
    global gameRun, numIncreaseCircle

    if lives <= 0:      #If lives are smaller than or equal to 0, then gameRun would be false
        gameRun = False

    elif lives >= 200:  #If lives are bigger than or equal to 200
        for i in range(numIncreaseCircle):          
            screen.delete(increaseCircleDrawing[i])
        numIncreaseCircle = 0                       #Set the number of increase circles to 0 for the rest of the game


def deleteObjects():
    screen.delete(playerDrawing, playerLives, bar)

    for i in range(numDecreaseBox1):            #Delete all the boxes, circles, etc.
        screen.delete(decreaseBoxDrawing1[i])
        screen.delete(dNumDrawing1[i])

    for i in range(numDecreaseBox2):
        screen.delete(decreaseBoxDrawing2[i])
        screen.delete(dNumDrawing2[i])

    for i in range(numDecreaseBox3):
        screen.delete(decreaseBoxDrawing3[i])
        screen.delete(dNumDrawing3[i])

    for i in range(numIncreaseCircle):
        screen.delete(increaseCircleDrawing[i])


################################## KEY HANDLERS ################################

def keyDownHandler(event):
    global xSpeedPlayer, QPressed

    if event.keysym == "Left":
        xSpeedPlayer = -7

        for i in range(numDecreaseBox1):    #If the player's center point is in the decrease box
            if yDecreaseBox1[i] < yPlayer + 30 < yDecreaseBox1[i] + 100 and xDecreaseBox1[i] < xPlayer + 30 < xDecreaseBox1[i] + 100:
                xSpeedPlayer = 0            #Then the player's speed would be 0 even if they did press on an arrow key, meaning that they can't move while in the box

        for i in range(numDecreaseBox2):
            if yDecreaseBox2[i] < yPlayer + 30 < yDecreaseBox2[i] + 100 and xDecreaseBox2[i] < xPlayer + 30 < xDecreaseBox2[i] + 100:
                xSpeedPlayer = 0

        for i in range(numDecreaseBox3):
            if yDecreaseBox3[i] < yPlayer + 30 < yDecreaseBox3[i] + 100 and xDecreaseBox3[i] < xPlayer + 30 < xDecreaseBox3[i] + 100:
                xSpeedPlayer = 0

    elif event.keysym == "Right":
        xSpeedPlayer = 7

        for i in range(numDecreaseBox1):
            if yDecreaseBox1[i] < yPlayer + 30 < yDecreaseBox1[i] + 100 and xDecreaseBox1[i] < xPlayer + 30 < xDecreaseBox1[i] + 100:
                xSpeedPlayer = 0

        for i in range(numDecreaseBox2):
            if yDecreaseBox2[i] < yPlayer + 30 < yDecreaseBox2[i] + 100 and xDecreaseBox2[i] < xPlayer + 30 < xDecreaseBox2[i] + 100:
                xSpeedPlayer = 0

        for i in range(numDecreaseBox3):
            if yDecreaseBox3[i] < yPlayer + 30 < yDecreaseBox3[i] + 100 and xDecreaseBox3[i] < xPlayer + 30 < xDecreaseBox3[i] + 100:
                xSpeedPlayer = 0

    elif event.keysym == "q" or event.keysym == "Q":    #If the player pressed "q" or "Q"
        QPressed = True                                 #The game stops running
        

def keyUpHandler( event ):      #If the arrow keys are released
    global xSpeedPlayer

    xSpeedPlayer = 0            #The speed of the player is 0


###################################### RUN GAME ################################

def runGame():
    setInitialValues()
    createInitialObjects()
    drawBackground()

    while QPressed == False and gameRun == True:
        drawPlayer()
        drawDecreaseBox()
        drawIncreaseCircle()
        scoreBar()

        updatePlayer()
        updateDecreaseBox()
        updateIncreaseCircle()
        collisionUpdate()
        checkLives()
        
        screen.update()
        sleep(0.02)
        deleteObjects()

    endGame()


#STARTS THE GAME AFTER 0 SECS
root.after(0, startScreen)

#BINDINGS
screen.bind("<Key>", keyDownHandler)
screen.bind("<KeyRelease>", keyUpHandler)

screen.pack()
screen.focus_set()
root.mainloop()
