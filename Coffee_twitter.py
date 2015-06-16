import tweepy, time, sys, urllib.request

CONSUMER_KEY = "N7e5kWDuVUZUIQvECbWLxMs4l"
CONSUMER_SECRET = "LGXwsNRAAZADnmXa1aq9fZu8AheOZCzC3jLqw3BzR83y7LVSBn"
ACCESS_KEY = "3162862942-ZeaQlEbeiDieXoJr7pdQr4BSLqXH2ZwGDncsWgh"
ACCESS_SECRET = "aN0lX8gEsaSAKGETBrem2ybdbM4BGEoAj1A1gIyIjwxjV"
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)



def get_price():
 page = urllib.request.urlopen("http://www.beans-r-us.appspot.com/prices-loyalty.html")
 text = page.read().decode("utf8")
 where = text.find(">$")
 start_of_price = where + 2
 end_of_price = start_of_price + 4
 price = (text[start_of_price:end_of_price])
 return float(text[start_of_price:end_of_price])

price_now = input("Do you want to see the price now(Y/N)?")
if price_now == "Y":
   api.update_status(status= get_price())
else:
   price = 99.99
   while price > 4.74:
    time.sleep(900)
    price = get_price()
   api.update_status(status= 'BUY!')
 
