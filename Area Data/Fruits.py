import json
from resources import get_data

def get_fruit_data():

    all_area_data = get_data.get_area_data()
    botw_names = get_data.get_botw_names()

    fruit_data = []

    for area_data in all_area_data:
        fruit_data.append({"Area Number":area_data['AreaNumber']})
        for i in range(len(area_data['Fruit'])):
            fruit_data[-1]['Fruit '+str(i+1)] = get_data.actor_name_conversion(area_data['Fruit'][i]['name'],botw_names)
            fruit_data[-1]['Value '+str(i+1)] = area_data['Fruit'][i]['num']

    return fruit_data

with open(r'Area Data\output\fruit_data.json','w') as f:
    f.write(json.dumps(get_fruit_data(),indent=2))