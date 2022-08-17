import json
from resources import get_data

def get_recommend_data():

    all_area_data = get_data.get_area_data()
    botw_names = get_data.get_botw_names()

    recommend_data = []

    for area_data in all_area_data:
        recommend_data.append({"Area Number":area_data['AreaNumber']})
        for i in range(len(area_data['Recommend']['armors'])):
            recommend_data[-1]['Armor '+str(i)] = get_data.armor_name_conversion(area_data['Recommend']['armors'][i]['name'],botw_names)
        recommend_data[-1]['Hearts'] = area_data['Recommend']['heart']
        recommend_data[-1]['Stamina'] = area_data['Recommend']['guts']
        for j in range(len(area_data['Recommend']['weapons'])):
            recommend_data[-1]['Weapon '+str(j)] = get_data.actor_name_conversion(area_data['Recommend']['weapons'][j]['name'],botw_names)

    return recommend_data

with open(r'Area Data\output\recommend_data.json','w') as f:
    f.write(json.dumps(get_recommend_data(),indent=2))