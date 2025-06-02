import requests
from bs4 import BeautifulSoup
import os
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time
gecko_path = r"C:\Users\othma\Downloads\geckodriver-v0.30.0-win64\geckodriver.exe"
ss=Service(gecko_path)
options = Options()
options.headless = True
driver = webdriver.Firefox(service=ss,options=options)
driver.get("https://booknode.com/serie/les-royaumes-oublies-la-legende-de-drizzt")
time.sleep(5)
divs = driver.find_element(By.XPATH,"/html/body/main/section/section[2]/div[7]/div/div/main/section[1]/div/article")

cl = []
for div in divs.find_elements(By.TAG_NAME,"div"):
    if div.get_attribute("class") == "book col-xs-12 col-xs1-12 col-sm-12":
        link = div.find_element(By.TAG_NAME,"a").get_attribute("href")
        nom = div.find_elements(By.TAG_NAME,"h4")[0].text
        for i in div.find_elements(By.TAG_NAME,"a"):
            if i.find_elements(By.TAG_NAME,"img") != []:
                print(len(i.find_elements(By.TAG_NAME,"img")), i.find_elements(By.TAG_NAME,"img")[0].get_attribute("data-src"))
        img = div.find_element(By.TAG_NAME,"a").find_element(By.TAG_NAME,"img").get_attribute("data-src")
        resume = div.find_element(By.TAG_NAME,"span").text
        res = f"<div><img src='{img}'/><p>{resume}</p><a href='{link}'>{nom}</a></div>"
        cl.append(res)
        
        

header ="""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="fr" xml:lang="fr">
  <head>
    <meta charset="UTF-8" />
    <title>Les Royaumes Oubliés - La Légende de Drizzt</title>
    <link rel="stylesheet" type="text/css" href="styles.css" />
  </head>
  <body>"""
join = '\n'.join(cl)
final = f"<liste>{join}</liste>"
footer = "</body></html>"
final = header + final + footer

# with open("C:/Users/othma/othmanoff.github.io/exercice2.xml",encoding="utf-8",mode="w") as f:
#     f.write(final)
driver.quit()

with open("C:/Users/othma/othmanoff.github.io/exercice2.xhtml",encoding="utf-8",mode="w") as f:
    f.write(final)