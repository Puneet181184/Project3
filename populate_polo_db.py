import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from polo_app.models import polo_db

def add_entry(name,age,country,status,points):     

	t=polo_db.objects.get_or_create(name=name,age=age,country=country,
          status=status,points=points)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("polo_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
country=[]
status=[]
points=[]







#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     age.append(row["Age"])
     country.append(row["Country"])
     status.append(row["Status"])
     points.append(row["Points"])


     

     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],country[i],status[i],
                  points[i])
	                                                                                                     



















