import urllib.request
page = urllib.request.urlopen(“http://www.beans-r-us.appspot.com/prices-loyalty.html")
text = page.read().decode(“utf8")
where = text.find(">$")
start_of_price = where + 2
end_of_price = start of price + 4
price = tex[start_of_price:end_of_price]
print(price)


