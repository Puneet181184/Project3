import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from triathlon_app.models import triathlon_db

def add_entry(name,dob,country,gender,rank,wins):     

	t=triathlon_db.objects.get_or_create(name=name,dob=dob,country=country,
          gender=gender,rank=rank,wins=wins)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("triathlon_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
dob=[]
country=[]
gender=[]
rank=[]
wins=[]






#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     dob.append(row["Date of Birth"])
     country.append(row["Country"])
     gender.append(row["Gender"])
     rank.append(row["Rank"])
     wins.append(row["Wins"])
     
     

     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],dob[i],country[i],gender[i],rank[i],wins[i])
	                                                                                                     



















