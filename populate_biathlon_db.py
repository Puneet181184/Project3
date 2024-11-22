import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from biathlon_app.models import biathlon_db

def add_entry(name,dob,country,gender,rank,points):     

	t=biathlon_db.objects.get_or_create(name=name,dob=dob,country=country,
          gender=gender,rank=rank,points=points)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("biathlon_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
dob=[]
country=[]
gender=[]
rank=[]
points=[]






#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     dob.append(row["Date of Birth"])
     country.append(row["Country"])
     gender.append(row["Gender"])
     rank.append(row["Rank"])
     points.append(row["Points"])
     
     

     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],dob[i],country[i],gender[i],rank[i],points[i])
	                                                                                                     



















