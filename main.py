from tkinter import *
from time import strftime
from PIL import ImageTk, Image, Image as PILImage
import webbrowser
from tkinter import ttk
import tkinter as tk
import time
import os
import pyttsx3
import random

#  QOL Statements
black = "black"
Black = "Black"
dark_blue = "#000020"
blue = "blue"
clock = "%H:%M:%S"
ocr = "OCR A Extended"

#   ----INTRODUCTION AND EXPLANATION COMMENT----
#   Every command define unit [def {....}():] is a part of V.mess and the JS[--] Units
#   Every D.D.S.A. Databank is marked with a comment for ease of adding more
#   Every import statement is a part of JS.P.U. and JS.PR.U.
#   Every .Tk() unit is handled by V.W.S.OS.
#   S.S.EVE is not a unit but the name of the main software that this is all based on
#   The entire project is S.S.EVE
#   JARVIS AI is not a part of this project
#   But a part of the Text Based Structural Interface Track or TB.S.I.T. for short
#   ----END OF INTRODUCTION AND EXPLANATION COMMENT----

# the startup sequence of the entire program


def startup():
    sseve_startup = Tk()
    sseve_startup.geometry("300x300+500+200")
    sseve_startup.config(bg="Black")
    sseve_startup.overrideredirect(True)

    main_text = Label(sseve_startup, text="Loading J.[S].A.R.V.I.S.", fg="dark blue", bg="black",
                      font=("ORC A Extended", 15))

    password = Entry(sseve_startup, width=20, font=20)
    password.place(x=0, y=280)

    password_list = ("jarvis" + " admin " + "char")

    def char_color_error_message():
        char_error_window = Toplevel()
        char_error_window.geometry("400x500")
        char_error_window.config(bg=black)
        char_error_window.overrideredirect(True)

        def update_rotation(image_label, angle_var, rotation_speed=5):
            angle_var[0] += rotation_speed
            rotated_image = error_char_bf.rotate(angle_var[0])
            rotated_image_tk = ImageTk.PhotoImage(rotated_image)
            image_label.configure(image=rotated_image_tk)
            image_label.image = rotated_image_tk  # Keep a reference to prevent garbage collection
            char_error_window.after(50, update_rotation, image_label, angle_var, rotation_speed)

        error_char_bf = PILImage.open("C:/Users/evert/Documents/J.[S].A.R.V.I.S. Project files/"
                                      "Data/16589-200 - kopie.png")

        error_char = ImageTk.PhotoImage(error_char_bf)

        # Create a label to display the image
        image_label = Label(char_error_window, image=error_char, bg='black')
        image_label.pack()

        # Set up rotation variables
        angle_var = [0]  # Using a list to make it mutable

        # Start the rotation update loop
        char_error_window.after(0, update_rotation, image_label, angle_var)

        Label(char_error_window, text="That color is already in use!", bg=black, fg=blue,).pack()

        char_error_window.after(3000, char_error_window.destroy)

        char_error_window.mainloop()

    # working passwords are: jarvis, admin, help, and play

    #   login safety sequence
    def login_check():
        login = password.get()
        if login == "jarvis":
            english = Button(sseve_startup, text="English", bg="black", fg="dark blue", command=english_setup,
                             font=("OCR A Extended", 20))
            english.place(x=0, y=250)
            dutch = Button(sseve_startup, text="Netherlands", bg="black", fg="dark blue", command=dutchsetup,
                           font=("OCR A Extended", 18))
            dutch.place(x=140, y=250)
            password.destroy()
            login_button.destroy()

        elif login == "char":
            sseve_startup.destroy()
            os.startfile("C:/Users/evert/Documents/J.[S].A.R.V.I.S. Project files/JSA - JSC Files/"
                         "AIChat/CharlotteAI.py")

        elif login == "exit":
            exit()

        elif login == "quit":
            exit()


        # DEBUG Mode
        elif login == "admin":
            sseve_startup.destroy()
            # Create the Tkinter window
            debug_mode = Tk()
            debug_mode.attributes("-fullscreen", True)
            debug_mode.config(bg="black")

            filepath = "C:/Users/evert/Documents/J.[S].A.R.V.I.S. Project files/Data/Jz6bAs.gif"
            frames = []  # Make frames a global variable

            def load_gif_frames(file_path):
                gif = Image.open(file_path)

                try:
                    while True:
                        frame = gif.convert("RGBA")
                        frames.append(ImageTk.PhotoImage(frame))
                        gif.seek(gif.tell() + 1)  # Move to the next frame
                except EOFError:
                    pass  # End of frames

            load_gif_frames(filepath)

            def update(ind):
                frame = frames[ind]
                ind = (ind + 1) % len(frames)
                label.configure(image=frame)
                debug_mode.after(10, update, ind)  # Adjust the delay as needed

            label = Label(debug_mode)
            label.pack()
            debug_mode.after(0, update, 0)

            def shutdown():
                debug_mode.destroy()

            def move_button(step):
                x, y = -abs(150) + step, 0  # Coordinates to move the button
                sdbutton.place(x=x, y=y)

                if x < 0:  # If the button hasn't reached its final position
                    debug_mode.after(1, move_button, step + 5)  # Increase step to move the button

            sdbutton = Button(debug_mode, text="Shutdown", command=shutdown, height=2, width=10, bg="black",
                              fg="green", font=("OCR A Extended", 20))
            sdbutton.place(x=10, y=10)  # Set initial off-screen position

            # Start the animation
            move_button(0)

            def move_button1(step):
                x, y = -abs(200) + step, 100  # Coordinates to move the button
                func0.place(x=x, y=y)

                if x < 0:  # If the button hasn't reached its final position
                    debug_mode.after(1, move_button1, step + 5)  # Increase step to move the button

            func0 = Button(debug_mode, text="ABI Mode", command=shutdown, height=2, width=10, bg="black",
                           fg="green", font=("OCR A Extended", 20))  # ABI is Audio Based Interaction
            func0.place(x=10, y=10)  # Set initial off-screen position

            # Start the animation
            move_button1(0)

            def move_button2(step):
                x, y = -abs(250) + step, 200  # Coordinates to move the button
                function_button.place(x=x, y=y)

                if x < 0:  # If the button hasn't reached its final position
                    debug_mode.after(1, move_button2, step + 5)  # Increase step to move the button

            function_button = Button(debug_mode, text="Holographic Mode", command=shutdown, height=2, width=15,
                                     bg="black", fg="green", font=("OCR A Extended", 15))
            function_button.place(x=10, y=10)  # Set initial off-screen position

            # Start the animation
            move_button2(0)

            def move_button3(step):
                x, y = -abs(300) + step, 300  # Coordinates to move the button
                func01.place(x=x, y=y)

                if x < 0:  # If the button hasn't reached its final position
                    debug_mode.after(1, move_button3, step + 5)  # Increase step to move the button

            func01 = Button(debug_mode, text="Crash Tester", command=shutdown, height=2, width=10, bg="black",
                            fg="green", font=("OCR A Extended", 15))
            func01.place(x=10, y=10)  # Set initial off-screen position

            # Start the animation
            move_button3(0)

            def move_button4(step):
                x, y = -abs(350) + step, 400  # Coordinates to move the button
                sd1button.place(x=x, y=y)

                if x < 0:  # If the button hasn't reached its final position
                    debug_mode.after(1, move_button4, step + 5)  # Increase step to move the button

            sd1button = Button(debug_mode, text="Users", command=shutdown, height=2, width=10, bg="black",
                               fg="green", font=("OCR A Extended", 20))
            sd1button.place(x=10, y=10)  # Set initial off-screen position

            # Start the animation
            move_button4(0)

            def move_button5(step):
                x, y = -abs(400) + step, 500  # Coordinates to move the button
                func2.place(x=x, y=y)

                if x < 0:  # If the button hasn't reached its final position
                    debug_mode.after(1, move_button5, step + 5)  # Increase step to move the button

            func2 = Button(debug_mode, text="edit colors", command=shutdown, height=2, width=11, bg="black",
                           fg="green", font=("OCR A Extended", 19))
            func2.place(x=10, y=10)  # Set initial off-screen position

            # Start the animation
            move_button5(0)

            def move_button6(step):
                x, y = -abs(450) + step, 600  # Coordinates to move the button
                func1button.place(x=x, y=y)

                if x < 0:  # If the button hasn't reached its final position
                    debug_mode.after(1, move_button6, step + 5)  # Increase step to move the button

            func1button = Button(debug_mode, text="Login User", command=startup, height=2,
                                 width=11, bg="black", fg="green", font=("OCR A Extended", 19))
            func1button.place(x=10, y=10)  # Set initial off-screen position

            # Start the animation
            move_button6(0)

            def move_button7(step):
                x, y = -abs(500) + step, 700  # Coordinates to move the button
                func3.place(x=x, y=y)

                if x < 0:  # If the button hasn't reached its final position
                    debug_mode.after(1, move_button7, step + 5)  # Increase step to move the button

            func3 = Button(debug_mode, text="no idea yet", command=shutdown, height=2, width=10, bg="black",
                           fg="green", font=("OCR A Extended", 20))
            func3.place(x=10, y=10)  # Set initial off-screen position

            # Start the animation
            move_button7(0)

            os.startfile("C:/Users/evert/PycharmProjects/test/main.pyw")
            debug_mode.mainloop()

        elif login == "help":
            password_help = Label(sseve_startup, text=password_list, bg='black', fg='blue',
                                  font=("OCR A Extended", 11))
            password_help.pack(side=TOP)

        else:
            login_error()

    login_button = Button(sseve_startup, text="login", command=login_check)
    login_button.place(x=250, y=280)

    login_button.bind("<Return>", login_check)

    #   JS Signature:

    signature0 = (Label(sseve_startup, text=("File==S.S.EVE; STATE==Complete;"
                        "Sequence Code==:""103AFF540!!VMESS-S.S.EVE""01125812240-VW.S.O.S.-C0150--!"),
                        fg="black", bg="Black"))
    signature0.pack(side=TOP)

    def english_setup():
        sseve_startup.destroy()
        main_screen = Toplevel()
        main_screen.attributes("-fullscreen", True)
        main_screen.config(bg="black")

        #   JS Signature:

        signature1 = (Label(main_screen, text=("File==S.S.EVE; STATE==Complete;"
                            "Sequence Code==:""5837FF540!!S.S.EVE""50725203240-VW.S.O.S.-C0450--!"),
                            fg="black", bg="Black"))
        signature1.pack(side=TOP)

        # D.D.S.A. Storage Unit

        wpr1 = ImageTk.PhotoImage(file="C:/Users/evert/Documents/J.[S].A.R.V.I.S. Project files/Data/1876553.gif")
        browser_logo = ImageTk.PhotoImage(
            file="C:/Users/evert/Documents/J.[S].A.R.V.I.S. Project files/Data/70x70Logo.scale-100.png")
        vscimage = ImageTk.PhotoImage(
            file="C:/Users/evert/AppData/Local/Programs/Microsoft VS Code/resources/app/resources/win32/code_70x70.png"
        )
        shutdown_logo = ImageTk.PhotoImage(
            file="C:/Users/evert/Documents/J.[S].A.R.V.I.S. Project files/Data/jarvis logo shutdown small.png")
        wpr2 = ImageTk.PhotoImage(
            file="c:/Users/evert/Documents/J.[S].A.R.V.I.S. Project files/Data/80fc6a6c4325b3eba2e0f2ba7cee2a13.jpg")
        wpr3 = ImageTk.PhotoImage(file="C:/Users/evert/Documents/J.[S].A.R.V.I.S. Project files/Data/1135480.jpg")

        holo_wpr = ImageTk.PhotoImage(file="C:/Users/evert/Documents/J.[S].A.R.V.I.S. Project files/Data/brudah.jpg")

        #   (pause line to differentiate between the normal code and the D.D.S.A. storage unit)

        wp = Label(main_screen, image=wpr1)
        wp.pack(pady=60)

        def open_vsc():
            import os
            os.startfile("C:/Users/evert/AppData/Local/Programs/Microsoft VS Code/Code.exe")

        def open_browser():
            import os
            os.startfile("C:/Users/evert/AppData/Local/Programs/Opera GX/opera.exe")

        # V.mess Execution Series

        def open_start_screen():
            starts = Tk()
            starts.geometry("1200x900")
            starts.config(bg="black")
            starts.overrideredirect(True)

            #   JS Signature:

            signature2 = (Label(starts, text=("File==S.S.EVE; STATE==Complete;"
                                "Sequence Code==:""103GDQ540!!V.MESS""01586712240-VW.S.O.S.-C9990--!"),
                                fg="black", bg="Black"))
            signature2.pack(side=TOP)

            def clock2():
                time_string2 = strftime("%H:%M:%S")
                clock2lbl.config(text=time_string2)

                (sseve_startup.after(10, clock2))

            def shutdown():
                starts.destroy()
                main_screen.destroy()
                exit()

            def close():
                starts.destroy()

            def text_mode():
                language_selector = Tk()
                language_selector.config(bg="black")
                language_selector.geometry("200x200+500+600")
                language_selector.overrideredirect(True)

                def english_version():
                    language_selector.destroy()
                    import os
                    os.startfile("C:/Users/evert/Documents/J.[S].A.R.V.I.S. Project files/"
                                 "Main Files/Text Based/JARVIS English Version/main.py")

                def dutch_version():
                    language_selector.destroy()
                    import os
                    os.startfile("C:/Users/evert/Documents/J.[S].A.R.V.I.S. Project files/"
                                 "Main Files/Text Based/JARVIS Dutch Version/main.py")

                dutch_version = Button(language_selector, command=dutch_version, bg="black", fg="dark blue",
                                       text="Nederland", font=("OCR A Extended", 20))
                dutch_version.pack(side=TOP)

                english_version = Button(language_selector, command=english_version, bg="black", fg="dark blue",
                                         text="Engels", font=("OCR A Extended", 20))
                english_version.pack(side=TOP)

            def settings():
                settingswindow = Tk()
                settingswindow.attributes("-fullscreen", True)
                settingswindow.config(bg="black")

                #   JS Signature:

                signature3 = (Label(sseve_startup, text=("File==settings; STATE==Complete;"
                                    "Sequence Code==:""103UPF540!!SSEVE""09925812240-VWSOS-C0890--!"),
                                    fg="black", bg="Black"))
                signature3.pack(side=TOP)

                def holomode():
                    settingswindow.destroy()
                    wp.config(image=holo_wpr)
                    startscr()
                    time_label.destroy()
                    starts.geometry("1920x1080")

                def wpselect():
                    settingswindow.destroy()
                    wps = Tk()
                    wps.geometry("250x250+640+270")
                    wps.config(bg="black")
                    wps.overrideredirect(True)

                    def wp1():
                        wp.config(image=wpr1)

                    def wp2():
                        wp.config(image=wpr2)

                    def wp3():
                        wp.config(image=wpr3)

                    def closewps():
                        wps.destroy()

                    wpsc = Button(wps, text="Sluit", command=closewps, bg="black", fg="white")
                    wpsc.pack(side=BOTTOM)

                    wp1btn = (Button
                              (wps, text=1, font=("OCR A Extended", 20),
                               bg="black", fg="white", command=wp1, height=1, width=5))
                    wp2btn = (Button
                              (wps, text=2, font=("OCR A Extended", 20),
                               bg="black", fg="white", command=wp2, height=1, width=5))
                    wp3btn = (Button
                              (wps, text=3, font=("OCR A Extended", 20),
                               bg="black", fg="white", command=wp3, height=1, width=5))
                    wp1btn.pack()
                    wp2btn.pack()
                    wp3btn.pack()

                def startmen():
                    starts.destroy()
                    startmenu.config(command=opensm)

                def startscr():
                    start.destroy()
                    startmenu.config(command=open_start_screen)

                def clockswitch_off():
                    if clock2lbl.config(fg="blue"):
                        clock2lbl.config(fg="black")

                    elif clock2lbl.config(fg="black"):
                        char_color_error_message()

                def clockswitch_on():
                    if clock2lbl.config(fg="black"):
                        clock2lbl.config(fg="blue")

                    elif clock2lbl.config(fg="blue"):
                        char_color_error_message()

                def closewndw():
                    settingswindow.destroy()

                holomodebtn = Button(settingswindow, command=holomode, text="hologhraphic interface mode", bg="black",
                                     width=20, height=2, fg="blue", font=("OCR A Extended", 20))
                holomodebtn.place(y=500, x=0)

                closebtn2 = Button(settingswindow, command=closewndw, text="X", font=("ARIAL", 20), bg="red", width=4,
                                   height=1)
                closebtn2.place(y=0, x=1450)

                clockbtnon = Button(settingswindow, command=clockswitch_on, text="Clock Off", bg='Black', fg="blue",
                                    width=10, height=2)
                clockbtnon.place(x=0, y=0)

                clockbtnoff = Button(settingswindow, command=clockswitch_off, text="Clock On", bg='black', fg='Blue',
                                     width=10, height=2)
                clockbtnoff.place(x=0, y=50)

                wallpapersel = Button(settingswindow, text="Wallpapers", command=wpselect, bg='black', fg='blue',
                                      width=10, height=2)
                wallpapersel.place(x=0, y=100)

                startmenbtn = Button(settingswindow, command=startmen, text="Start menu", bg="black", fg="blue",
                                     width=10, height=2)
                startmenbtn.place(x=0, y=150)

                startscrbtn = Button(settingswindow, command=startscr, text="Start screen", bg="black", fg="blue",
                                     width=10, height=2)
                startscrbtn.place(x=0, y=200)

                settingswindow.mainloop()

            starts.after(30000, close)

            bgname = Label(starts, text="J.[S].A.R.V.I.S.", font=("Engravers MT", 100), bg="black", fg="dark blue")
            bgname.place(x=0, y=350)

            closebtn = Button(starts, command=shutdown, text="shutdown", bg="dark blue", fg="black",
                              width=15, height=5, font=("OCR A Extended", 20))
            closebtn.place(y=700, x=0)

            funcbtn1 = Button(starts, command=close, text="Close", bg="black", fg="White", width=10, height=5,
                              font=("OCR A Extended", 20))
            funcbtn1.place(y=700, x=250)

            funcbtn2 = Button(starts, command=settings, text="Settings", bg="#200040", fg="white",
                              width=10, height=4, font=("OCR A Extended", 20))
            funcbtn2.place(y=680, x=1000)

            tbmode = Button(starts, command=text_mode,
                            text="Text Based Version", bg="black", fg="white", width=150, height=2)
            tbmode.place(y=0, x=0)

            vnamej = Label(starts, text="J.||P", bg="Black", fg="Blue", font=("OCR A Extended", 50))
            vnamej.place(x=980, y=100)

            vnames = Label(starts, text="S.||R", bg="Black", fg="Blue", font=("OCR A Extended", 50))
            vnames.place(x=980, y=180)

            vnamea = Label(starts, text="A.||O", bg="Black", fg="Blue", font=("OCR A Extended", 50))
            vnamea.place(x=980, y=260)

            vnamer = Label(starts, text="R.||J", bg="Black", fg="Blue", font=("OCR A Extended", 50))
            vnamer.place(x=980, y=340)

            vnamev = Label(starts, text="V.||E", bg="Black", fg="Blue", font=("OCR A Extended", 50))
            vnamev.place(x=980, y=420)

            vnamei = Label(starts, text="I.||C", bg="Black", fg="Blue", font=("OCR A Extended", 50))
            vnamei.place(x=980, y=500)

            vnames = Label(starts, text="S.||T", bg="Black", fg="Blue", font=("OCR A Extended", 50))
            vnames.place(x=980, y=580)

            search = Entry(starts, width=20, font=20)
            search.place(y=550, x=0)

            def opensource():
                string = search.get()
                webbrowser.open("Https://www." + string)

            Button(starts, text="Go", command=opensource, width=10, bg="black", fg="white").place(y=600, x=0)

            clock2lbl = Label(starts, font=("OCR A Extended", 25), fg="blue", bg="black")
            clock2lbl.place(y=830, x=1000)

            clock2()

        def opensm():
            start = Tk()
            start.geometry("250x400+0+463")
            start.config(bg="black")
            start.overrideredirect(True)

            def clock2():
                time_string2 = strftime("%H:%M:%S")
                clock2lbl.config(text=time_string2)

                (sseve_startup.after(10, clock2))

            def shutdown():
                start.destroy()
                main_screen.destroy()
                exit()

            def close():
                start.destroy()

            def textmode():

                languageselector = Tk()
                languageselector.config(bg="black")
                languageselector.geometry("200x200+500+600")
                languageselector.overrideredirect(True)

                def englishver():
                    languageselector.destroy()
                    import os
                    os.startfile(
                        "C:/Users/evert/Documents/J.[S].A.R.V.I.S. Project files/"
                        "Main Files/Text Based/JARVIS English Version/main.py")

                def dutchver():
                    languageselector.destroy()
                    import os
                    os.startfile(
                        "C:/Users/evert/Documents/J.[S].A.R.V.I.S. Project files/"
                        "Main Files/Text Based/JARVIS Dutch Version/main.py")

                dutchversion = Button(languageselector, command=dutchver, bg="black", fg="dark blue", text="Dutch",
                                      font=("OCR A Extended", 20))
                dutchversion.pack(side=TOP)

                englishversion = Button(languageselector, command=englishver, bg="black", fg="dark blue", 
                                        text="English", font=("OCR A Extended", 20))
                englishversion.pack(side=TOP)

            def settings():
                settingswindow = Tk()
                settingswindow.attributes("-fullscreen", True)
                settingswindow.config(bg="black")

                def holomode():
                    settingswindow.destroy()
                    start.destroy()
                    wp.config(image=holo_w.p.r)
                    startscr1()
                    time_label.destroy()
                    starts.geometry("1920x1080")

                def startmen1():
                    starts.destroy()
                    startmenu.config(command=opensm)

                def startscr1():
                    start.destroy()
                    startmenu.config(command=open_start_screen)

                def wpselect():
                    settingswindow.destroy()
                    wps = Tk()
                    wps.geometry("250x250+640+270")
                    wps.config(bg="black")
                    wps.overrideredirect(True)

                    def wp1():
                        wp.config(image=wpr1)

                    def wp2():
                        wp.config(image=wpr2)

                    def wp3():
                        wp.config(image=wpr3)

                    def closewps():
                        wps.destroy()

                    wpsc = Button(wps, text="Close", command=closewps, bg="black", fg="white")
                    wpsc.pack(side=BOTTOM)

                    wp1btn = (Button
                              (wps, text=1, font=("OCR A Extended", 20),
                               bg="black", fg="white", command=wp1, height=1, width=5))
                    wp2btn = (Button
                              (wps, text=2, font=("OCR A Extended", 20),
                               bg="black", fg="white", command=wp2, height=1, width=5))
                    wp3btn = (Button
                              (wps, text=3, font=("OCR A Extended", 20),
                               bg="black", fg="white", command=wp3, height=1, width=5))
                    wp1btn.pack()
                    wp2btn.pack()
                    wp3btn.pack()

                def clockswitch_off():
                    if clock2lbl.config(fg="blue"):
                        clock2lbl.config(fg="black")
                    if clock2lbl.config(fg="black"):
                        char_color_error_message()

                def clockswitch_on():
                    if clock2lbl.config(fg="black"):
                        clock2lbl.config(fg="blue")

                    if clock2lbl.config(fg="blue"):
                        char_color_error_message()

                def closewndw():
                    settingswindow.destroy()

                holomodebtn = Button(settingswindow, command=holomode, text="hologhraphic interface mode", bg="black",
                                     width=20, height=2, fg="blue", font=("OCR A Extended", 20))
                holomodebtn.place(y=500, x=0)

                closebtn2 = Button(settingswindow, command=closewndw, text="X", font=("ARIAL", 20), bg="red", width=4,
                                   height=1)
                closebtn2.place(y=0, x=1450)

                clockbtnon = Button(settingswindow, command=clockswitch_off, text="clock off", bg='Black', fg="blue",
                                    width=10, height=2)
                clockbtnon.place(x=0, y=0)

                clockbtnoff = Button(settingswindow, command=clockswitch_on, text="clock on", bg='black', fg='Blue',
                                     width=10, height=2)
                clockbtnoff.place(x=0, y=50)

                wallpapersel = Button(settingswindow, text="wallpapers", command=wpselect, bg='black', fg='blue',
                                      width=10, height=2)
                wallpapersel.place(x=0, y=100)

                startmenbtn1 = Button(settingswindow, command=startmen1, text="Start menu", bg="black", fg="blue",
                                      width=10, height=2)
                startmenbtn1.place(x=0, y=150)

                startscrbtn1 = Button(settingswindow, command=startscr1, text="Start screen", bg="black", fg="blue",
                                      width=10, height=2)
                startscrbtn1.place(x=0, y=200)

                settingswindow.mainloop()

            start.after(30000, close)

            closebtn = Button(start, command=shutdown, text="shutdown", bg="black", fg="white", width=30, height=2)
            closebtn.place(y=350, x=0)

            funcbtn1 = Button(start, command=close, text="close", bg="black", fg="white", width=30, height=2)
            funcbtn1.place(y=300, x=0)

            funcbtn2 = Button(start, command=settings, text="settings", bg="black", fg="white", width=30, height=2)
            funcbtn2.place(y=250, x=0)

            tbmode = Button(start, command=textmode, text="Text Based Version", bg="black", fg="white",
                            width=30, height=2)
            tbmode.place(y=200, x=0)

            name = Label(start, text="J.[S].A.R.V.I.S.", bg="Black", fg="Blue", font=("OCR A Extended", 20))
            name.pack(side=TOP)

            name2 = Label(start, text="Project", bg="Black", fg="Blue", font=("OCR A Extended", 20))
            name2.pack(side=TOP)

            clock2lbl = Label(start, font=("OCR A Extended", 25), fg="blue", bg="black")
            clock2lbl.pack(side=TOP)

            clock2()

        def fulltime():
            timew = Tk()
            timew.geometry("250x200+1290+670")
            timew.overrideredirect(True)
            timew.config(bg="#000030")

            def closetime():
                timew.destroy()

            closetimebtn = Button(timew, command=closetime, bg="red", fg="black", text="X", width=100)
            closetimebtn.pack(side=TOP)

            def detailtime():
                detailtimestring = strftime("%H:%M:%S")
                detailtimelabel.config(text=detailtimestring)

                timew.after(10, detailtime)

            detailtimelabel = Label(timew, font=("OCR A Extended", 20), fg="blue", bg="#000030")
            detailtimelabel.pack(side=TOP)

            detailtime()

            def date():
                datestring = strftime("%d/%m/%Y")
                datelabel.config(text=datestring)

                timew.after(10, date)

            datelabel = Label(timew, font=("OCR A Extended", 20), fg="blue", bg="#000030")
            datelabel.pack(side=TOP)

            date()

            def detaildate():
                detaildatestring = strftime("%A/%B/%Y")
                detaildatelabel.config(text=detaildatestring)

                timew.after(10, detaildate)

            detaildatelabel = Label(timew, font=("OCR A Extended", 15), fg="blue", bg="#000030")
            detaildatelabel.pack(side=TOP)

            detaildate()

            timew.mainloop()

        def clockd():
            time_string = strftime("%A/%H:%M")
            time_label.config(text=time_string, padx=620)

            main_screen.after(10, clockd)

        time_label = Button(main_screen, font=("OCR A Extended", 20), fg="blue", bg="#000030",
                            width=100, command=fulltime, border=0)
        time_label.place(y=830, x=0)

        clockd()

        startmenu = Button(main_screen, bg="Black", image=shutdown_logo, command=opensm, width=50, text="Start")
        startmenu.place(y="835", x="0")

        browser = Button(main_screen, image=browser_logo, border=0, command=open_browser, bg="black")
        browser.place(x=1400, y=0)

        vscode = Button(main_screen, bg="black", image=vscimage, border=0, command=open_vsc)
        vscode.place(x=1330, y=0)

        main_screen.mainloop()

    def dutchsetup():
        sseve_startup.destroy()
        mainscreend = Toplevel()
        mainscreend.attributes("-fullscreen", True)
        mainscreend.config(bg="black")

        # D.D.S.A. Storage Unit

        wpr1 = ImageTk.PhotoImage(file="C:/Users/evert/Documents/J.[S].A.R.V.I.S. Project files/Data/1876553.gif")
        browserlogo = ImageTk.PhotoImage(
            file="C:/Users/evert/Documents/J.[S].A.R.V.I.S. Project files/Data/70x70Logo.scale-100.png")
        vscimage = ImageTk.PhotoImage(
            file="C:/Users/evert/AppData/Local/Programs/Microsoft VS Code/resources/app/resources/win32/code_70x70.png"
        )
        shutdown_logo = ImageTk.PhotoImage(
            file="C:/Users/evert/Documents/J.[S].A.R.V.I.S. Project files/Data/jarvis logo shutdown small.png")
        wpr2 = ImageTk.PhotoImage(
            file="c:/Users/evert/Documents/J.[S].A.R.V.I.S. Project files/Data/80fc6a6c4325b3eba2e0f2ba7cee2a13.jpg")
        wpr3 = ImageTk.PhotoImage(file="C:/Users/evert/Documents/J.[S].A.R.V.I.S. Project files/Data/1135480.jpg")

        #   (pause line to differentiate between the normal code and the D.D.S.A. storage unit)

        wp = Label(mainscreend, image=wpr1)
        wp.pack(pady=60)

        def open_vsc():
            import os
            os.startfile("C:/Users/evert/AppData/Local/Programs/Microsoft VS Code/Code.exe")

        def open_browser():
            import os
            os.startfile("C:/Users/evert/AppData/Local/Programs/Opera GX/opera.exe")

        # V.mess Execution Series

        def openstartscreen():
            starts = Tk()
            starts.geometry("1200x900")
            starts.config(bg="black")
            starts.overrideredirect(True)

            def clock2():
                time_string2 = strftime("%H:%M:%S")
                clock2lbl.config(text=time_string2)

                (sseve_startup.after(10, clock2))

            def shutdown():
                starts.destroy()
                mainscreend.destroy()
                exit()

            def close():
                starts.destroy()

            def textmode():

                languageselector = Tk()
                languageselector.config(bg="black")
                languageselector.geometry("200x200+500+600")
                languageselector.overrideredirect(True)

                def englishver():
                    languageselector.destroy()
                    import os
                    os.startfile("C:/Users/evert/Documents/J.[S].A.R.V.I.S. Project files/"
                                 "Main Files/Text Based/JARVIS English Version/main.py")

                def dutchver():
                    languageselector.destroy()
                    import os
                    os.startfile("C:/Users/evert/Documents/J.[S].A.R.V.I.S. Project files/"
                                 "Main Files/Text Based/JARVIS Dutch Version/main.py")

                dutchversion = Button(languageselector, command=dutchver, bg="black", fg="dark blue", text="Nederlands",
                                      font=("OCR A Extended", 20))
                dutchversion.pack(side=TOP)

                englishversion = Button(languageselector, command=englishver, bg="black", fg="dark blue", text="Engels",
                                        font=("OCR A Extended", 20))
                englishversion.pack(side=TOP)

            def settings():
                settingswindow = Tk()
                settingswindow.attributes("-fullscreen", True)
                settingswindow.config(bg="black")

                def wpselect():
                    settingswindow.destroy()
                    wps = Tk()
                    wps.geometry("250x250+640+270")
                    wps.config(bg="black")
                    wps.overrideredirect(True)

                    def wp1():
                        wp.config(image=wpr1)

                    def wp2():
                        wp.config(image=wpr2)

                    def wp3():
                        wp.config(image=wpr3)

                    def closewps():
                        wps.destroy()

                    wpsc = Button(wps, text="Sluit", command=closewps, bg="black", fg="white")
                    wpsc.pack(side=BOTTOM)

                    wp1btn = (Button
                              (wps, text=1, font=("OCR A Extended", 20),
                               bg="black", fg="white", command=wp1, height=1, width=5))
                    wp2btn = (Button
                              (wps, text=2, font=("OCR A Extended", 20),
                               bg="black", fg="white", command=wp2, height=1, width=5))
                    wp3btn = (Button
                              (wps, text=3, font=("OCR A Extended", 20),
                               bg="black", fg="white", command=wp3, height=1, width=5))
                    wp1btn.pack()
                    wp2btn.pack()
                    wp3btn.pack()

                def startmen():
                    starts.destroy()
                    startmenu.config(command=opensm)

                def startscr():
                    startd.destroy()
                    startmenu.config(command=openstartscreen)

                def clockswitch_off():
                    if clock2lbl.config(fg="blue"):
                        clock2lbl.config(fg="black")

                def clockswitch_on():
                    if clock2lbl.config(fg="black"):
                        clock2lbl.config(fg="blue")

                def closewndw():
                    settingswindow.destroy()

                closebtn2 = Button(settingswindow, command=closewndw, text="X", font=("ARIAL", 20), bg="red", width=4,
                                   height=1)
                closebtn2.place(y=0, x=1450)

                clockbtnon = Button(settingswindow, command=clockswitch_on, text="Klok uit", bg='black', fg="white",
                                    width=10, height=2)
                clockbtnon.place(x=0, y=0)

                clockbtnoff = Button(settingswindow, command=clockswitch_off, text="Klok aan", bg='black', fg='white',
                                     width=10, height=2)
                clockbtnoff.place(x=0, y=50)

                wallpapersel = Button(settingswindow, text="Achtergronden", command=wpselect, bg='black', fg='white',
                                      width=10, height=2)
                wallpapersel.place(x=0, y=100)

                startmenbtn = Button(settingswindow, command=startmen, text="Start menu", bg="black", fg="white",
                                     width=10, height=2)
                startmenbtn.place(x=0, y=150)

                startscrbtn = Button(settingswindow, command=startscr, text="Start scherm", bg="black", fg="white",
                                     width=10, height=2)
                startscrbtn.place(x=0, y=200)

                settingswindow.mainloop()

            starts.after(30000, close)

            bgname = Label(starts, text="J.[S].A.R.V.I.S.", font=("Engravers MT", 100), bg="black", fg="dark blue")
            bgname.place(x=0, y=350)

            closebtn = Button(starts, command=shutdown, text="Afsluiten", bg="dark blue", fg="black",
                              width=15, height=5, font=("OCR A Extended", 20))
            closebtn.place(y=700, x=0)

            funcbtn1 = Button(starts, command=close, text="Sluit", bg="black", fg="White", width=10, height=5,
                              font=("OCR A Extended", 20))
            funcbtn1.place(y=700, x=250)

            funcbtn2 = Button(starts, command=settings, text="Instellingen", bg="#200040", fg="white",
                              width=12, height=4, font=("OCR A Extended", 20))
            funcbtn2.place(y=680, x=990)

            tbmode = Button(starts, command=textmode,
                            text="Tekst Based Versie", bg="black", fg="white", width=150, height=2)
            tbmode.place(y=0, x=0)

            vnamej = Label(starts, text="J.||P", bg="Black", fg="Blue", font=("OCR A Extended", 50))
            vnamej.place(x=980, y=100)

            vnames = Label(starts, text="S.||R", bg="Black", fg="Blue", font=("OCR A Extended", 50))
            vnames.place(x=980, y=180)

            vnamea = Label(starts, text="A.||O", bg="Black", fg="Blue", font=("OCR A Extended", 50))
            vnamea.place(x=980, y=260)

            vnamer = Label(starts, text="R.||J", bg="Black", fg="Blue", font=("OCR A Extended", 50))
            vnamer.place(x=980, y=340)

            vnamev = Label(starts, text="V.||E", bg="Black", fg="Blue", font=("OCR A Extended", 50))
            vnamev.place(x=980, y=420)

            vnamei = Label(starts, text="I.||C", bg="Black", fg="Blue", font=("OCR A Extended", 50))
            vnamei.place(x=980, y=500)

            vnames = Label(starts, text="S.||T", bg="Black", fg="Blue", font=("OCR A Extended", 50))
            vnames.place(x=980, y=580)

            search = Entry(starts, width=20, font=20)
            search.place(y=550, x=0)

            def opensource():
                string = search.get()
                webbrowser.open("Https://www." + string)

            Button(starts, text="Gaan", command=opensource, width=10, bg="black", fg="white").place(y=600, x=0)

            clock2lbl = Label(starts, font=("OCR A Extended", 25), fg="blue", bg="black")
            clock2lbl.place(y=830, x=1000)

            clock2()

        def opensm():
            startd = Tk()
            startd.geometry("250x400+0+463")
            startd.config(bg="black")
            startd.overrideredirect(True)

            def clock2():
                time_string2 = strftime("%H:%M:%S")
                clock2lbl.config(text=time_string2)

                (s.s.eve_startup.after(10, clock2))

            def shutdown():
                startd.destroy()
                mainscreend.destroy()
                exit()

            def close():
                startd.destroy()

            def textmode():

                languageselector = Tk()
                languageselector.config(bg="black")
                languageselector.geometry("200x200+500+600")
                languageselector.overrideredirect(True)

                def englishver():
                    languageselector.destroy()
                    import os
                    os.startfile("C:/Users/evert/Documents/J.[S].A.R.V.I.S. Project files/"
                                 "Main Files/Text Based/JARVIS English Version/main.py")

                def dutchver():
                    languageselector.destroy()
                    import os
                    os.startfile("C:/Users/evert/Documents/J.[S].A.R.V.I.S. Project files/"
                                 "Main Files/Text Based/JARVIS Dutch Version/main.py")

                dutchversion = Button(languageselector, command=dutchver, bg="black", fg="dark blue", text="Nederlands",
                                      font=("OCR A Extended", 20))
                dutchversion.pack(side=TOP)

                englishversion = Button(languageselector, command=englishver, bg="black", fg="dark blue", text="Engels",
                                        font=("OCR A Extended", 20))
                englishversion.pack(side=TOP)

            def settings():
                settingswindow = Tk()
                settingswindow.attributes("-fullscreen", True)
                settingswindow.config(bg="black")

                def wpselect():
                    settingswindow.destroy()
                    wps = Tk()
                    wps.geometry("250x250+640+270")
                    wps.config(bg="black")
                    wps.overrideredirect(True)

                    def wp1():
                        wp.config(image=wpr1)

                    def wp2():
                        wp.config(image=wpr2)

                    def wp3():
                        wp.config(image=wpr3)

                    def closewps():
                        wps.destroy()

                    wpsc = Button(wps, text="Sluit", command=closewps, bg="black", fg="white")
                    wpsc.pack(side=BOTTOM)

                    wp1btn = (Button
                              (wps, text=1, font=("OCR A Extended", 20),
                               bg="black", fg="white", command=wp1, height=1, width=5))
                    wp2btn = (Button
                              (wps, text=2, font=("OCR A Extended", 20),
                               bg="black", fg="white", command=wp2, height=1, width=5))
                    wp3btn = (Button
                              (wps, text=3, font=("OCR A Extended", 20),
                               bg="black", fg="white", command=wp3, height=1, width=5))
                    wp1btn.pack()
                    wp2btn.pack()
                    wp3btn.pack()

                def startmen():
                    starts.destroy()
                    startmenu.config(command=opensm)

                def startscr():
                    startd.destroy()
                    startmenu.config(command=openstartscreen)

                def clockswitch_off():
                    if clock2lbl.config(fg="blue"):
                        clock2lbl.config(fg="black")

                def clockswitch_on():
                    if clock2lbl.config(fg="black"):
                        clock2lbl.config(fg="blue")

                def closewndw():
                    settingswindow.destroy()

                closebtn2 = Button(settingswindow, command=closewndw, text="X", font=("ARIAL", 20), bg="red", width=4,
                                   height=1)
                closebtn2.place(y=0, x=1450)

                clockbtnon = Button(settingswindow, command=clockswitch_on, text="Klok uit", bg='Black', fg="blue",
                                    width=10, height=2)
                clockbtnon.place(x=0, y=0)

                clockbtnoff = Button(settingswindow, command=clockswitch_off, text="Klok aan", bg='black', fg='Blue',
                                     width=10, height=2)
                clockbtnoff.place(x=0, y=50)

                wallpapersel = Button(settingswindow, text="Achtergronden", command=wpselect, bg='black', fg='blue',
                                      width=10, height=2)
                wallpapersel.place(x=0, y=100)

                startmenbtn = Button(settingswindow, command=startmen, text="Start menu", bg="black", fg="blue",
                                     width=10, height=2)
                startmenbtn.place(x=0, y=150)

                startscrbtn = Button(settingswindow, command=startscr, text="Start scherm", bg="black", fg="blue",
                                     width=10, height=2)
                startscrbtn.place(x=0, y=200)

                settingswindow.mainloop()

            startd.after(30000, close)

            closebtn = Button(startd, command=shutdown, text="Afsluiten", bg="black", fg="white", width=30, height=2)
            closebtn.place(y=350, x=0)

            funcbtn1 = Button(startd, command=close, text="Sluit", bg="black", fg="white", width=30, height=2)
            funcbtn1.place(y=300, x=0)

            funcbtn2 = Button(startd, command=settings, text="Instellingen", bg="black", fg="white", width=30, height=2)
            funcbtn2.place(y=250, x=0)

            tbmode = Button(startd, command=textmode, text="Tekst Based Versie", bg="black", fg="white",
                            width=30, height=2)
            tbmode.place(y=200, x=0)

            name = Label(startd, text="J.[S].A.R.V.I.S.", bg="Black", fg="Blue", font=("OCR A Extended", 20))
            name.pack(side=TOP)

            name2 = Label(startd, text="Project", bg="Black", fg="Blue", font=("OCR A Extended", 20))
            name2.pack(side=TOP)

            clock2lbl = Label(startd, font=("OCR A Extended", 25), fg="blue", bg="black")
            clock2lbl.pack(side=TOP)

            clock2()

        def fulltime():
            timew = Tk()
            timew.geometry("250x200+1290+670")
            timew.overrideredirect(True)
            timew.config(bg="#000030")

            def closetime():
                timew.destroy()

            closetimebtn = Button(timew, command=closetime, bg="red", fg="black", text="X", width=100)
            closetimebtn.pack(side=TOP)

            def detailtime():
                detailtimestring = strftime("%H:%M:%S")
                detailtimelabel.config(text=detailtimestring)

                timew.after(10, detailtime)

            detailtimelabel = Label(timew, font=("OCR A Extended", 20), fg="blue", bg="#000030")
            detailtimelabel.pack(side=TOP)

            detailtime()

            def date():
                datestring = strftime("%d/%m/%Y")
                datelabel.config(text=datestring)

                timew.after(10, date)

            datelabel = Label(timew, font=("OCR A Extended", 20), fg="blue", bg="#000030")
            datelabel.pack(side=TOP)

            date()

            def detaildate():
                detaildatestring = strftime("%A/%B/%Y")
                detaildatelabel.config(text=detaildatestring)

                timew.after(10, detaildate)

            detaildatelabel = Label(timew, font=("OCR A Extended", 15), fg="blue", bg="#000030")
            detaildatelabel.pack(side=TOP)

            detaildate()

            timew.mainloop()

        def clock2d():
            time_string = strftime("%A/%H:%M")
            time_label.config(text=time_string, padx=620)

            mainscreend.after(10, clock2d)

        time_label = Button(mainscreend, font=("OCR A Extended", 20), fg="blue", bg="#000030",
                            width=100, command=fulltime, border=0)
        time_label.place(y=830, x=0)

        clock2d()

        startmenu = Button(mainscreend, bg="Black", image=shutdown_logo, command=opensm, width=50, text="Start")
        startmenu.place(y="835", x="0")

        browser = Button(mainscreend, image=browserlogo, border=0, command=open_browser, bg="black")
        browser.place(x=1400, y=0)

        vscode = Button(mainscreend, bg="black", border=0, image=vscimage, command=open_vsc)
        vscode.place(x=1330, y=0)

        mainscreend.mainloop()

    main_text.pack()

    def clocks():
        time_strings = strftime("%H:%M:%S")
        clockslbl.config(text=time_strings)

        (sseve_startup.after(10, clocks))

    clockslbl = Label(sseve_startup, font=("OCR A Extended", 25), fg="blue", bg="black")
    clockslbl.pack()

    clocks()

    def login_error():
        error = Tk()
        error.title("WARNING")
        error.config(bg="black")
        error.geometry("400x200+500+400")

        errortext = Label(error, text="", font=("OCR A Extended", 25), fg="blue", bg="black")
        errortext.pack()

        errortext.config(text="Invalid Password")

        error.mainloop()

    sseve_startup.mainloop()


startup()
exit()
