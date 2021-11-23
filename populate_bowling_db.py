import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from bowling_app.models import bowling_db

def add_entry(name,age,country,gender,debut,city,state,
     bowls,events,championships,matches,cashes,titles,average):     

	t=bowling_db.objects.get_or_create(name=name,age=age,country=country,gender=gender,
          debut=debut,city=city,state=state,bowls=bowls,events=events,championships=championships,
          matches=matches,cashes=cashes,
          titles=titles,average=average)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("bowling_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
country=[]
gender=[]
debut=[]
city=[]
state=[]
bowls=[]
events=[]
championships=[]
matches=[]
cashes=[]
titles=[]
average=[]








#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     age.append(row["Age"])
     country.append(row["Country"])
     gender.append(row["Gender"])
     country.append(row["Country"])
     debut.append(row["Debut"])
     city.append(row["City"])
     state.append(row["State"])
     bowls.append(row["Bowls"])
     events.append(row["Events"])
     championships.append(row["Championships"])
     matches.append(row["Matches"])
     cashes.append(row["Cashes"])
     titles.append(row["Titles"])
     average.append(row["Average"])

     

     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],country[i],gender[i],debut[i],city[i],state[i],
                  bowls[i],events[i],championships[i],matches[i],cashes[i],
                  titles[i],average[i])
	                                                                                                     



















