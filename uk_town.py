import csv
import pprint
from collections import defaultdict , Counter

pp = pprint.PrettyPrinter(indent=4)

""" This function opens the csv file in the read mode.
    Input -  is the csv file.
    Output - the list of dicitonaries 
"""
def towns_file():
    with open("uk-towns-sample.csv", "r") as file:
        towns_reader = csv.DictReader(file)
        list_of_dict = list(towns_reader)
        for town in list_of_dict:
            town["easting"] = int(town["easting"])
            town["northing"] = int(town["northing"])
            town["latitude"] = float(town["latitude"])
            town["longitude"] = float(town["longitude"])
            town["elevation"] = int(town["elevation"])
    return list_of_dict
   

""" This function is finding the duplictates names.
    Input - list of dictionaries.  
    Output - list of dulpicates names 
"""
def duplicates_name(list_of_dict):
    list_of_towns = []
    output_dict = {}
    for town_dict in list_of_dict:
        list_of_towns.append(town_dict["name"])
    counter_of_town = Counter(list_of_towns)
    for key, value in counter_of_town.items():
        if value > 1:
            output_dict[key] = value
    return output_dict
 
   
""" This function is filtering all the towns where (Meads) exist.
    Input - list of dictionaries 
    Output - The list of names where Meads exist
"""
def meads_in_name(list_of_dict):
    list_of_town_with_meads = []
    for town in list_of_dict:
        if "Meads" in town["name"]:
            list_of_town_with_meads.append(town["name"])
    return list_of_town_with_meads       

""" This function is finding all towns in between two latitude and longitude.
    Input - Two lists of dictionaries.
    Output - list of towns that are inside the the the given latitude and longitude. 
"""
def cities_between_long_lat(coordinates, list_of_dict):
    list_of_towns = []
    for town in list_of_dict:
         if  coordinates[0]["lat"] < town["latitude"]:
             if coordinates[1]["lat"] < town["latitude"]:
                 if coordinates[0]["long"] <  town["longitude"]: 
                    if coordinates[1]["long"] < town["longitude"]: 
                       list_of_towns.append(town["name"])                              
    return list_of_towns


""" This function is finding all towns that are above elevation of 100.
    Input -  list of dictionaries and an benchmark number for elevation.
    Output - list of towns above 100
"""
def towns_above_elevetion_of_100(list_of_dict, elevations):
    list_of_towns = []
    for town in list_of_dict:
        if town["elevation"] > elevations[0]["max"]:
            list_of_towns.append(town["name"])
    return list_of_towns


""" This function is filtering names of all the villages.
    Input - list of dictionaries.
    Output - list of names whose town type is village
"""
def all_villages(list_of_dict, town_types):
    list_of_vilages = []
    for vilage in list_of_dict:
        list_of_vilages =  [vilage for vilage in list_of_dict if vilage['town_type']==town_types["town_ham"]]
        list_of_vilages.append(vilage["town_type"])
    return list_of_vilages


""" This is the main function where the program starts executing .
    The function defined above gets executed after this main funtcion runs.
"""
if __name__ == '__main__':
   
#   This list of dictionaries which used to find the towns within the coordinates 
    coordinates = [{                                  
                     "lat": 53.30935,
                     "long": -1.5331
                    },
                   {
                     "lat": 53.21941,
                     "long": -1.30514
                   }]
# Below is the list of dictinary set as the benchmark for elevation
    elevations = [{
                    "max" : 100,
                    "min" : 20
                }]
# Below is the is the dictionary of types of town
    town_types = {  
                   "town_vil": "Village",
                   "town_sub": "Suburban Area",
                   "town_ham":  "Hamlet",
                   "town_loc": "Locality",
                   "town_town":  "Town",
                   "town_cit": "City"

                   }


    pp.pprint(towns_file())                        
    pp.pprint(cities_between_long_lat(coordinates, towns_file()))
    pp.pprint(meads_in_name(towns_file()))
    pp.pprint(duplicates_name(towns_file()))
    pp.pprint(all_villages(towns_file(), town_types))
    pp.pprint(towns_above_elevetion_of_100(towns_file(), elevations))
    pp.pprint(towns_above_elevetion_of_100(towns_file(), elevations))
    pp.pprint(all_villages(towns_file()))
    pp.pprint(towns_above_elevetion_of_100(towns_file(), elevations))
    pp.pprint(towns_above_elevetion_of_100(towns_file(), elevations))