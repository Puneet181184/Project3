import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from pool_app.models import pool_db

def add_entry(name,age,dob,gender,country,rank,wpanumber,
     usopenpoints ,austriaopenpoints,worldcuppoints,totalpoints):     

	t=pool_db.objects.get_or_create(name=name,age=age,dob=dob,gender=gender,country=country,
          rank=rank,wpanumber=wpanumber,usopenpoints=usopenpoints,austriaopenpoints=austriaopenpoints,
          worldcuppoints=worldcuppoints,totalpoints=totalpoints)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("pool_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
dob=[]
gender=[]
country=[]
rank=[]
wpanumber=[]
usopenpoints=[]
austriaopenpoints=[]
worldcuppoints=[]
totalpoints=[]








#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     age.append(row["Age"])
     dob.append(row["Date of Birth"])
     gender.append(row["Gender"])
     country.append(row["Country"])
     rank.append(row["Rank"])
     wpanumber.append(row["WPA Number"])
     usopenpoints.append(row["US Open Points"])
     austriaopenpoints.append(row["Austria Open Points"])
     worldcuppoints.append(row["World Cup Points"])
     totalpoints.append(row["Total Points"])

     

     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],dob[i],gender[i],country[i],rank[i],wpanumber[i],
                  usopenpoints[i],austriaopenpoints[i],worldcuppoints[i],totalpoints[i])
	                                                                                                     



















