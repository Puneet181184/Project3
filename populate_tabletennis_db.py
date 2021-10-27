import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from tabletennis_app.models import tabletennis_db

def add_entry(name,age,dob,gender,country,debut,height,weight,
     plays,grip,rank,bestrank,singlesplayed,singleswon,
     singleslost,doublesplayed,doubleswon,doubleslost,
     totalplayed,totalwon,totallost):     

	t=tabletennis_db.objects.get_or_create(name=name,age=age,dob=dob,gender=gender,country=country,
          debut=debut,height=height,weight=weight,plays=plays,grip=grip,
          rank=rank,bestrank=bestrank,
          singlesplayed=singlesplayed,singleswon=singleswon,singleslost=singleslost,doublesplayed=doublesplayed,
          doubleswon=doubleswon,doubleslost=doubleslost,
          totalplayed=totalplayed,totalwon=totalwon,totallost=totallost)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("tabletennis_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
dob=[]
gender=[]
country=[]
debut=[]
height=[]
weight=[]
plays=[]
grip=[]
rank=[]
bestrank=[]
singlesplayed=[]
singleswon=[]
singleslost=[]
doublesplayed=[]
doubleswon=[]
doubleslost=[]
totalplayed=[]
totalwon=[]
totallost=[]







#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     age.append(row["Age"])
     dob.append(row["Date of Birth"])
     gender.append(row["Gender"])
     country.append(row["Country"])
     debut.append(row["Debut"])
     height.append(row["Height in m"])
     weight.append(row["Weight in kg"])
     plays.append(row["Plays"])
     grip.append(row["Grip"])
     rank.append(row["Rank"])
     bestrank.append(row["Best Rank"])
     singlesplayed.append(row["Singles Played"])
     singleswon.append(row["Singles Won"])
     singleslost.append(row["Singles Lost"])
     doublesplayed.append(row["Doubles Played"])
     doubleswon.append(row["Doubles Won"])
     doubleslost.append(row["Doubles Lost"])
     totalplayed.append(row["Total Played"])
     totalwon.append(row["Total Won"])
     totallost.append(row["Total Lost"])

     

     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],dob[i],gender[i],country[i],debut[i],height[i],weight[i],
                  plays[i],grip[i],rank[i],bestrank[i],singlesplayed[i],
                  singleswon[i],singleslost[i],doublesplayed[i],
                  doubleswon[i],doubleslost[i],totalplayed[i],
                  totalwon[i],totallost[i])
	                                                                                                     



















