import requests
import json
import inquirizer

class main():
    # call the filtered API
    # this takehome only deals with subway route transportation so filtering those out API side is a much quicker process
    # than loading all transportation routes into memory and then filtering
    subway_routes = 'https://api-v3.mbta.com/routes?filter[type]=1,2'
    response = requests.get(subway_routes)

    #if response was given and the status code is 200 then get and set the json
    if response and response.status_code == 200:
        json_data = json.dumps(response.json(), indent=4)
    else:
        None

    def get_direction_dest(json_data):
        #load the data into a dict
        data = json.loads(json_data)
        routes={}
        max_min = {}

        for item in data['data']:
            key = item['attributes']['long_name']
            val_list = item['attributes']['direction_destinations']

            val=[]
            # loop through the list of direction_destinations and remove the ors
            for v in val_list:
                val += v.split(' or ')
                # calculate the length of the stops routes[key]=val returns line name and stops. print(len(stops))
                count_stops = len(val)
                routes[key] = count_stops

        maximum = max(routes, key=routes.get)  # Just use 'min' instead of 'max' for minimum.
        minimum = min(routes, key=routes.get)  # Just use 'min' instead of 'max' for minimum.
        print(maximum, routes[maximum])
        print(minimum, routes[minimum])

        return

    q2 = get_direction_dest(json_data)


# List a rail route you could travel to get from one stop to the other.
# Davis to Kendall -> Redline
# Ashmont to Arlington -> Redline, Greenline
def third_question(second_question, data):
    start = [
        inquirer.List('long_name',
                      message="What is your starting station?",
                      choices=["Red Line",
                               "Orange Line",
                               "Blue Line",
                               "Fairmount Line",
                               "Fitchburg Line",
                               "Framingham/Worcester Line",
                               "Franklin Line",
                               "Greenbush Line",
                               "Haverhill Line",
                               "Kingston/Plymouth Line",
                               "Lowell Line",
                               "Middleborough/Lakeville Line",
                               "Needham Line",
                               "Newburyport/Rockport Line",
                               "Providence/Stoughton Line",
                               "Foxboro Event Service"],
                      ),
    ]
    end = [
        inquirer.List('long_name',
                      message="What is your ending station?",
                      choices=["Red Line",
                               "Orange Line",
                               "Blue Line",
                               "Fairmount Line",
                               "Fitchburg Line",
                               "Framingham/Worcester Line",
                               "Franklin Line",
                               "Greenbush Line",
                               "Haverhill Line",
                               "Kingston/Plymouth Line",
                               "Lowell Line",
                               "Middleborough/Lakeville Line",
                               "Needham Line",
                               "Newburyport/Rockport Line",
                               "Providence/Stoughton Line",
                               "Foxboro Event Service"],
                      ),
    ]
    start = inquirer.prompt(start)
    end = inquirer.prompt(end)
    # now I have start and target station, and all I need now is to pull the stops for all stations
    # and cross those against my starting and ending stations to figure out how to get from point A to B
    stops = second_question(data) # can use second method for this
    connected_paths = []
    known_path=[]
    for stops in connected_paths:
        # check if the current subway can take us directly to target
        if end in stops["stops"]:
            known_path += already_path + [stops]
            continue
        #now check other stops to see if they can take us to the target
        for end in stops["stops"]:
            if end == start: # no need to check out current stop
                continue
            else:
                # let check the this stop for connections
                known_path += find_next_route(stops, target, aready_path + [stops])
    return known_path
    print (len(route))


