import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from golf_app.models import golf_db

def add_entry(name,age,dob,country,currentrank,bestrank,debut,height,weight,
     events,madecuts,first,second,third,fourth,totalpoints,
     averagepoints,divisor):     

	t=golf_db.objects.get_or_create(name=name,age=age,dob=dob,country=country,
          currentrank=currentrank,bestrank=bestrank,debut=debut,height=height,weight=weight,
          events=events,madecuts=madecuts,
          first=first,second=second,third=third,fourth=fourth,
          totalpoints=totalpoints,averagepoints=averagepoints,divisor=divisor)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("golf_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
dob=[]
country=[]
currentrank=[]
bestrank=[]
debut=[]
height=[]
weight=[]
events=[]
madecuts=[]
first=[]
second=[]
third=[]
fourth=[]
totalpoints=[]
averagepoints=[]
divisor=[]






#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     age.append(row["Age"])
     dob.append(row["Date of Birth"])
     country.append(row["Country"])
     currentrank.append(row["Current Rank"])
     bestrank.append(row["Best Rank"])
     debut.append(row["Debut"])
     height.append(row["Height in m"])
     weight.append(row["Weight in kg"])
     events.append(row["Events"])
     madecuts.append(row["Made Cuts"])
     first.append(row["First"])
     second.append(row["Second"])
     third.append(row["Third"])
     fourth.append(row["Fourth"])
     totalpoints.append(row["Total Points"])
     averagepoints.append(row["Average Points"])
     divisor.append(row["Divisor"])
     

     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],dob[i],country[i],currentrank[i],bestrank[i],debut[i],height[i],weight[i],
                  events[i],madecuts[i],first[i],second[i],third[i],
                  fourth[i],totalpoints[i],averagepoints[i],divisor[i])
	                                                                                                     



















