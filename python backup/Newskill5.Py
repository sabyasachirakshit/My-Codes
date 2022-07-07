list1 = [["005", "005" ], ["Ronit", "21"], ["Rakshit" , "19"]]
dic1 = dict(list1)
dic2= list(dic1)
for item in dic2:
    if str(item).isnumeric():
      print(item)
