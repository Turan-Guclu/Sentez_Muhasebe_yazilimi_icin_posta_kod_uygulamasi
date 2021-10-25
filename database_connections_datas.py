import pyodbc
server = 1 # Sunucu İp Adresi
database = 1# VeriTabanı Adı
username =1 #Kullanıcı Adı
password=1 #Şifre
connections=pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)