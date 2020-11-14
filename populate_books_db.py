import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from books_app.models import books_db

def add_entry(title,author,publisher,isbn,pages,year,price):
	t=books_db.objects.get_or_create(title=title,author=author,publisher=publisher,isbn=isbn,pages=pages,year=year,price=price)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("books_titles.csv","r")
reader=csv.DictReader(csvfile)
title=[]
author=[]
publisher=[]
isbn=[]
pages=[]
year=[]
price=[]



#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     title.append(row["Book Title"])
     author.append(row["Author"])
     publisher.append(row["Publisher"])
     isbn.append(row["ISBN"])
     pages.append(row["Number of Pages"])
     year.append(row["Year"])
     price.append(row["Price"])



#inserting values into the Table
for i in range(0,len(title)):
	add_entry(title[i],author[i],publisher[i],isbn[i],pages[i],year[i],price[i])
	





















