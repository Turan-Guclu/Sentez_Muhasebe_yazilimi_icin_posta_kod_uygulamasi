
from database_connections_datas import connections
tr_karakterler = ["ş","ç","ö","ğ","ü","ı","Ş","Ç","Ö","Ğ","Ü","İ",'İ']
eng_karakterler = ["s","c","o","g","u","i","S","C","O","G","U","I",'i']

cursor = connections.cursor()
cursor.execute("""
select CityName,DistrictName from Erp_Address as addr
inner join dbo.Meta_City as city
on addr.CityId=city.RecId 
inner join dbo.Meta_District as dsct 
on addr.DistrictId=dsct.RecId
""") 
tr_city=[]
tr_district=[]
city=[]
district=[]
row = cursor.fetchone() 
while row: 
    tr_city.append(str(row[0].strip()))
    tr_district.append(row[1])
    row = cursor.fetchone()
for  t in tr_city:
    for i in range(13):
        t=t.replace(tr_karakterler[i],eng_karakterler[i])
    city.append(str(t).lower())

for  c in tr_district:
    for i in range(13):
        c=c.replace(tr_karakterler[i],eng_karakterler[i])
    district.append(str(c).lower())
