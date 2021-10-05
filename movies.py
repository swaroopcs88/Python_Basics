#!/usr/bin/env python3
import requests
import csv
response = requests.get("http://www.omdbapi.com/?i=tt3896198&apikey=dfb95ec1")
#print(response.json())
data = response.json()
title= data['Title']
header = ['Title', 'Source', 'Value']

with open('movies.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)

    for item in data['Ratings']:
        list = []
        list.append(title)
        list.append(item['Source'])
        list.append(item['Value'])
        writer.writerow(list)
