# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 15:54:04 2019

@author: Andrey
"""

import requests
from requests.auth import HTTPDigestAuth
import json
import pandas as pd
import os

urlForUserGender = "https://gender-api.com/get?name=" # In name we put the user name
country = "&country=CR"
keyInfo = "&key=xXpsAhbmCofwvvjQTu"

os.chdir("/Users/Andrey/Desktop/GenderResearchGithubCostaRica/data")
datos_est = pd.read_csv('CostaRicanUsersInfo.csv')


def generate_csv(data):
    data.to_csv('C:/Users/Andrey/Desktop/GenderResearchGithubCostaRica/data/CostaRicanUsersGender.csv', encoding='utf-8', header=True, index=False)
    print("Finished Gender generation!")
    
def fillMissedData(array, limit):
    for i in range(len(array), limit):
        array.append("UNDEFINED")

# Generando los first_names
    
first_names =  []

for name in datos_est.loc[:,'name']:
    if isinstance(name, str):
        first_name = name.split()[0]
        first_names.append(first_name)
    else:
        first_names.append("UNDEFINED")
    
datos_est["first_name"] = first_names

# Teniendo los firstanmes debemos proceder a obtener la data

genders = [] #Retrieve the genders
accuracy = [] #Retrieve accuracy
API_CALLS = 0

for i in range (499, 1000):
    newURL = urlForUserGender + datos_est.loc[i ,'first_name'] + country + keyInfo
    print(newURL)
    
    myResponse = requests.get(newURL)

    if(myResponse.ok):
        jData = json.loads(myResponse.content)
        API_CALLS += 1
        print(API_CALLS)
        genders.append(jData["gender"])
        accuracy.append(jData["accuracy"])

    else:
        # If response code is not ok (200), print the resulting http error code with description
        myResponse.raise_for_status()

print("Termine de obtener data")

fillMissedData(genders, len(first_names))
fillMissedData(accuracy, len(first_names))

print(genders)
print(accuracy)

datos_est["gender"] = genders
datos_est["accuracy"] = accuracy

generate_csv(datos_est)