import json
from resources import get_data

def get_insect_data():

    all_area_data = get_data.get_area_data()
    botw_names = get_data.get_botw_names()

    insect_data = []

    for area_data in all_area_data:
        insect_data.append({"Area Number":area_data['AreaNumber']})
        for i in range(len(area_data['Insect'])):
            insect_data[-1]['Insect '+str(i+1)] = get_data.actor_name_conversion(area_data['Insect'][i]['name'],botw_names)
            insect_data[-1]['Value '+str(i+1)] = area_data['Insect'][i]['num']

    return insect_data

with open(r'Area Data\output\insect_data.json','w') as f:
    f.write(json.dumps(get_insect_data(),indent=2))