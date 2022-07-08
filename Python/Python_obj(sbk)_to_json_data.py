import json
p_str = {'4': 5, '6': 7, '1': 3, '2': 4}
print("Original string:", p_str)
print("JSON DATA->", json.dumps(p_str, sort_keys=True, indent=4))
