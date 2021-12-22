import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from weightlifting_app.models import weightlifting_db

def add_entry(name,age,dob,country,gender,category,rank,height,
     weight,snatch,jerk,total):     

	t=weightlifting_db.objects.get_or_create(name=name,age=age,dob=dob,country=country,gender=gender,
          category=category,rank=rank,height=height,weight=weight,snatch=snatch,
          jerk=jerk,total=total)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("weightlifting_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
dob=[]
country=[]
gender=[]
category=[]
rank=[]
height=[]
weight=[]
snatch=[]
jerk=[]
total=[]







#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     age.append(row["Age"])
     dob.append(row["DOB"])
     country.append(row["Country"])
     gender.append(row["Gender"])
     category.append(row["Category in kg"])
     rank.append(row["Rank"])
     height.append(row["Height in m"])
     weight.append(row["Weight in kg"])
     snatch.append(row["Snatch"])
     jerk.append(row["Jerk"])
     total.append(row["Total"])

     

     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],dob[i],country[i],gender[i],category[i],rank[i],height[i],weight[i],
                  snatch[i],jerk[i],total[i])
	                                                                                                     



















