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
        print(json.dumps(long_names))
        return

    q1 = first_question(data)

    # Question 2
    # subway name with the most stops and number of stops https://api-v3.mbta.com/stops
    # subway route with the least stops and number of stops https://api-v3.mbta.com/stops
    # A list of the stops that connect two or more subway routes along with the relevant route
    # names for each of those stops
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
        print(json.dumps(routes))
        return
    q2 = second_question(data)