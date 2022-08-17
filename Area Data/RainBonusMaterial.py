import json
from resources import get_data

def get_rainbonus_data():

    all_area_data = get_data.get_area_data()
    botw_names = get_data.get_botw_names()

    rainbonus_data = []

    for area_data in all_area_data:
        rainbonus_data.append({"Area Number":area_data['AreaNumber']})
        for i in range(len(area_data['RainBonusMaterial'])):
            rainbonus_data[-1]['Rain Bonus Material '+str(i+1)] = get_data.actor_name_conversion(area_data['RainBonusMaterial'][i]['name'],botw_names)
            rainbonus_data[-1]['Value '+str(i+1)] = area_data['RainBonusMaterial'][i]['num']

    return rainbonus_data

with open(r'Area Data\output\rainbonus_data.json','w') as f:
    f.write(json.dumps(get_rainbonus_data(),indent=2))