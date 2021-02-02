import requests
import json
from collections import Counter

class main():
    # call the filtered API
    # this takehome only deals with subway route transportation so filtering those out API side is a much quicker process
    # than loading all transportation routes into memory and then filtering
    url = 'https://api-v3.mbta.com/routes?filter[type]=1,2'
    response = requests.get(url)

    #if response was given and the status code is 200 then get and set the json
    if response and response.status_code == 200:
        json_data = json.dumps(response.json(), indent=4)
    else:
        None

    # Question 1
    # go through each entry to get the long_name
    def first_question(json_data):
        #load the data into a dict
        data_in_dict = json.loads(json_data)
        long_names = [row['attributes']['long_name'] for row in data_in_dict['data']]
        formatli = json.dumps(long_names, indent=4)
        return formatli

    q1 = first_question(json_data)
    #print(q1)

    # last step here is to create and write to a file rather than printing to console

    # Question 2
    # subway name with the most stops and number of stops
    # subway route with the least stops and number of stops
    # A list of the stops that connect two or more subway routes along with the relevant route
    # names for each of those stops.
    #try hash map
    def second_question(json_data):

       #load the data into a dict
       data = json.loads(json_data)
       routes={}

       for item in data['data']:
           key = item['attributes']['long_name']
           val_list = item['attributes']['direction_destinations']

           val=[]
           for v in val_list:
               val += v.split(' or ')
           routes[key]=val

           return routes

    q2 = second_question(json_data)
    print(q2)