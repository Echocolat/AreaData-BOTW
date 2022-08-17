import json
from resources import get_data

def get_plant_data():

    all_area_data = get_data.get_area_data()
    botw_names = get_data.get_botw_names()

    plant_data = []

    for area_data in all_area_data:
        plant_data.append({"Area Number":area_data['AreaNumber']})
        for i in range(len(area_data['Plant'])):
            plant_data[-1]['Plant '+str(i+1)] = get_data.actor_name_conversion(area_data['Plant'][i]['name'],botw_names)
            plant_data[-1]['Value '+str(i+1)] = area_data['Plant'][i]['num']

    return plant_data

with open(r'Area Data\output\plant_data.json','w') as f:
    f.write(json.dumps(get_plant_data(),indent=2))