import json
from django.conf import settings


def save_json(data):
    json_object = json.dumps(data, indent=2)
    print(json_object)
    with open(settings.MEDIA_ROOT + settings.GENERETED_CONFIG, 'w', encoding='utf8') as file:
        return file.write(json_object)



