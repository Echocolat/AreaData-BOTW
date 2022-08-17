import json
from resources import get_data

def get_mushroom_data():

    all_area_data = get_data.get_area_data()
    botw_names = get_data.get_botw_names()

    mushroom_data = []

    for area_data in all_area_data:
        mushroom_data.append({"Area Number":area_data['AreaNumber']})
        for i in range(len(area_data['Mushroom'])):
            mushroom_data[-1]['Mushroom '+str(i+1)] = get_data.actor_name_conversion(area_data['Mushroom'][i]['name'],botw_names)
            mushroom_data[-1]['Value '+str(i+1)] = area_data['Mushroom'][i]['num']

    return mushroom_data

with open(r'Area Data\output\mushroom_data.json','w') as f:
    f.write(json.dumps(get_mushroom_data(),indent=2))