import json
from resources import get_data

def get_bird_data():

    all_area_data = get_data.get_area_data()
    botw_names = get_data.get_botw_names()

    bird_data = []

    for area_data in all_area_data:
        bird_data.append({"Area Number":area_data['AreaNumber']})
        for i in range(len(area_data['Bird'])):
            bird_data[-1]['Bird '+str(i+1)] = get_data.actor_name_conversion(area_data['Bird'][i]['name'],botw_names)
            bird_data[-1]['Value '+str(i+1)] = area_data['Bird'][i]['num']

    return bird_data

with open(r'Area Data\output\bird_data.json','w') as f:
    f.write(json.dumps(get_bird_data(),indent=2))