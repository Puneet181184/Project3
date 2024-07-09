import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from skating_app.models import skating_db

def add_entry(name,age,dob,gender,club):     

	t=skating_db.objects.get_or_create(name=name,age=age,dob=dob,gender=gender,club=club)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("skating_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
dob=[]
gender=[]
club=[]






#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     age.append(row["Age"])
     dob.append(row["Date of Birth"])
     gender.append(row["Gender"])
     club.append(row["Club"])
     


     

     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],dob[i],gender[i],
                  club[i])
	                                                                                                     



















