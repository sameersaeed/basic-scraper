#sameer saeed 
#web scraping on a practice site
#collects specific data from the site and dumps it into an excel file

import bs4 
import csv
import re
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'http://books.toscrape.com/'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("li", {"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
container = containers[0]

filename = "itemslist.csv"
f = open(filename, "w")

headers = "book name, price ($)\n"

filename = "itemslist.csv"
f.write(headers)

for container in containers:
    #brand = container.div.div.a.img["title"]

    product_name = container.div.a.img["alt"]

    price = container.findAll("p", {"class":"price_color"})
    priceStr = re.findall("\d+\.\d+",str(price))
    priceStr = ",".join(priceStr)
    print("product_name: " + product_name)
    print("price: $",priceStr)

    f.write(product_name.replace(",", " ") + "," + priceStr +"\n")
f.close()

#python /Users/sameersaeed/Desktop/Files/webscr/bookscr_test.py
