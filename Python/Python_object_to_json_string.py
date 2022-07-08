import json
python_dict={"name":"David","age":6,"class":"I"}
python_list=["Red","Green","Black"]
python_str="Python JSON"
python_int=(1234)
python_float=(21.34)
python_T=(True)
python_F=(False)
python_N=(None)

json_dict=json.dumps(python_dict)
json_list=json.dumps(python_list)
json_str=json.dumps(python_str)
json_int=json.dumps(python_int)
json_float=json.dumps(python_float)
json_T=json.dumps(python_T)
json_F=json.dumps(python_F)
json_N=json.dumps(python_N)

print("JSON DICTIONARY:",json_dict)
print("JSON LIST:",json_list)
print("JSON STRING:",json_str)
print("JSON INTEGER:",json_int)
print("JSON FLOAT:",json_float)
print("JSON TRUE:",json_T)
print("JSON FALSE:",json_F)
print("JSON NONE:",json_N)