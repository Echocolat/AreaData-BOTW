import json
from resources import get_data

def get_grasscut_data():

    all_area_data = get_data.get_area_data()
    botw_names = get_data.get_botw_names()

    grasscut_data = []

    for area_data in all_area_data:
        grasscut_data.append({"Area Number":area_data['AreaNumber']})
        for i in range(len(area_data['GrassCut'])):
            grasscut_data[-1]['Material '+str(i+1)] = get_data.actor_name_conversion(area_data['GrassCut'][i]['name'],botw_names)
            grasscut_data[-1]['Value '+str(i+1)] = area_data['GrassCut'][i]['num']

    return grasscut_data

with open(r'Area Data\output\grasscut_data.json','w') as f:
    f.write(json.dumps(get_grasscut_data(),indent=2))