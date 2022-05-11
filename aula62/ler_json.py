import json

with open('js.json', 'r') as file:
    d1_json = file.read()
    d1_json = json.loads(d1_json)

for k, v in d1_json.items():
    print(k)
    for pk, pv in v.items():
        print(f'\t{pk}: {pv}')

    print()
