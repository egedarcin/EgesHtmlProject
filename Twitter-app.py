#--This program tweets to https://twitter.com/darchibald_#
#--You have to change consumer key/secret/access key/secret for your own account.#
#--This program uses pygame, but there is no python 3 support for macOS.#
#--To download pygame for macOS: http://florian-berger.de/en/articles/installing-pygame-for-python-3-on-os-x/#

import tweepy, time, sys
from tkinter import *
import tkinter.messagebox
import pygame.mixer

sounds = pygame.mixer
sounds.init()

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

def play_sent_sound():
    sent_s.play()

def tweet_data():
   input = tweet_text.get()
   api.update_status(status= input)
   tweet_text.delete(0, END)

CONSUMER_KEY = "N7e5kWDuVUZUIQvECbWLxMs4l"
CONSUMER_SECRET = "LGXwsNRAAZADnmXa1aq9fZu8AheOZCzC3jLqw3BzR83y7LVSBn"
ACCESS_KEY = "3162862942-ZeaQlEbeiDieXoJr7pdQr4BSLqXH2ZwGDncsWgh"
ACCESS_SECRET = "aN0lX8gEsaSAKGETBrem2ybdbM4BGEoAj1A1gIyIjwxjV"
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


app = Tk()
app.title("Twitter")

app.geometry("300x300+100+100")
app.configure(background='cyan' )
Label(app, text = "Whatcha Thinkin?", background='cyan').pack()
tweet_text = Entry(app,  width = 150, background='cyan')
tweet_text.pack()

sent_s = sounds.Sound("beep.wav")

Button (app, text = "Tweet!",
             width = 20, command = combine_funcs(tweet_data, play_sent_sound)).pack()

app.mainloop()
