import json


def write_json(name, response):
    with open(f'test_files/{name}.json', 'w') as file:
        file.write(json.dumps(json.loads(response.text), ensure_ascii=False, indent=4))


def save_string(string):
    print(string.replace('-', '\\-').replace('.', '\\.'))
    return string.replace('-', '\\-').replace('.', '\\.')
