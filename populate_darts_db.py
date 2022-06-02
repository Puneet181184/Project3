import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from darts_app.models import darts_db

def add_entry(name,age,dob,country,gender,rank,height,
     darts,titles,finishes):     

	t=darts_db.objects.get_or_create(name=name,age=age,dob=dob,country=country,
          gender=gender,rank=rank,height=height,darts=darts,titles=titles,
          finishes=finishes)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("darts_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
dob=[]
country=[]
gender=[]
rank=[]
height=[]
darts=[]
titles=[]
finishes=[]








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
     darts.append(row["Darts in g"])
     titles.append(row["Titles"])
     finishes.append(row["Finishes"])


     

     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],dob[i],country[i],gender[i],rank[i],height[i],
                  darts[i],titles[i],finishes[i])
	                                                                                                     



















