from tkinter import *
from time import *
from PIL import ImageTk
import webbrowser
from tkinter import ttk

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
SSEVESTARTUP = Tk()
SSEVESTARTUP.geometry("300x300+500+200")
SSEVESTARTUP.config(bg="Black")
SSEVESTARTUP.overrideredirect(True)

maintext = Label(SSEVESTARTUP, text="Loading J.[S].A.R.V.I.S.", fg="dark blue", bg="black",
                                    font=("ORC A Extended", 15))

password = Entry(SSEVESTARTUP, width=20, font=20)
password.place(x=0, y=280)

passwdlist = ("jarvis" + " admin " + "play")

# working passwords are: jarvis, admin, help, and play


#   login safety sequence
def loginlook():
    login = password.get()
    if login == "jarvis":
        english = Button(SSEVESTARTUP, text="English", bg="black", fg="dark blue", command=englishsetup,
                         font=("OCR A Extended", 20))
        english.place(x=0, y=250)
        dutch = Button(SSEVESTARTUP, text="Nederlands", bg="black", fg="dark blue", command=dutchsetup,
                       font=("OCR A Extended", 18))
        dutch.place(x=140, y=250)
        password.destroy()
        loginbtn.destroy()

    # DEBUG Mode
    elif login == "admin":
        debugmode = Tk()
        debugmode.attributes("-fullscreen", True)
        debugmode.config(bg="black")

    elif login == "help":
        passwordhelp = Label(SSEVESTARTUP, text=passwdlist, bg='black', fg='blue', font=("OCR A Extended", 11))
        passwordhelp.pack(side=TOP)

    else:
        login_error()


loginbtn = Button(SSEVESTARTUP, text="login", command=loginlook)
loginbtn.place(x=250, y=280)

#   JS Signature:

Signature0 = (Label(SSEVESTARTUP, text=("File==SSEVE; STATE==Complete;"
                    "Sequence Code==:"
                    "103AFF540!!VMESS-SSEVE"
                    "01125812240-VWSOS-C0150--!"), fg="black", bg="Black"))
Signature0.pack(side=TOP)


