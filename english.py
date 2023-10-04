from time import *
from tkinter import *
import os


print("Hi there, my name is JARVIS. I'm the text based A.I. this software runs on")
print("")
print("How could i be of service?")

while True:
    if input() == "/list":
        print("/list")
        print("/opera")
        print("/discord")
        print("/time")
        print("/date")
        print("/program end")
        print("...")
        print("more to be added...")
        print("very well sir a list of commands is being opened for you")
        print("what can i do for you next?")

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

        print("very well sir time is being opened for you")
        print("what can i do for you next?")
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

        print("what can i do for you next?")

    elif input() == "/program end":
        exit()

    elif input() == "/open browser" or "/opera":
        os.startfile("C:/Users/evert/Desktop/Opera GX-browser.lnk")
        print("very well sir, your browser is being opened for you")
        print("what can i do for you next?")

    elif input() == "/open DC" or "/discord":
        os.startfile("C:/Users/evert/Desktop/Discord.lnk")
        print("very well sir discord is being opened for you")
        print("what can i do for you next?")

    else:
        print("I'm sorry but i dont know what that means.. Maybe try something else?")

        break
