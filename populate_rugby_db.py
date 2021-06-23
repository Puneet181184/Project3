import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from rugby_app.models import rugby_db

def add_entry(name,age,dob,nationality,team,position,debut,height,weight,
     matches,wins,draws,losses,minutes,started,points,
     tries,drops,penalties,conversions,yellowcards,redcards):     

	t=rugby_db.objects.get_or_create(name=name,age=age,dob=dob,nationality=nationality,
          team=team,position=position,height=height,weight=weight,debut=debut,
          matches=matches,wins=wins,
          draws=draws,losses=losses,minutes=minutes,started=started,
          points=points,tries=tries,drops=drops,
          penalties=penalties,conversions=conversions,yellowcards=yellowcards,redcards=redcards)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("rugby_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
dob=[]
nationality=[]
team=[]
position=[]
height=[]
weight=[]
debut=[]
matches=[]
wins=[]
draws=[]
losses=[]
minutes=[]
started=[]
points=[]
tries=[]
drops=[]
penalties=[]
conversions=[]
yellowcards=[]
redcards=[]






#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     age.append(row["Age"])
     dob.append(row["Date of Birth"])
     nationality.append(row["Nationality"])
     team.append(row["Team"])
     position.append(row["Position"])
     debut.append(row["Debut"])
     height.append(row["Height in cm"])
     weight.append(row["Weight in kg"])
     matches.append(row["Matches"])
     wins.append(row["Wins"])
     draws.append(row["Draws"])
     losses.append(row["Losses"])
     minutes.append(row["Minutes"])
     started.append(row["Started"])
     points.append(row["Points"])
     tries.append(row["Tries"])
     drops.append(row["Drops"])
     penalties.append(row["Penalties"])
     conversions.append(row["Conversions"])
     yellowcards.append(row["Yellow Cards"])
     redcards.append(row["Red Cards"])
     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],dob[i],nationality[i],team[i],position[i],debut[i],height[i],weight[i],
                  matches[i],wins[i],draws[i],losses[i],minutes[i],
                  started[i],points[i],tries[i],drops[i],penalties[i],conversions[i],yellowcards[i],redcards[i])
	                                                                                                     



















