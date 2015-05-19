from tkinter import*
import pygame.mixer

app = Tk()
app.title("Head First Mix")
app.geometry('250x100+200+100')

sound_file = "Dubstep.wav"

mixer = pygame.mixer
mixer.init()

def track_start():
    track.play(loops = -1)
def track_stop():
    track.stop()

track = mixer.Sound(sound_file)

track_playing = IntVar()
start_button = Button(app, command = track_start, text = "Start")
start_button.pack(side = LEFT)
stop_button = Button(app, command = track_stop, text = "Stop")
stop_button.pack(side = RIGHT)
    
def shutdown():
    mixer.stop()
    app.destroy()

app.protocol("WM_DELETE_WINDOW", shutdown)

app.mainloop()

