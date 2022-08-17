import json
from resources import get_data

def get_climate_data():

    all_area_data = get_data.get_area_data()
    botw_names = get_data.get_botw_names()

    climate_data = []

    for area_data in all_area_data:
        climate_data.append({"Area Number":area_data['AreaNumber'],"Area Name":area_data['Area'],"EnvSound":area_data['EnvSound'],"Climate":area_data['Climate']})

    return climate_data

with open(r'Area Data\output\climate_data.json','w') as f:
    f.write(json.dumps(get_climate_data(),indent=2))