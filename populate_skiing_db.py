import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from skiing_app.models import skiing_db

def add_entry(name,age,dob,height,skitype):     

	t=skiing_db.objects.get_or_create(name=name,age=age,dob=dob,height=height,skitype=skitype)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("skiing_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
dob=[]
height=[]
skitype=[]







#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     age.append(row["Age"])
     dob.append(row["Date of Birth"])
     height.append(row["Height in cm"])
     skitype.append(row["skitype"])
     
     

     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],dob[i],height[i],skitype[i])
	                                                                                                     



















