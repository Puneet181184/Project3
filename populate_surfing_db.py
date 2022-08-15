import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from surfing_app.models import surfing_db

def add_entry(name,age,dob,country,gender,rank,debut,height,weight,
     wins,score):     

	t=surfing_db.objects.get_or_create(name=name,age=age,dob=dob,country=country,
          gender=gender,rank=rank,debut=debut,height=height,weight=weight,
          wins=wins,score=score)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("surfing_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
dob=[]
country=[]
gender=[]
rank=[]
debut=[]
height=[]
weight=[]
wins=[]
score=[]







#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     age.append(row["Age"])
     dob.append(row["Date of Birth"])
     country.append(row["Country"])
     gender.append(row["Gender"])
     rank.append(row["Rank"])
     debut.append(row["Debut"])
     height.append(row["Height in cm"])
     weight.append(row["Weight in kg"])
     wins.append(row["Wins"])
     score.append(row["Score"])
     
     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],dob[i],country[i],gender[i],rank[i],debut[i],height[i],weight[i],
                  wins[i],score[i])
	                                                                                                     



















