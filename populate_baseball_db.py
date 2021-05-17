import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from baseball_app.models import baseball_db

def add_entry(name,age,dob,nationality,college,team,position,debut,height,weight,
     games,appearances,atbats,runs,hits,doubles,triples,
     homeruns,runsbatted,steals,walks,strikeouts,stolenbases,caughtstealing,totalbases):     

	t=baseball_db.objects.get_or_create(name=name,age=age,dob=dob,nationality=nationality,college=college,
          team=team,position=position,height=height,weight=weight,debut=debut,
          games=games,appearances=appearances,
          atbats=atbats,runs=runs,hits=hits,doubles=doubles,
          triples=triples,homeruns=homeruns,runsbatted=runsbatted,
          steals=steals,walks=walks,strikeouts=strikeouts,stolenbases=stolenbases,caughtstealing=caughtstealing,totalbases=totalbases)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("baseball_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
dob=[]
nationality=[]
college=[]
team=[]
position=[]
height=[]
weight=[]
debut=[]
games=[]
appearances=[]
atbats=[]
runs=[]
hits=[]
doubles=[]
triples=[]
homeruns=[]
runsbatted=[]
steals=[]
walks=[]
strikeouts=[]
stolenbases=[]
caughtstealing=[]
totalbases=[]





#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     age.append(row["Age"])
     dob.append(row["Date of Birth"])
     nationality.append(row["Nationality"])
     college.append(row["College"])
     team.append(row["Team"])
     position.append(row["Position"])
     debut.append(row["Debut"])
     height.append(row["Height in cm"])
     weight.append(row["Weight in kg"])
     games.append(row["Games"])
     appearances.append(row["Appearances"])
     atbats.append(row["At bats"])
     runs.append(row["Runs"])
     hits.append(row["Hits"])
     doubles.append(row["doubles"])
     triples.append(row["Triples"])
     homeruns.append(row["Home Runs"])
     runsbatted.append(row["Runs Batted"])
     steals.append(row["Steals"])
     walks.append(row["Walks"])
     strikeouts.append(row["Strikeouts"])
     stolenbases.append(row["Stolen Bases"])
     caughtstealing.append(row["Caught Stealing"])
     totalbases.append(row["Total Bases"])




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],dob[i],nationality[i],college[i],position[i],height[i],weight[i],
                  preferedhand[i],games[i],gamestarted[i],minutes[i],goals[i],attempts[i],
                  assists[i],steals[i],points[i],threepoints[i],twopoints[i],blocks[i],freethrows[i],rebounds[i],fouls[i])
	                                                                                                     



















