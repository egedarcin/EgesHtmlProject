from tkinter import *

app = Tk()
app.title("Button")
app.geometry('300x100+300+200')

flipper = IntVar()

def flip_it():
    if flipper.get() == 1:
        print("Cool. I'm all ON, man!")
    else:
        print("Phooey. I'm OFF.")

Checkbutton(app, variable = flipper, command = flip_it,text = "Flip it?").pack()
app.mainloop()
