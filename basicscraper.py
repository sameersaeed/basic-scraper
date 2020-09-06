#sameer saeed 
#web scraping on a practice site
#collects specific data from the site and dumps it into an excel file

import bs4 
import csv
import re
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#finds url and stores page's html data
my_url = 'http://books.toscrape.com/'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

#finds all containers on page
containers = page_soup.findAll("li", {"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
container = containers[0]

#creating the excel sheet that the data will be written to
filename = "itemslist.csv"
f = open(filename, "w")

headers = "book name, price ($)\n"

filename = "itemslist.csv"
f.write(headers)

#iterates over each container in site
for container in containers:
    #gets name and price 
    product_name = container.div.a.img["alt"]
    
    #gets the price solely in decimal format and converts it to a string
    price = container.findAll("p", {"class":"price_color"})
    priceStr = re.findall("\d+\.\d+",str(price))
    priceStr = ",".join(priceStr)
    
    
    print("product_name: " + product_name)
    print("price: $",priceStr)

    f.write(product_name.replace(",", " ") + "," + priceStr +"\n")
f.close()
