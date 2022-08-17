import json
from resources import get_data

def get_animal_data():

    all_area_data = get_data.get_area_data()
    botw_names = get_data.get_botw_names()

    animal_data = []

    for area_data in all_area_data:
        animal_data.append({"Area Number":area_data['AreaNumber']})
        for i in range(len(area_data['Animal'])):
            animal_data[-1]['Animal '+str(i+1)] = get_data.actor_name_conversion(area_data['Animal'][i]['name'],botw_names)
            animal_data[-1]['Value '+str(i+1)] = area_data['Animal'][i]['num']

    return animal_data

with open(r'Area Data\output\animal_data.json','w') as f:
    f.write(json.dumps(get_animal_data(),indent=2))