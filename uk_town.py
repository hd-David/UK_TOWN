import csv
import pprint
from collections import defaultdict , Counter

pp = pprint.PrettyPrinter(indent=4)

""" This function opens the vsc file in the read mode and 
    returning the list of dcitonaries as the output """
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
   

""" This function is finding the duplictates of names of towns. 
Taking the list of dictionaries as an input and returing 
 a list of dulpicates towns as output"""
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
Giving the list of towns where Meads exist"""
def meads_in_name(list_of_dict):
    list_of_town_with_meads = []
    for town in list_of_dict:
        if "Meads" in town["name"]:
            list_of_town_with_meads.append(town["name"])
    return list_of_town_with_meads       

""" This function is finding all towns in between two latitude and longitude.
   having two lists of dictionaries as input and and returning a list as an output. """
def cities_between_long_lat(coordinates, list_of_dict):
    list_of_towns = []
    for town in list_of_dict:
         if  coordinates[0]["lat"] < town["latitude"]:
             if coordinates[1]["lat"] < town["latitude"]:
                 if coordinates[0]["long"] <  town["longitude"]: 
                    if coordinates[1]["long"] < town["longitude"]: 
                       list_of_towns.append(town["name"])                              
    return list_of_towns


""" This function is getting all towns that are above elevation of 100.
   Recieving list of dictionary as an input and return a list of towns above 100"""
def towns_above_elevetion_of_100(list_of_dict, elevations):
    list_of_towns = []
    for town in list_of_dict:
        if town["elevation"] > elevations[0]["max"]:
            list_of_towns.append(town["name"])
    return list_of_towns


""" This function is filtering all towns that are found in the village.
    Its receiving list of dictionaries as input and returning a list of dictionaries.
    """
def all_villages(list_of_dict):
    list_of_vilages = []
    for vilage in list_of_dict:
        list_of_vilages =  [vilage for vilage in list_of_dict if vilage['town_type']=="Village"]
        list_of_vilages.append(vilage["town_type"])
    return list_of_vilages


""" This is the main function where the program starts executing .
    The function defined above gets executed after this main, in short they are called in the main function"""
if __name__ == '__main__':

    coordinates =         [{ 
                             "lat": 53.30935,
                              "long": -1.5331
                            },
                             {
                                  "lat": 53.21941,
                                  "long": -1.30514
                            }]

    elevations = [{
                    "max" : 100,
                    "min" : 20
                }]

    # pp.pprint(towns_file())                        
    # pp.pprint(cities_between_long_lat(coordinates, towns_file()))
    # pp.pprint(meads_in_name(towns_file()))
    pp.pprint(duplicates_name(towns_file())) 
    #pp.pprint(all_villages(towns_file()))
    #pp.pprint(towns_above_elevetion_of_100(towns_file(), elevations))