import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from iceskating_app.models import iceskating_db

def add_entry(name,age,country,height,weight,level):     

	t=iceskating_db.objects.get_or_create(name=name,age=age,country=country,height=height,weight=weight,level=level)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("iceskating_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
country=[]
height=[]
weight=[]
level=[]






#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     age.append(row["Age"])
     country.append(row["Country"])
     height.append(row["Height in m"])
     weight.append(row["Weight in kg"])
     level.append(row["Level"])


     

     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],country[i],height[i],
                  weight[i],level[i])
	                                                                                                     



















