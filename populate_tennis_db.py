import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from tennis_app.models import tennis_db

def add_entry(name,age,dob,nationality,rank,debut,seasons,height,weight,
     preferedhand,titles,grandslams,tourfinals,masters,daviscups,totalpoints,tournamentpoints,rankingpoints,
     overallwins,hardwins,claywins,grasswins,carpetwins,games,aces,faults):     

	t=tennis_db.objects.get_or_create(name=name,age=age,dob=dob,nationality=nationality,rank=rank,
          debut=debut,seasons=seasons,height=height,weight=weight,
          preferedhand=preferedhand,titles=titles,grandslams=grandslams,tourfinals=tourfinals,
          masters=masters,daviscups=daviscups,totalpoints=totalpoints,tournamentpoints=tournamentpoints,
          rankingpoints=rankingpoints,overallwins=overallwins,hardwins=hardwins,
          claywins=claywins,grasswins=grasswins,carpetwins=carpetwins,games=games,
          aces=aces,faults=faults)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("tennis_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
dob=[]
nationality=[]
rank=[]
debut=[]
seasons=[]
height=[]
weight=[]
preferedhand=[]
titles=[]
grandslams=[]
tourfinals=[]
masters=[]
daviscups=[]
totalpoints=[]
tournamentpoints=[]
rankingpoints=[]
overallwins=[]
hardwins=[]
claywins=[]
grasswins=[]
carpetwins=[]
games=[]
aces=[]
faults=[]






#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     age.append(row["Age"])
     dob.append(row["Date of Birth"])
     nationality.append(row["Nationality"])
     rank.append(row["Rank"])
     debut.append(row["Debut"])
     seasons.append(row["Seasons"])
     height.append(row["Height in cm"])
     weight.append(row["Weight in kg"])
     preferedhand.append(row["Prefered Hand"])
     titles.append(row["Titles"])
     grandslams.append(row["Grand Slams"])
     tourfinals.append(row["Tour Finals"])
     masters.append(row["Masters"])
     daviscups.append(row["Davis Cups"])
     totalpoints.append(row["Total Points"])
     tournamentpoints.append(row["Tournament Points"])
     rankingpoints.append(row["Ranking Points"])
     overallwins.append(row["Win Overall (in %)"])
     hardwins.append(row["Win Hard (in %)"])
     claywins.append(row["Win Clay (in %)"])
     grasswins.append(row["Win Grass"])
     carpetwins.append(row["Win Carpet"])
     games.append(row["Games"])
     aces.append(row["Aces"])
     faults.append(row["Faults"])




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],dob[i],nationality[i],rank[i],debut[i],seasons[i],height[i],weight[i],
                  preferedhand[i],titles[i],grandslams[i],tourfinals[i],masters[i],daviscups[i],totalpoints[i],
                  tournamentpoints[i],rankingpoints[i],overallwins[i],hardwins[i],claywins[i],grasswins[i],
                  carpetwins[i],games[i],aces[i],faults[i])
	                                                                                                     



