def englishsetup():
    SSEVESTARTUP.destroy()
    mainscreen = Tk()
    mainscreen.attributes("-fullscreen", True)
    mainscreen.config(bg="black")

    #   JS Signature:

    signature1 = (Label(mainscreen, text=("File==SSEVE; STATE==Complete;"
                        "Sequence Code==:"
                        "5837FF540!!SSEVE"
                        "50725203240-VWSOS-C0450--!"), fg="black", bg="Black"))
    signature1.pack(side=TOP)

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

    holowpr = ImageTk.PhotoImage(file="C:/Users/evert/Documents/J.[S].A.R.V.I.S. Project files/Data/brudah.jpg")

    #   (pause line to differentiate between the normal code and the D.D.S.A. storage unit)

    wp = Label(mainscreen, image=wpr1)
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

        #   JS Signature:

        signature2 = (Label(starts, text=("File==SSEVE; STATE==Complete;"
                                        "Sequence Code==:"
                                        "103GDQ540!!VMESS"
                                        "01586712240-VWSOS-C9990--!"), fg="black", bg="Black"))
        signature2.pack(side=TOP)

        def clock2():
            time_string2 = strftime("%H:%M:%S")
            clock2lbl.config(text=time_string2)

            (SSEVESTARTUP.after(10, clock2))

        def shutdown():
            starts.destroy()
            mainscreen.destroy()

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

            #   JS Signature:

            signature3 = (Label(SSEVESTARTUP, text=("File==settings; STATE==Complete;"
                                                    "Sequence Code==:"
                                                    "103UPF540!!SSEVE"
                                                    "09925812240-VWSOS-C0890--!"), fg="black", bg="Black"))
            signature3.pack(side=TOP)

            def holomode():
                settingswindow.destroy()
                wp.config(image=holowpr)
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
                startmenu.config(command=openstartscreen)

            def clockswitch_off():
                if clock2lbl.config(fg="blue"):
                    clock2lbl.config(fg="black")

            def clockswitch_on():
                if clock2lbl.config(fg="black"):
                    clock2lbl.config(fg="blue")

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

        tbmode = Button(starts, command=textmode,
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

            (SSEVESTARTUP.after(10, clock2))

        def shutdown():
            start.destroy()
            mainscreen.destroy()

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

            englishversion = Button(languageselector, command=englishver, bg="black", fg="dark blue", text="English",
                                    font=("OCR A Extended", 20))
            englishversion.pack(side=TOP)

        def settings():
            settingswindow = Tk()
            settingswindow.attributes("-fullscreen", True)
            settingswindow.config(bg="black")

            def holomode():
                settingswindow.destroy()
                start.destroy()
                wp.config(image=holowpr)
                startscr1()
                time_label.destroy()
                starts.geometry("1920x1080")

            def startmen1():
                starts.destroy()
                startmenu.config(command=opensm)

            def startscr1():
                start.destroy()
                startmenu.config(command=openstartscreen)

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

            def clockswitch_on():
                if clock2lbl.config(fg="black"):
                    clock2lbl.config(fg="blue")

            def closewndw():
                settingswindow.destroy()

            holomodebtn = Button(settingswindow, command=holomode, text="hologhraphic interface mode", bg="black",
                                 width=20, height=2, fg="blue", font=("OCR A Extended", 20))
            holomodebtn.place(y=500, x=0)

            closebtn2 = Button(settingswindow, command=closewndw, text="X", font=("ARIAL", 20), bg="red", width=4,
                               height=1)
            closebtn2.place(y=0, x=1450)

            clockbtnon = Button(settingswindow, command=clockswitch_on, text="clock off", bg='Black', fg="blue",
                                width=10, height=2)
            clockbtnon.place(x=0, y=0)

            clockbtnoff = Button(settingswindow, command=clockswitch_off, text="clock on", bg='black', fg='Blue',
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

        tbmode = Button(start, command=textmode, text="Text Based Version", bg="black", fg="white", width=30, height=2)
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

        mainscreen.after(10, clockd)

    time_label = Button(mainscreen, font=("OCR A Extended", 20), fg="blue", bg="#000030",
                        width=100, command=fulltime, border=0)
    time_label.place(y=830, x=0)

    clockd()

    startmenu = Button(mainscreen, bg="Black", image=shutdown_logo, command=opensm, width=50, text="Start")
    startmenu.place(y="835", x="0")

    browser = Button(mainscreen, image=browserlogo, border=0, command=open_browser, bg="black")
    browser.place(x=1400, y=0)

    vscode = Button(mainscreen, bg="black", image=vscimage, border=0, command=open_vsc)
    vscode.place(x=1330, y=0)

    mainscreen.mainloop()


def dutchsetup():
    SSEVESTARTUP.destroy()
    mainscreend = Tk()
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

            (SSEVESTARTUP.after(10, clock2))

        def shutdown():
            starts.destroy()
            mainscreend.destroy()

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

            (SSEVESTARTUP.after(10, clock2))

        def shutdown():
            startd.destroy()
            mainscreend.destroy()

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

        tbmode = Button(startd, command=textmode, text="Tekst Based Versie", bg="black", fg="white", width=30, height=2)
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


maintext.pack()


def clocks():
    time_strings = strftime("%H:%M:%S")
    clockslbl.config(text=time_strings)

    (SSEVESTARTUP.after(10, clocks))


clockslbl = Label(SSEVESTARTUP, font=("OCR A Extended", 25), fg="blue", bg="black")
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


def sig_check():
    if not Signature0:
        errortext.config(text=not + "not found")
        error_message()


sig_check()

SSEVESTARTUP.mainloop()
