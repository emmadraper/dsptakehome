import json
import requests

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
        #print(json.dumps(maxstops))
        #print(json.dumps(minstops))
        return routes
        # C) A list of the stops that connect two or more subway routes along with the relevant route and the names for each of those stops

    # Extend your program again such that the user can provide any two stops on the subway routes
    # List a rail route you could travel to get from one stop to the other.
    # Davis to Kendall -> Redline
    # Ashmont to Arlington -> Redline, Greenline
    def third_question(data):
        A = input("What is the first stop? ")
        B = input("What is the second stop? ")
        # now I have start and target station, and all I need now is to pull the stops for all stations
        # and cross those against my starting and ending stations to figure out how to get from point A to B
        stops = second_question(data) # can use second method for this
        def find_next_route(A, B, already_path=[]):
            connected_paths = [] # need an array to store the connected paths
            direct=[] # need an array to track if A and B are direct

        print(find_next_route(A, B))

    #print(first_question(data))
    #second_question(data)
    third_question(data)
