import os 
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","music_site.settings")
django.setup()

from music_app.models import music_db

def add_entry(title,artist,album,writer,othername,isni,ipi,isrc,sesac_id,sesac_pub,
	ascap_id,ascap_pub,ascap_ipi,bmi_id,bmi_pub,gmr_id,gmr_pub,gmr_ipi,country,year):
	t=music_db.objects.get_or_create(title=title,artist=artist,album=album,writer=writer,othername=othername,isni=isni,ipi=ipi,
		isrc=isrc,sesac_id=sesac_id,sesac_pub=sesac_pub,ascap_id=ascap_id,ascap_pub=ascap_pub,ascap_ipi=ascap_ipi,
		bmi_id=bmi_id,bmi_pub=bmi_pub,gmr_id=gmr_id,gmr_pub=gmr_pub,gmr_ipi=gmr_ipi,country=country,year=year)[0]
	t.save()
    

#add imports
import csv

#open csv file
csvfile=open("music_titles.csv","r")
reader=csv.DictReader(csvfile)
title=[]
artist=[]
album=[]
writer=[]
othername=[]
isni=[]
ipi=[]
isrc=[]
sesac_id=[]
sesac_pub=[]
ascap_id=[]
ascap_pub=[]
ascap_ipi=[]
bmi_id=[]
bmi_pub=[]
gmr_id=[]
gmr_pub=[]
gmr_ipi=[]
country=[]
year=[]


#read values from the csv file
for row in reader:
	#print(row["Track Title"])
     title.append(row["Track Title"])
     artist.append(row["Artist Name"])
     album.append(row["Album"])
     writer.append(row["Writer"])
     othername.append(row["Othername"])
     isni.append(row["ISNI code"])
     ipi.append(row["IPI code"])
     isrc.append(row["ISRC"])
     sesac_id.append(row["SESAC Work ID"])
     sesac_pub.append(row["SESAC Publisher"])
     ascap_id.append(row["ASCAP Work ID"])
     ascap_pub.append(row["ASCAP Publisher"])
     ascap_ipi.append(row["ASCAP Publishers' IPI"])
     bmi_id.append(row["BMI Work ID"])
     bmi_pub.append(row["BMI Publisher"])
     gmr_id.append(row["GMR Work ID"])
     gmr_pub.append(row["GMR Publisher"])
     gmr_ipi.append(row["GMR Publishers' IPI"])
     country.append(row["Country"])
     year.append(row["Year"])


#inserting values into the Table
for i in range(0,len(title)):
	add_entry(title[i],artist[i],album[i],writer[i],othername[i],isni[i],ipi[i],isrc[i],sesac_id[i],sesac_pub[i],
		ascap_id[i],ascap_pub[i],ascap_ipi[i],bmi_id[i],bmi_pub[i],gmr_id[i],gmr_pub[i],gmr_ipi[i],country[i],year[i])
	





















