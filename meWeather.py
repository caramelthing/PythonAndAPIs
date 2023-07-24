#!/usr/bin/env python3

#page  329 from automate the boring stuff
#prints the weather for a location  for the command line.

import json, requests, sys

#compute location from command line arguments

if len(sys.argv) <2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ''.join(sys.argv[1:])

#browse to and save free openweathermap.org api key
#download json data from openweathermap.org

url = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=68f0bd076f50fb15639fdb0230669d2b&q={a}&cnt=3' .format(a=location)
response = requests.get(url)
response.raise_for_status()

#Download and load JSON String Data and Print Weather

#load JSON data into a python varable.
weatherData = json.loads(response.text)

#print weather descriptions.
w = weatherData['list']
print('Current weather in {a}:'.format(a=location))
print(w[0]['weather'][0]['main'],'-', w[0]['weather'][0]['description'])
print()
print(w[1]['weather'][0]['main'],'-', w[1]['weather'][0]['description'])
print()
print(w[2]['weather'][0]['main'],'-', w[2]['weather'][0]['description'])