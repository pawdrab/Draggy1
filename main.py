import random
import tkinter as tk
from time import *
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt

root = tk.Tk()
displayWidth = root.winfo_screenwidth()
displayHeight = root.winfo_screenheight()
root.config(bg="#000000")
root.attributes("-fullscreen", True)
root.geometry(str(displayWidth)+"x"+str(displayHeight)+"+0+0")
pixel = tk.PhotoImage(width=1, height=1)

buttonWidth = int(displayWidth/3)
buttonHeight = int(displayHeight/4)
paddingx = int( displayWidth/20)
paddingy = int( displayHeight/20)

var = StringVar()
var.set("Zacznij pomiar")
startButtonString = StringVar()
startButtonString.set("Kliknij aby zaczac pomiar")

speed = 0
speedTable = []
timeTable = []

def graph():
    plt.plot(timeTable, speedTable)
    plt.grid(visible=True)
    plt.autoscale(enable=True, tight=True)
    plt.locator_params(axis="both", tight=True, nbins=10)
    plt.show()
    print(round(float(timeTable[-1]), 2 ))

def displayCurrentSpeed(speed):
    var.set("V = " + str(round(speed, 2)) + " km/h")

def displayCurrendTime(currentTime):
    startButtonString.set("T = " + str( round(currentTime, 2) ) + " s")
    root.update_idletasks()

def getStartSpeed():
    startSpeed = startMeasurementSlider.get()
    print("Start speed = " + str(startSpeed))
    return startSpeed

def getEndSpeed():
    endSpeed = endMeasurementSlider.get()
    print("End speed = " + str(endSpeed))
    return endSpeed

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

def measure(speed):
    startSpeed = getStartSpeed()
    endSpeed = getEndSpeed()
    speedTable.clear()
    timeTable.clear()
    measurement_start = round(time(),3)
    while(speed < endSpeed):
        addedValue = random.randint(1, 100)/100
        sleep(1 / 18)
        speed = speed + addedValue
        speedTable.append(round(speed, 3))
        timeTable.append((round( (time() - measurement_start) , 3)))
        x = ((speed - startSpeed) / (endSpeed - startSpeed)) * 100
        displayCurrentSpeed(speed)
        displayCurrendTime((time() - measurement_start))
        speedProgressBar['value'] = x
    measurement_stop = round(time(),3)
    startButtonString.set("Czas pomiaru : " + str(round((measurement_stop - measurement_start), 3 )) + " s")
    root.update_idletasks()
    return (round((measurement_stop - measurement_start),3))

myButton3 = Button(root, text="Wyjście", bg="#888888", command = myButton3Clicked, image=pixel, height = buttonHeight/3, width = buttonWidth/3, compound="c", font=("Arial", 25))
myButton3.place(x=paddingx, y=paddingy)
myButton1 = Button(root, textvariable=str(startButtonString), bg="#888888", command = myButton1Clicked, image=pixel, height = buttonHeight, width = buttonWidth, compound="c", font=("Arial", 25))
myButton1.place(x=displayWidth-buttonWidth-paddingx, y=paddingy)
myButton2 = Button(root, text="Pokaż wykres", bg="#888888", command = myButton2Clicked, image=pixel, height = buttonHeight, width = buttonWidth, compound="c", font=("Arial", 25))
myButton2.place(x=displayWidth-buttonWidth-paddingx, y=displayHeight-buttonHeight-paddingy)
myLabel1 = Label(root, textvariable=str(var), bg="#888888", image=pixel, height = buttonHeight, width = buttonWidth, compound="c", font=("Arial", 25))
myLabel1.place(x=displayWidth-buttonWidth-paddingx, y = (displayHeight-buttonHeight)/2)
startMeasurementSlider = Scale(root, from_=0, label="V start", to=250, orient=HORIZONTAL, length = buttonWidth, width=buttonWidth/5, sliderlength=buttonWidth/5, font=("Arial", 50))
startMeasurementSlider.place(x=paddingx, y=(displayHeight-buttonHeight)/2)
endMeasurementSlider = Scale(root, from_=0, label="V end", to=250, orient=HORIZONTAL, length = buttonWidth, width=buttonWidth/5, sliderlength=buttonWidth/5, font=("Arial", 50))
endMeasurementSlider.place(x=paddingx, y=(displayHeight-buttonHeight))
speedProgressBar = ttk.Progressbar(root, orient=HORIZONTAL, length=buttonWidth, mode = 'determinate')
speedProgressBar.place(x=paddingx, y=( (displayHeight-buttonHeight) -  ((displayHeight-buttonHeight)/8)  ) )

root.mainloop()
