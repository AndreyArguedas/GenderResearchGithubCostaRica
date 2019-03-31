# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 20:19:09 2019

@author: Andrey
"""

import requests
from requests.auth import HTTPDigestAuth
import json
import pandas as pd

url = "https://api.github.com/search/users?q=location:Costa%20Rica&per_page=100&page="

usersUrl = []
API_calls = 0

userName = "AndreyArguedas" # Use here your user name
password = input("Password: ")

def generate_csv_from_array(data):
    dict_data = {'usersURL': data}
    data_frame = pd.DataFrame(dict_data)
    data_frame.to_csv('C:/Users/Andrey/Desktop/GenderResearchGithubCostaRica/data/CostaRicanUsers.csv', encoding='utf-8', header=True, index=False)
    print("Finished URL generation!")

# It is a good practice not to hardcode the credentials. So ask the user to enter credentials at runtime
for i in range(1, 4):
    newURL = url + str(i)
    
    myResponse = requests.get(newURL,auth=(userName , password), verify=True)

    if(myResponse.ok):

        jData = json.loads(myResponse.content)

        for item in jData["items"]:
            usersUrl.append(item["url"])
        API_calls += 1
        if(API_calls == 3):
            generate_csv_from_array(usersUrl) 

    else:
        # If response code is not ok (200), print the resulting http error code with description
        myResponse.raise_for_status()