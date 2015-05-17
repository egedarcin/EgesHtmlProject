from tkinter import *

app = Tk()
app.title("Button")
app.geometry('300x100+300+200')

def button_click():
    print("I've just been touched you pervert!")

b = Button(app, text = "Click on me!", width = 15, command = button_click)
b.pack(padx = 10, pady = 10)


app.mainloop()
