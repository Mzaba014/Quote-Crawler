import json
with open('test.json') as jsonfile:
    parsed = json.load(jsonfile)

    print(json.dumps(parsed, indent=2, sort_keys=True))