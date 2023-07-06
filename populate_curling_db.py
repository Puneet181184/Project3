import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from curling_app.models import curling_db

def add_entry(name,age,country,ranking):     

	t=curling_db.objects.get_or_create(name=name,age=age,country=country,ranking=ranking)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("curling_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
country=[]
ranking=[]







#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     age.append(row["Age"])
     country.append(row["Country"])
     ranking.append(row["Ranking"])


     

     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],country[i],ranking[i])
	                                                                                                     



















