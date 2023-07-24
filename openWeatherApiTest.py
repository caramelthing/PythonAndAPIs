'''#!/usr/bin/env python3
import requests
url = 'http://api.openweathermap.org/data/2.5/forecast/?id=524901&appid=68f0bd076f50fb15639fdb0230669d2b&q=s%'
response = requests.get(url)
print(response)

this now works
went off the documentation from openweather and used formatting {}' .format(predefined variable)- to make it work
'''

import requests

url = 'http://api.openweathermap.org/data/2.5/forecast?/daily/?q=BrightonUK&cnt=3&appid=68f0bd076f50fb15639fdb0230669d2b&q'
response = requests.get(url)
print(response)