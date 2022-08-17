import json

def actor_name_conversion(actor_name,botw_names):

    if actor_name in botw_names:
        return botw_names[actor_name]
    else:
        return actor_name

def armor_name_conversion(armor_name,botw_names):
    if "001" in armor_name:
        return actor_name_conversion(armor_name,botw_names) + " level 0"
    elif "002" in armor_name:
        return actor_name_conversion(armor_name,botw_names) + " level 1"
    elif "003" in armor_name:
        return actor_name_conversion(armor_name,botw_names) + " level 2"
    elif "004" in armor_name:
        return actor_name_conversion(armor_name,botw_names) + " level 3"
    else:
        return actor_name_conversion(armor_name,botw_names) + " level 4"

def get_area_data():

    with open(r'Area Data\resources\area_data.json','r') as area_data_file:
        all_area_data = json.loads(area_data_file.read())
    
    return all_area_data

def get_botw_names():
    
    with open(r'Area Data\resources\botw_names.json') as botw_names_file:
        botw_names = json.loads(botw_names_file.read())

    return botw_names