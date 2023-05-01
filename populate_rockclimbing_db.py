import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from rockclimbing_app.models import rockclimbing_db

def add_entry(name,age,country,height,weight,rankingboulder,rankinglead):     

	t=rockclimbing_db.objects.get_or_create(name=name,age=age,country=country,height=height,
          weight=weight,rankingboulder=rankingboulder,rankinglead=rankinglead)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("rockclimbing_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
country=[]
height=[]
weight=[]
rankingboulder=[]
rankinglead=[]







#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     age.append(row["Age"])
     country.append(row["Country"])
     height.append(row["Height in m"])
     weight.append(row["Weight in kg"])
     rankingboulder.append(row["Ranking Boulder"])
     rankinglead.append(row["Ranking Lead"])


     

     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],country[i],height[i],weight[i],rankingboulder[i],rankinglead[i])
	                                                                                                     



















