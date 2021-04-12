import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from basketball_app.models import basketball_db

def add_entry(name,age,dob,nationality,college,position,height,weight,
     preferedhand,games,gamestarted,minutes,goals,attempts,assists,steals,
     points,threepoints,twopoints,blocks,freethrows,rebounds,fouls):     

	t=chess_db.objects.get_or_create(name=name,age=age,dob=dob,nationality=nationality,college=college,
          position=position,height=height,weight=weight,
          preferedhand=preferedhand,games=games,gamestarted=gamestarted,
          minutes=minutes,goals=goals,attempts=attempts,assists=assists,
          steals=steals,points=points,threepoints=threepoints,
          twopoints=twopoints,blocks=blocks,freethrows=freethrows,rebounds=rebounds,fouls=fouls)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("basketball_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
dob=[]
nationality=[]
college=[]
position=[]
height=[]
weight=[]
preferedhand=[]
games=[]
gamestarted=[]
minutes=[]
goals=[]
attempts=[]
assists=[]
steals=[]
points=[]
threepoints=[]
twopoints=[]
blocks=[]
freethrows=[]
rebounds=[]
fouls=[]






#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     age.append(row["Age"])
     dob.append(row["Date of Birth"])
     nationality.append(row["Nationality"])
     college.append(row["College"])
     position.append(row["position"])
     height.append(row["Height in cm"])
     weight.append(row["Weight in kg"])
     preferedhand.append(row["Prefered Hand"])
     games.append(row["Games"])
     gamestarted.append(row["Games Started"])
     minutes.append(row["Minutes"])
     goals.append(row["Goals"])
     attempts.append(row["Attempts"])
     assists.append(row["Assists"])
     steals.append(row["Steals"])
     points.append(row["Points"])
     threepoints.append(row["Three Points"])
     twopoints.append(row["Two Points"])
     blocks.append(row["Blocks"])
     freethrows.append(row["Free Throws"])
     rebounds.append(row["Rebounds"])
     fouls.append(row["Fouls"])




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],dob[i],nationality[i],rank[i],debut[i],height[i],weight[i],
                  title[i],playerid[i],gender[i],stdrating[i],rapidrating[i],blitzrating[i],
                  games[i],wins[i],draws[i],losses[i],score[i])
	                                                                                                     



















