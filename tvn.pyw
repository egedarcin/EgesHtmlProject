from tkinter import *
app = Tk()
app.title("TVN Game Show")
app.geometry('300x100+200+100')
b1 = Button(app, text = "Correct!", width = 10)
b1.pack(side = 'left', padx = 10, pady = 10)

b2 = Button(app, text = "Wrong!", width = 10)
b2.pack(side = 'right', padx = 10, pady = 10)

app.mainloop
