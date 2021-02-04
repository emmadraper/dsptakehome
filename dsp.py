import json
import requests
import inquirer

class main():
    # call the filtered API
    # this take home only deals with subway route transportation so filtering those out API side is a much quicker process
    # than loading all transportation routes into memory and then filtering
    routes = requests.get('https://api-v3.mbta.com/routes?filter[type]=1,2')
    data = routes.json()['data']

    # Question 1
    # go through each entry to get the long_name
    def first_question(data):
        long_names = []
        for row in data:
            long_names += [row['attributes']['long_name']]
        long_names = json.dumps(long_names)
        return long_names

    # Question 2
    # A) subway name with the most stops and number of stops https://api-v3.mbta.com/stops
    # B) subway route with the least stops and number of stops https://api-v3.mbta.com/stops
    def second_question(data):
        routes= []
        for route_entry in data:
        	stops = requests.get('https://api-v3.mbta.com/stops?filter[route]=' + route_entry["id"])
        	stops = stops.json()["data"]
        	route_object={
        	  "route": route_entry["attributes"]["long_name"],
        	  "stops": [],
        	  "count": len(stops)
        	}
                for s in stops:
                    route_object["stops"] += [s["attributes"]["name"]]
                routes+=[route_object]
        maxstops = max(routes, key=lambda x:x['count'])
        minstops = min(routes, key=lambda x:x['count'])
        print(json.dumps(maxstops))
        print(json.dumps(minstops))

        return routes

        # C) A list of the stops that connect two or more subway routes along with the relevant route and the names for each of those stops

    # Extend your program again such that the user can provide any two stops on the subway routes

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
        start = inquirer.prompt(start)
        #print start["long_name"]
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
        end = inquirer.prompt(end)
        #print end["long_name"]
        # now I have start and ending stations, and all I need now is to pull the stops for those two stations
        print(second_question(start))
        print(second_question(end))


    print(first_question(data))
    second_question(data)
    #third_question(second_question, data)
