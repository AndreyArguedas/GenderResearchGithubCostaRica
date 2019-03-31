# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 22:11:51 2019

@author: Andrey
"""

import requests
import json
import pandas as pd
import os

def generate_csv_from_dict(data):
    data_frame = pd.DataFrame(data)
    data_frame.columns = ["id", "login", "html_url", "name", "email"]
    data_frame.to_csv('C:/Users/Andrey/Desktop/GenderResearchGithubCostaRica/data/CostaRicanUsersInfo.csv', encoding='utf-8', header=True, index=False)
    print("Finished URL generation!")

os.chdir("/Users/Andrey/Desktop/GenderResearchGithubCostaRica/data")
datos_est = pd.read_csv('CostaRicanUsers.csv')
users = datos_est.loc[:,'usersURL']


userName = "AndreyArguedas" # Use here your user name
password = input("Password: ")


API_calls = 0
data = []
for user in users:
    
    myResponse = requests.get(user ,auth=(userName , password), verify=True)

    if(myResponse.ok):
        userData = json.loads(myResponse.content)
        data.append([userData["id"], userData['login'], userData['html_url'], userData['name'], userData['email']])
        API_calls += 1
        print(API_calls)
        if(API_calls == len(users)):
            generate_csv_from_dict(data)
    else:
        # If response code is not ok (200), print the resulting http error code with description
        myResponse.raise_for_status()
