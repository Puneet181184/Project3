import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from badminton_app.models import badminton_db

def add_entry(name,age,dob,gender,country,debut,height,weight,
     plays,rank,tourrank,careerwins,singlesplayed,singleswon,
     singleslost,doublesplayed,doubleswon,doubleslost,
     mixedplayed,mixedwon,mixedlost):     

	t=badminton_db.objects.get_or_create(name=name,age=age,dob=dob,gender=gender,country=country,
          debut=debut,height=height,weight=weight,plays=plays,rank=rank,
          tourrank=tourrank,careerwins=careerwins,
          singlesplayed=singlesplayed,singleswon=singleswon,singleslost=singleslost,doublesplayed=doublesplayed,
          doubleswon=doubleswon,doubleslost=doubleslost,
          mixedplayed=mixedplayed,mixedwon=mixedwon,mixedlost=mixedlost)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("badminton_players.csv","r")
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
rank=[]
tourrank=[]
careerwins=[]
singlesplayed=[]
singleswon=[]
singleslost=[]
doublesplayed=[]
doubleswon=[]
doubleslost=[]
mixedplayed=[]
mixedwon=[]
mixedlost=[]







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
     rank.append(row["Rank"])
     tourrank.append(row["Tour Rank"])
     careerwins.append(row["Career wins"])
     singlesplayed.append(row["Singles Played"])
     singleswon.append(row["Singles Won"])
     singleslost.append(row["Singles Lost"])
     doublesplayed.append(row["Doubles Played"])
     doubleswon.append(row["Doubles Won"])
     doubleslost.append(row["Doubles Lost"])
     mixedplayed.append(row["Mixed Played"])
     mixedwon.append(row["Mixed Won"])
     mixedlost.append(row["Mixed Lost"])

     

     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],dob[i],gender[i],country[i],debut[i],height[i],weight[i],
                  plays[i],rank[i],tourrank[i],careerwins[i],singlesplayed[i],
                  singleswon[i],singleslost[i],doublesplayed[i],
                  doubleswon[i],doubleslost[i],mixedplayed[i],
                  mixedwon[i],mixedlost[i])
	                                                                                                     



















