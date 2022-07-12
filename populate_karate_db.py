import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from karate_app.models import karate_db

def add_entry(name,age,country,gender,rank,category,
     worldgold,worldsilver,worldbronze):     

	t=karate_db.objects.get_or_create(name=name,age=age,country=country,
          gender=gender,rank=rank,category=category,worldgold=worldgold,worldsilver=worldsilver,
          worldbronze=worldbronze)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("karate_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
country=[]
gender=[]
rank=[]
category=[]
worldgold=[]
worldsilver=[]
worldbronze=[]







#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     age.append(row["Age"])
     country.append(row["Country"])
     gender.append(row["Gender"])
     rank.append(row["Rank"])
     category.append(row["Category"])
     worldgold.append(row["Worldgold"])
     worldsilver.append(row["Worldsilver"])
     worldbronze.append(row["Worldbronze"])


     

     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],country[i],gender[i],rank[i],category[i],worldgold[i],
                  worldsilver[i],worldbronze[i])
	                                                                                                     



















