import json

def actor_name_conversion(actor_name,botw_names):

    if actor_name in botw_names:
        return botw_names[actor_name]
    else:
        return actor_name

def get_area_data():

    with open(r'Area Data\resources\area_data.json','r') as area_data_file:
        all_area_data = json.loads(area_data_file.read())
    
    return all_area_data

def get_botw_names():
    
    with open(r'Area Data\resources\botw_names.json') as botw_names_file:
        botw_names = json.loads(botw_names_file.read())

    return botw_names