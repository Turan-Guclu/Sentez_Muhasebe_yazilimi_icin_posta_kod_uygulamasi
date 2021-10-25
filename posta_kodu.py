# -*- coding: utf-8 -*-
import time
from requests.api import request
from requests.models import Response
from selenium import webdriver
from database_connection import city,district
driver_path = "C:\ProgramData\Anaconda3\driver\chromedriver.exe"

neighbourhood=[]
post_codes=[]
logs=[]
class post_code:
    def __init__(self,city,district):
        self.url="https://www.postakodu.com.tr/"
        self.browser = webdriver.Chrome(driver_path)
        self.city = city
        self.district = district
    
    def city_post_code(self):
        for i,m in zip(self.city,self.district):
            if (str(i)=="denizli" and str(m)=="merkez" or str(i)=="izmir" and str(m)=="merkez" 
             or str(i)=="manisa" and str(m)=="merkez" or str(i)=="bursa" and str(m)=="merkez" 
             or str(i)=="afyonkarahisar" or str(i)=="samsun" or str(i)=="ankara" or str(i)=="ordu" 
             or str(i)=="adana" and str(m)=="merkez" or str(i)=="trabzon" and str(m)=="ortahisar"):
                self.browser.get(self.url+i)
                print(self.url+i)
                pos_cod=self.browser.find_element_by_id("p_postakod").text
                print(f"{pos_cod},")
                logs.append(self.url+i)
                post_codes.append(f"{pos_cod}\n")      
            else:
                 self.browser.get(self.url+i+"/"+m)
                 print(self.url+i+"/"+m)
                 pos_cod=self.browser.find_element_by_id("p_postakod").text
                 print(f"{pos_cod},")
                 logs.append(self.url+i+"/"+m)
                 post_codes.append(f"{pos_cod}\n")  
        f=open("postakodlari.txt","w")
        for post in post_codes:
             f.write(post) 
        s=open("logs.txt","w")
        for log,post in zip(logs,post_codes):    
            s.write(log)
            s.write(post)      

post_code = post_code(city,district)
post_code.city_post_code()


