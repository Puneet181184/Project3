import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from icehockey_app.models import icehockey_db

def add_entry(name,age,dob,nationality,team,position,debut,height,weight,
     games,assists,goals,powerplaygoals,shorthandgoals,wininggoals,overtimegoals,
     points,powerplaypoints,shorthandpoints,shots,shotspercentage,penaltyminutes,winspercentage):     

	t=icehockey_db.objects.get_or_create(name=name,age=age,dob=dob,nationality=nationality,
          team=team,position=position,height=height,weight=weight,debut=debut,
          games=games,assists=assists,
          goals=goals,powerplaygoals=powerplaygoals,shorthandgoals=shorthandgoals,wininggoals=wininggoals,
          overtimegoals=overtimegoals,points=points,powerplaypoints=powerplaypoints,
          shorthandpoints=shorthandpoints,shots=shots,shotspercentage=shotspercentage,
          penaltyminutes=penaltyminutes,winspercentage=winspercentage)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("icehockey_players.csv","r")
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
games=[]
assists=[]
goals=[]
powerplaygoals=[]
shorthandgoals=[]
wininggoals=[]
overtimegoals=[]
points=[]
powerplaypoints=[]
shorthandpoints=[]
shots=[]
shotspercentage=[]
penaltyminutes=[]
winspercentage=[]





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
     height.append(row["Height in feet"])
     weight.append(row["Weight in lb"])
     games.append(row["Games"])
     assists.append(row["Assists"])
     goals.append(row["Goals"])
     powerplaygoals.append(row["Powerplay Goals"])
     shorthandgoals.append(row["Shorthand Goals"])
     wininggoals.append(row["Winning Goals"])
     overtimegoals.append(row["Overtime Goals"])
     points.append(row["Points"])
     powerplaypoints.append(row["Powerplay Points"])
     shorthandpoints.append(row["Shorthand Points"])
     shots.append(row["Shots"])
     shotspercentage.append(row["Shots Percentage"])
     penaltyminutes.append(row["Penalty Minutes"])
     winspercentage.append(row["Wins Percentage"])
     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],dob[i],nationality[i],team[i],position[i],debut[i],height[i],weight[i],
                  games[i],assists[i],goals[i],powerplaygoals[i],shorthandpoints[i],
                  wininggoals[i],overtimegoals[i],points[i],powerplaypoints[i],shorthandpoints[i],shots[i],shotspercentage[i],
                  penaltyminutes[i],winspercentage[i])
	                                                                                                     



















