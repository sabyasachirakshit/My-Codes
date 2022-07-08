def add_name(dic, key, value):
    dic[key] = value
    print(dic)


add_name({}, "Brutus", 300)
add_name({"piano": 500}, "Brutus", 400)
add_name({"piano": 500, "stereo": 300}, "caligula", 400)
