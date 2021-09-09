import json

states_and_cities = json.loads(open('states_and_cities.json').read())
print(list(states_and_cities.keys()))
city = states_and_cities['Andhra Pradesh']
print(city)