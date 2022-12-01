import json
from django.conf import settings


def read_json():
    with open(settings.MAPPINGS_PATH, 'r', encoding='utf8') as file:
        return json.load(file)


def save_json(data):
    json_object = json.dumps(data, indent=2)
    print(settings.MEDIA_ROOT + settings.GENERATED_MAPPINGS)
    with open(settings.MEDIA_ROOT + settings.GENERATED_MAPPINGS, 'w', encoding='utf8') as file:
        return file.write(json_object)


def generate_mappings(keys):
    json = read_json()
    data = {'mappings': {}}
    for item in keys:
        key = json.get(item, None)
        if key:
            data['mappings'][item] = key

    return data


