import json
import os.path

thresh_max = 15000
thresh_min = 9000

# with open('./data.json', 'r') as file:
#      json_data = json.load(file)
#      for item in json_data["features"]:
#         print(item)
#         if item['properties']['iso3166_2'] in ['37','48','12','29','20','15','30','44']:
#             print(item['properties']['iso3166_2'])

def update_val(sensor_id, value):
    print(value, thresh_max)
    BASE = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(BASE, "data.json")
    if value > thresh_max:
        with open(file_name, 'r') as file:
            json_data = json.load(file)
            for item in json_data["features"]:
                if item['properties']['iso3166_2'] == sensor_id:
                    # print(item['properties']['iso3166_2'])
                    item['properties']['status'] = "critical"
    elif value > thresh_min:
        with open(file_name, 'r') as file:
            json_data = json.load(file)
            for item in json_data["features"]:
                if item['properties']['iso3166_2'] == sensor_id:
                    item['properties']['status'] = "normal"
    else:
        with open(file_name, 'r') as file:
            json_data = json.load(file)
            for item in json_data["features"]:
                if item['properties']['iso3166_2'] == sensor_id:
                    item['properties']['status'] = "clogged"

    with open(file_name, "w") as jsonFile:
        json.dump(json_data, jsonFile, indent=2)

if __name__ == "__main__":

    update_val('12', 16)
