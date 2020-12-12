import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from cricket_app.models import cricket_db

def add_entry(name,age,country,debut,skill,odimatches,odiruns,odiwickets,odicatches,
     testmatches,testruns,testwickets,testcatches,t20matches,t20runs,t20wickets,t20catches):
	t=cricket_db.objects.get_or_create(name=name,age=age,country=country,debut=debut,skill=skill,
          odimatches=odimatches,odiruns=odiruns,odiwickets=odiwickets,odicatches=odicatches,
          testmatches=testmatches,testruns=testruns,testwickets=testwickets,testcatches=testcatches,
          t20matches=t20matches,t20runs=t20runs,t20wickets=t20wickets,t20catches=t20catches)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("cricket_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
country=[]
debut=[]
skill=[]
odimatches=[]
odiruns=[]
odiwickets=[]
odicatches=[]
testmatches=[]
testruns=[]
testwickets=[]
testcatches=[]
t20matches=[]
t20runs=[]
t20wickets=[]
t20catches=[]




#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     age.append(row["Age"])
     country.append(row["Country"])
     debut.append(row["Debut"])
     skill.append(row["Skill"])
     odimatches.append(row["ODI Matches"])
     odiruns.append(row["ODI Runs"])
     odiwickets.append(row["ODI Wickets"])
     odicatches.append(row["ODI Catches"])
     testmatches.append(row["Test Matches"])
     testruns.append(row["Test Runs"])
     testwickets.append(row["Test Wickets"])
     testcatches.append(row["Test Catches"])
     t20matches.append(row["T20 Matches"])
     t20runs.append(row["T20 Runs"])
     t20wickets.append(row["T20 Wickets"])
     t20catches.append(row["T20 Catches"])




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],country[i],debut[i],skill[i],odimatches[i],odiruns[i],odiwickets[i],odicatches[i],
                  testmatches[i],testruns[i],testwickets[i],testcatches[i],t20matches[i],t20runs[i],t20wickets[i],
                  t20catches[i])
	





















