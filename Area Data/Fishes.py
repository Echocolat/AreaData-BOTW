import json
from resources import get_data

def get_fish_data():

    all_area_data = get_data.get_area_data()
    botw_names = get_data.get_botw_names()

    fish_data = []

    for area_data in all_area_data:
        fish_data.append({"Area Number":area_data['AreaNumber']})
        for i in range(len(area_data['Fish'])):
            fish_data[-1]['Fish '+str(i+1)] = get_data.actor_name_conversion(area_data['Fish'][i]['name'],botw_names)
            fish_data[-1]['Value '+str(i+1)] = area_data['Fish'][i]['num']

    return fish_data

with open(r'Area Data\output\fish_data.json','w') as f:
    f.write(json.dumps(get_fish_data(),indent=2))