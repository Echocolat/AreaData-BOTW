import json
from resources import get_data

def get_autoplacement_data():

    all_area_data = get_data.get_area_data()
    botw_names = get_data.get_botw_names()

    autoplacement_data = []

    for area_data in all_area_data:
        autoplacement_data.append({"Area Number":area_data['AreaNumber']})
        if 'AutoCliffMaterial' in area_data:
            for i in range(len(area_data['AutoCliffMaterial'])):
                autoplacement_data[-1]['Cliff Material '+str(i+1)] = get_data.actor_name_conversion(area_data['AutoCliffMaterial'][i]['name'],botw_names)
                autoplacement_data[-1]['Cliff Material Value '+str(i+1)] = round(area_data['AutoCliffMaterial'][i]['num'],2)
        if 'AutoPlacementMaterial' in area_data:
            for j in range(len(area_data['AutoPlacementMaterial'])):
                autoplacement_data[-1]['Auto Placement Material '+str(j+1)] = get_data.actor_name_conversion(area_data['AutoPlacementMaterial'][j]['name'],botw_names)
                autoplacement_data[-1]['Auto Placement Material Value '+str(j+1)] = area_data['AutoPlacementMaterial'][j]['num']

    return autoplacement_data

with open(r'Area Data\output\autoplacement_data.json','w') as f:
    f.write(json.dumps(get_autoplacement_data(),indent=2))