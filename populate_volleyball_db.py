import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from volleyball_app.models import volleyball_db

def add_entry(name,age,dob,country,gender,rank,height,weight,points):     

	t=volleyball_db.objects.get_or_create(name=name,age=age,dob=dob,country=country,
          gender=gender,rank=rank,height=height,weight=weight,points=points)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("volleyball_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
dob=[]
country=[]
gender=[]
rank=[]
height=[]
weight=[]
points=[]







#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     age.append(row["Age"])
     dob.append(row["Date of Birth"])
     country.append(row["Country"])
     gender.append(row["Gender"])
     rank.append(row["Rank"])
     height.append(row["Height in m"])
     weight.append(row["Weight in kg"])
     points.append(row["Points"])


     

     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],dob[i],country[i],gender[i],rank[i],height[i],weight[i],
                  points[i])
	                                                                                                     



















