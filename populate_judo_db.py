import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from judo_app.models import judo_db

def add_entry(name,age,country,rank,points,gold,silver,bronze):     

	t=judo_db.objects.get_or_create(name=name,age=age,country=country,rank=rank,points=points,gold=gold,silver=silver,bronze=bronze)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("judo_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
country=[]
rank=[]
points=[]
gold=[]
silver=[]
bronze=[]






#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     age.append(row["Age"])
     country.append(row["Country"])
     rank.append(row["Rank"])
     points.append(row["Points"])
     gold.append(row["Gold"])
     silver.append(row["Silver"])
     bronze.append(row["Bronze"])


     

     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],country[i],rank[i],
                  points[i],gold[i],silver[i],bronze[i])
	                                                                                                     



















