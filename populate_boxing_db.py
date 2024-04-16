import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from boxing_app.models import boxing_db

def add_entry(name,age,country,height,weight,wins,losses,
     draws):     

	t=boxing_db.objects.get_or_create(name=name,age=age,country=country,height=height,
          weight=weight,wins=wins,losses=losses,draws=draws)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("boxing_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
country=[]
height=[]
weight=[]
wins=[]
losses=[]
draws=[]







#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     age.append(row["Age"])
     country.append(row["Country"])
     height.append(row["Height in m"])
     weight.append(row["Weight in kg"])
     wins.append(row["Wins"])
     losses.append(row["Losses"])
     draws.append(row["Draws"])
     


     

     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],country[i],height[i],weight[i],wins[i],losses[i],
                  draws[i])
	                                                                                                     



















