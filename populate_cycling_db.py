import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from cycling_app.models import cycling_db

def add_entry(name,age,dob,country,debut,gender,rank,height,
     weight,points,wins,grandtours,classics):     

	t=cycling_db.objects.get_or_create(name=name,age=age,dob=dob,country=country,debut=debut,
          gender=gender,rank=rank,height=height,weight=weight,points=points,
          wins=wins,grandtours=grandtours,
          classics=classics)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("cycling_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
dob=[]
country=[]
debut=[]
gender=[]
rank=[]
height=[]
weight=[]
points=[]
wins=[]
grandtours=[]
classics=[]







#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     age.append(row["Age"])
     dob.append(row["Date of Birth"])
     country.append(row["Country"])
     debut.append(row["Debut"])
     gender.append(row["Gender"])
     rank.append(row["Rank"])
     height.append(row["Height in m"])
     weight.append(row["Weight in kg"])
     points.append(row["Points"])
     wins.append(row["Wins"])
     grandtours.append(row["Grand Tours"])
     classics.append(row["Classics"])


     

     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],dob[i],country[i],debut[i],gender[i],rank[i],height[i],
                  weight[i],points[i],wins[i],grandtours[i],classics[i])
	                                                                                                     



















