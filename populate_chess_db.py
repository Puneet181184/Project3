import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from chess_app.models import chess_db

def add_entry(name,age,dob,nationality,rank,debut,height,weight,
     title,playerid,gender,stdrating,rapidrating,blitzrating,games,wins,
     draws,losses,score):     

	t=chess_db.objects.get_or_create(name=name,age=age,dob=dob,nationality=nationality,rank=rank,
          debut=debut,height=height,weight=weight,
          title=title,playerid=playerid,gender=gender,
          stdrating=stdrating,rapidrating=rapidrating,blitzrating=blitzrating,games=games,
          wins=wins,draws=draws,losses=losses,
          score=score)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("chess_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
dob=[]
nationality=[]
rank=[]
debut=[]
height=[]
weight=[]
title=[]
playerid=[]
gender=[]
stdrating=[]
rapidrating=[]
blitzrating=[]
games=[]
wins=[]
draws=[]
losses=[]
score=[]







#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     age.append(row["Age"])
     dob.append(row["Date of Birth"])
     nationality.append(row["Nationality"])
     rank.append(row["Rank"])
     debut.append(row["Debut"])
     height.append(row["Height in cm"])
     weight.append(row["Weight in kg"])
     title.append(row["Title"])
     playerid.append(row["ID"])
     gender.append(row["Gender"])
     stdrating.append(row["Std Rating"])
     rapidrating.append(row["Rapid Rating"])
     blitzrating.append(row["Blitz Rating"])
     games.append(row["Games"])
     wins.append(row["Wins"])
     draws.append(row["Draws"])
     losses.append(row["Losses"])
     score.append(row["Score in %"])
     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],dob[i],nationality[i],rank[i],debut[i],height[i],weight[i],
                  title[i],playerid[i],gender[i],stdrating[i],rapidrating[i],blitzrating[i],
                  games[i],wins[i],draws[i],losses[i],score[i])
	                                                                                                     



















