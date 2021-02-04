import json
import requests
from collections import defaultdict

class main():
    # call the filtered API
    # this take home only deals with subway route transportation so filtering those out API side is a much quicker process
    # than loading all transportation routes into memory and then filtering
    routes_api = requests.get('https://api-v3.mbta.com/routes?filter[type]=0,1')
    data = routes_api.json()['data']

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
        all_stops=defaultdict(list)
        for route_entry in data:
            stop_api = requests.get('https://api-v3.mbta.com/stops?filter[route]=' + route_entry["id"])
            stops = stop_api.json()["data"]
            route_object={"route": route_entry["attributes"]["long_name"], "stops": [], "count": len(stops)}
            for s in stops:
                route_object["stops"] += [s["attributes"]["name"]]
            routes+=[route_object]
            #print(route_object)

        maxstops = max(routes, key=lambda x:x['count'])
        minstops = min(routes, key=lambda x:x['count'])
        print(json.dumps(maxstops))
        print(json.dumps(minstops))

        for route in routes:
            for stop in route['stops']:
                all_stops[stop] += [route['route']]
        print(json.dumps(all_stops))
        return routes

    print(first_question(data))
    second_question(data)
    #third_question(data, 'Ashmont', 'Arlington')