import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from football_app.models import football_db

def add_entry(name,age,dob,nationality,birthplace,fifaid,debut,position,league,club,
     height,weight,foot,matches,goals,assists,penaltyscored,penaltymissed,goalsconceded,
     yellowcards,redcards):     

	t=cricket_db.objects.get_or_create(name=name,age=age,dob=dob,nationality=nationality,birthplace=birthplace,
          fifaid=fifaid,debut=debut,position=position,league=league,
          club=club,height=height,weight=weight,foot=foot,
          matches=matches,goals=goals,assists=assists,penaltyscored=penaltyscored,
          penaltymissed=penaltymissed,goalsconceded=goalsconceded,yellowcards=yellowcards,
          redcards=redcards)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("football_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
dob=[]
nationality=[]
birthplace=[]
fifaid=[]
debut=[]
position=[]
league=[]
club=[]
height=[]
weight=[]
foot=[]
matches=[]
goals=[]
assists=[]
penaltyscored=[]
penaltymissed=[]
goalsconceded=[]
yellowcards=[]
redcards=[]






#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     age.append(row["Age"])
     dob.append(row["Date of Birth"])
     nationality.append(row["Nationality"])
     birthplace.append(row["Birthplace"])
     fifaid.append(row["FIFA ID"])
     debut.append(row["debut"])
     position.append(row["Position"])
     league.append(row["League"])
     club.append(row["Club"])
     height.append(row["Height"])
     weight.append(row["Weight in lbs"])
     foot.append(row["Preferred foot"])
     matches.append(row["Matches"])
     goals.append(row["Goals"])
     assists.append(row["Assists"])
     penaltyscored.append(row["Penalties Scored"])
     penaltymissed.append(row["Penalties Missed"])
     goalsconceded.append(row["Goals Conceded"])
     yellowcards.append(row["Yellow Cards"])
     redcards.append(row["Red Cards"])



#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],dob[i],nationality[i],birthplace[i],fifaid[i],debut[i],position[i],league[i],
                  club[i],height[i],weight[i],foot[i],matches[i],goals[i],assists[i],
                  penaltyscored[i],penaltymissed[i],goalsconceded[i],yellowcards[i],redcards[i])
	





















