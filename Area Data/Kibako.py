import json
from resources import get_data

def get_kibako_data():

    all_area_data = get_data.get_area_data()
    botw_names = get_data.get_botw_names()

    kibako_data = []

    for area_data in all_area_data:
        kibako_data.append({"Area Number":area_data['AreaNumber'],"Kibako":area_data['Kibako']})

    return kibako_data

with open(r'Area Data\output\kibako_data.json','w') as f:
    f.write(json.dumps(get_kibako_data(),indent=2))