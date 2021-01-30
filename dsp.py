import requests
import json

class main():
    #call the API
    url = 'https://api-v3.mbta.com/routes?filter[type]=1,2'
    response = requests.get(url)

    #if response was given and the status code is 200 then get and set the json
    if response and response.status_code == 200:
        json_data = json.dumps(response.json(), indent=4)
    else:
        None

    # print(json_data)
    #load the data into a dict

    data_in_dict = json.loads(json_data)

    #go through each entry to get the long_name
    mylist= [row['attributes']['long_name'] for row in data_in_dict['data']]
    print(mylist)