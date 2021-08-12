# -*- coding: utf-8 -*-
"""
Created on Mon May 25 13:10:08 2020

@author: DParis
"""

#packages to perform the request, handle JSON objects, and encode URLs
import requests
import json
import urllib

def getdatabycode(data,codes,code):
    for i in range(len(codes)):
        if codes[i] == code:
            return data[i]
        else:
            return "Nombre no encontrado"

session = requests.Session()
#%% Parametros API

#API KEY as defined in the settings tab, so that the script has full access to the data
API_KEY = 'XXXXX'
#base endpoint, see https://bubble.io/reference#API.get_api.Endpoint
base_url = 'https://subnormalmx.com/api/1.1/obj/'
base_datos = "User"

#%% Get Data 


#Query initial parameters. We do not send a limit parameter (default is 100)
cursor = 0
remaining = 10000

#we keep making calls till we have no remaining items to fetch
while remaining > 0:
    #data we send with the search. Search constraints would be here
    params = {'api_token': API_KEY,'cursor': cursor }
    url = base_url + base_datos + '?' + urllib.parse.urlencode(params)
    response = session.get(url,verify = False)

    if response.status_code != 200:
        print('Error with status code {}'.format(response.status_code))
        exit()

    chunk = response.json()['response']
    remaining = chunk['remaining']
    count = chunk['count']
    results = chunk['results']

    #we print each object
    for result in results:
        print(json.dumps(result, indent=4, sort_keys=True))

    cursor += count

codigos = [results[i]["UID"] for i in range(len(results))]   
Instagrams = [results[i]["Instagram"] for i in range(len(results))]

#%% Leer Codigo

codigo = "cus_H3XzsSg2dD6cMw"

#%% Accion
if codigo in codigos:
    
    print("pasa " + getdatabycode(Instagrams, codigos, codigo))
    
    base_datos = "Entradas"
    params = {'api_token': API_KEY}
    url = base_url + base_datos + '?' + urllib.parse.urlencode(params)
    data = {"Instagram":getdatabycode(Instagrams, codigos, codigo),"UID":codigo}
    r = requests.post(url,data=data,verify = False)
    
else:
    print("no pasa")