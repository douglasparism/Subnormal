# -*- coding: utf-8 -*-
"""
Created on Wed May 27 13:08:19 2020

@author: DParis
"""

import requests
import json
import urllib

session = requests.Session()

#API KEY as defined in the settings tab, so that the script has full access to the data
API_KEY = 'xxxx'
#base endpoint, see https://bubble.io/reference#API.get_api.Endpoint
base_url = 'https://subnormalmx.com/version-test/api/1.1/obj/'
base_datos = "Entradas"

params = {'api_token': API_KEY}
url = base_url + base_datos + '?' + urllib.parse.urlencode(params)

data = {"Instagram":"MrSUBMX","UID":"Hector es prueba"}
r = requests.post(url,data=data,verify = False)

print(r.content)