import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from diving_app.models import diving_db

def add_entry(name,dob,country,gender,discipline):     

	t=diving_db.objects.get_or_create(name=name,dob=dob,country=country,
          gender=gender,discipline=discipline)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("diving_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
dob=[]
country=[]
gender=[]
discipline=[]







#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     dob.append(row["Date of Birth"])
     country.append(row["Country"])
     gender.append(row["Gender"])
     discipline.append(row["Discipline"])


     

     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],dob[i],country[i],gender[i],
                  discipline[i])
	                                                                                                     



















