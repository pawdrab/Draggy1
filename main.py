import tkinter as tk
from tkinter import *
from time import *
import random
import matplotlib.pyplot as plt
#import pyrebase

root = tk.Tk()
displayWidth = root.winfo_screenwidth()
displayHeight = root.winfo_screenheight()
root.config(bg="#2D5D2D")
root.attributes("-fullscreen", True)
#root.overrideredirect(True)
root.geometry(str(displayWidth)+"x"+str(displayHeight)+"+0+0")
pixel = tk.PhotoImage(width=1, height=1)

amountOfButtons = 3
buttonWidth = int(2*displayWidth/7)
buttonHeight = int(2*displayHeight/7)
paddingx = int( (displayWidth-amountOfButtons*buttonWidth)/(amountOfButtons+1) )
paddingy = int( (displayHeight-amountOfButtons*buttonHeight)/(amountOfButtons+1) )

var = StringVar()
var.set("Zacznij pomiar")

startButtonString = StringVar()
startButtonString.set("Kliknij aby zaczac pomiar")

measurement_time = 0
speed = 100
speedTable = []
timeTable = []

def graph():
    plt.plot(timeTable, speedTable)
    plt.show()

def displayCurrentSpeed(speed):
    var.set("V = " + str(round(speed, 2)))
    root.update_idletasks()

def displayCurrendTime(currentTime):
    startButtonString.set(round(currentTime, 2) )
    root.update_idletasks()

def myButton2Clicked():
    graph()

def myButton3Clicked():
    root.destroy()

def myButton1Clicked():
    var.set("Pomiar trwa")
    root.update_idletasks()
    measurement_time = measure(speed)
    print(speedTable)
    print(timeTable)
    print("zarejestrowano " + str(len(speedTable)) + " próbek")
    print("Czas = " + str(measurement_time))
    #var.set(str(measurement_time))
    #root.update_idletasks()

def measure(speed):
    measurement_start = time()
    while(speed < 200):
        addedValue = random.randint(1, 100)/100
        sleep(1 / 18)
        speed = speed + addedValue
        speedTable.append(speed)
        timeTable.append(str(time() - measurement_start))
        displayCurrentSpeed(speed)
        displayCurrendTime((time() - measurement_start))
    measurement_stop = time()
    return (measurement_stop - measurement_start)

myButton3 = Button(root, text="Wyjście", bg="#888888", command = myButton3Clicked, image=pixel, height = buttonHeight/3, width = buttonWidth/3, compound="c")
myButton3.place(x=paddingx, y=paddingy)
myButton1 = Button(root, textvariable=str(startButtonString), bg="#888888", command = myButton1Clicked, image=pixel, height = buttonHeight, width = buttonWidth, compound="c")
myButton1.place(x=displayWidth-buttonWidth-paddingx, y=paddingy)
myButton2 = Button(root, text="Pokaż wykres", bg="#888888", command = myButton2Clicked, image=pixel, height = buttonHeight, width = buttonWidth, compound="c", )
myButton2.place(x=displayWidth-buttonWidth-paddingx, y=displayHeight-buttonHeight-paddingy)
myLabel1 = Label(root, textvariable=str(var), bg="#888888", image=pixel, height = buttonHeight, width = buttonWidth, compound="c")
myLabel1.place(x=displayWidth-buttonWidth-paddingx, y = (displayHeight-buttonHeight)/2)

root.mainloop()







