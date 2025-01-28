import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from paragliding_app.models import paragliding_db

def add_entry(name,age,country,playerid,gender,):     

	t=paragliding_db.objects.get_or_create(name=name,age=age,country=country,
          playerid=playerid,gender=gender)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("paragliding_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
country=[]
playerid=[]
gender=[]







#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     age.append(row["Age"])
     country.append(row["Country"])
     playerid.append(row["ID"])
     gender.append(row["Gender"])
    
     
     

     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],country[i],playerid[i],gender[i])
	                                                                                                     



















