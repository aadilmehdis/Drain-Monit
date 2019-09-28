import json 
with open('./data.json', 'r') as file:
     json_data = json.load(file)
     for item in json_data["features"]:
        print(item)
        if item['properties']['iso3166_2'] in ['37','48','12','29','20','15','30','44']:
            print(item['properties']['iso3166_2'])

def fun(sensor_id, value):
    if value > threshold:
        item['properties']['iso3166_2']['status'] = "critical"