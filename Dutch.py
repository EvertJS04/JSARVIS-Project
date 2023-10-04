from time import *
from tkinter import *
import os

print("Hey daar, ik ben JARVIS, dit systeem zijn virtuele A.I. assistent")
print("")
print("Hoe kan ik u noemen?")

username = input()

print("okay " + username + ". Wat kan ik voor u doen?")

while True:
    if input() == "/list":
        print("/list")
        print("/opera")
        print("/discord")
        print("/time")
        print("/date")
        print("/program end")
        print("...")
        print("binnenkort meer opties...")
        print("okay " + username + " een lijst met alle commandos wordt voor u geopent")
        print("wat kan ik nog meer voor u doen?")

    elif input() == "/time" or "/showtime":
        clockwndw = Tk()
        clockwndw.geometry("500x500")
        clockwndw.config(bg="black")


        def clock2():
            time_string = strftime("%H:%M:%S")
            time_label.config(text=time_string)

            clockwndw.after(10, clock2)


        time_label = Label(clockwndw, font=("OCR A Extended", 70), fg="white", bg="Blue")
        time_label.pack()

        clock2()

        print("kay " + username + " de tijd wordt voor u geopent")
        print("Wat kan ik nog meer voor u doen?")
        clockwndw.mainloop()

    elif input() == "/date" or "/showdate":
        datewndw = Tk()
        datewndw.geometry("500x500")
        datewndw.config(bg="black")

        def date():
            time_string2 = strftime("%d:%m:%y")
            time_label2.config(text=time_string2)

            datewndw.after(10, date)


        time_label2 = Label(datewndw, font=("OCR A Extended", 70), fg="white", bg="Blue")
        time_label2.place(y=830, x=1395)

        date()
        print("okay " + username + " de datum wordt voor u geopent")
        print("Wat kan ik nog meer voor udoen?")

    elif input() == "/program end":
        exit()

    elif input() == "/open browser" or "/opera":
        os.startfile("C:/Users/evert/Desktop/Opera GX-browser.lnk")
        print("Okay " + username + " Uw browser wordt voor u geopent")
        print("wat kan ik nog meer voor ik doen?")

    elif input() == "/open DC" or "/discord":
        os.startfile("C:/Users/evert/Desktop/Discord.lnk")
        print("Okay " + username + " Discord wordt voor u geopent")
        print("Wat kan ik nog meer voor u doen?")

    else:
        print("Sorry, maar ik weet niet wat dat betekend, kunt u het misschien nog een keer proberen?")
        break
