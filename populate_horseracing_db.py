import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from horseracing_app.models import horseracing_db

def add_entry(name,age,rank,horse,starts,gold,
     silver,bronze):     

	t=horseracing_db.objects.get_or_create(name=name,age=age,
          rank=rank,horse=horse,
          starts=starts,gold=gold,silver=silver,bronze=bronze)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("horseracing_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
rank=[]
horse=[]
starts=[]
gold=[]
silver=[]
bronze=[]








#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     age.append(row["Age"])
     rank.append(row["Rank"])
     horse.append(row["Horse"])
     starts.append(row["Starts"])
     gold.append(row["Gold"])
     silver.append(row["Silver"])
     bronze.append(row["Bronze"])

     

     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],rank[i],horse[i],starts[i],
                  gold[i],silver[i],bronze[i])
	                                                                                                     



















