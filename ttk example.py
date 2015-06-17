import tweepy, time, sys
import tkinter as tk
from tkinter import ttk
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

root = tk.Tk()
root.title("Twitter")
root.configure(background='cyan')
ttk.Style().configure('style.TLabel', foreground='red', background='cyan')
ttk.Style().configure('style.TButton', foreground='red', background='black')

label = ttk.Label(root, text='Watcha Thinkin?', style='style.TLabel')
label.pack()

tweet_text = ttk.Entry(root, width = 40, background='cyan')
tweet_text.pack()

button = ttk.Button(root, text='Tweet!', style='green/black.TButton', command = tweet_data)
button.pack()

root.mainloop()
