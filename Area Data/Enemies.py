import json
from resources import get_data

def get_enemies_data():

    all_area_data = get_data.get_area_data()
    botw_names = get_data.get_botw_names()

    enemies_data = []

    for area_data in all_area_data:
        enemies_data.append({"Area Number":area_data['AreaNumber']})
        for i in range(len(area_data['Enemy'])):
            enemies_data[-1]['Enemy '+str(i+1)] = get_data.actor_name_conversion(area_data['Enemy'][i]['name'],botw_names)
            enemies_data[-1]['Value '+str(i+1)] = area_data['Enemy'][i]['num']

    return enemies_data

with open(r'Area Data\output\enemies_data.json','w') as f:
    f.write(json.dumps(get_enemies_data(),indent=2))