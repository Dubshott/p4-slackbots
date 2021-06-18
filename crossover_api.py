import json

def Ideal_Weathers_parse(id):
    url = 'https://fish.nighthawkcodingsociety.com/all_ideal_weathers'
    json_data = get_url(url)
    json_object = json.loads(json_data)
    ideal_condition = ''
    for item in json_object['all_ideal_weathers']:
        if id == item['id']:
            ideal_condition = item['condition']
    return ideal_condition



if __name__ == "__main__":
    print(Ideal_Weathers_parse(2))