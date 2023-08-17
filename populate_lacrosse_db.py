import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from lacrosse_app.models import lacrosse_db

def add_entry(name,age,country,rank,height,weight):     

	t=lacrosse_db.objects.get_or_create(name=name,age=age,country=country,rank=rank,
          height=height,weight=weight)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("lacrosse_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
country=[]
rank=[]
height=[]
weight=[]







#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     age.append(row["Age"])
     country.append(row["Country"])
     rank.append(row["Rank"])
     height.append(row["Height in feet"])
     weight.append(row["Weight in pounds"])


     

     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],country[i],rank[i],height[i],
                  weight[i])
	                                                                                                     



















