#--This program tweets to https://twitter.com/darchibald_#
#--You have to change consumer key/secret/access key/secret for your own account.#
#--This program uses tweepy. To install: open command line and paste this: pip install tweepy #
#-- If you don't have pip: paste this to the command line: sudo apt-get install python-pip #

import tweepy, time, sys
from tkinter import *
import tkinter.messagebox

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

app.geometry("300x100+100+100")
app.configure(background='cyan' )
Label(app, text = "Whatcha Thinkin?", background='cyan').pack()
tweet_text = Entry(app,  width = 150, background='cyan')
tweet_text.pack()

Button (app, text = "Tweet!",
             width = 20, command = tweet_data).pack()

app.mainloop()
