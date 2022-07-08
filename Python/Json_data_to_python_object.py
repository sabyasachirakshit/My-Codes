import json
json_obj='{"Name":"David","Class":"I","Age":6}'
python_obj=json.loads(json_obj)
print("JSON DATA-->")
print(python_obj)
print(type(python_obj))
print("Name:",python_obj["Name"])
print("Age:",python_obj["Age"])
print("Class:",python_obj["Class"])