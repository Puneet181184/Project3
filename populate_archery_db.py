import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from archery_app.models import archery_db

def add_entry(name,age,dob,country,debut,gender,rank,arrowlength,
     drawweight,averagearrow,worldcupgold,worldcupsilver,worldcupbronze):     

	t=archery_db.objects.get_or_create(name=name,age=age,dob=dob,country=country,debut=debut,
          gender=gender,rank=rank,arrowlength=arrowlength,drawweight=drawweight,averagearrow=averagearrow,
          worldcupgold=worldcupgold,worldcupsilver=worldcupsilver,
          worldcupbronze=worldcupbronze)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("archery_players.csv","r")
reader=csv.DictReader(csvfile)
name=[]
age=[]
dob=[]
country=[]
debut=[]
gender=[]
rank=[]
arrowlength=[]
drawweight=[]
averagearrow=[]
worldcupgold=[]
worldcupsilver=[]
worldcupbronze=[]







#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     name.append(row["Name"])
     age.append(row["Age"])
     dob.append(row["Date of Birth"])
     country.append(row["Country"])
     debut.append(row["Debut"])
     gender.append(row["Gender"])
     rank.append(row["Rank"])
     arrowlength.append(row["Arrow Length in cm"])
     drawweight.append(row["Draw Weight in kg"])
     averagearrow.append(row["Average Arrow"])
     worldcupgold.append(row["World Cup Gold"])
     worldcupsilver.append(row["World Cup Silver"])
     worldcupbronze.append(row["World Cup Bronze"])


     

     




#inserting values into the Table
for i in range(0,len(name)):
	add_entry(name[i],age[i],dob[i],country[i],debut[i],gender[i],rank[i],arrowlength[i],
                  drawweight[i],averagearrow[i],worldcupgold[i],worldcupsilver[i],worldcupbronze[i])
	                                                                                                     



















