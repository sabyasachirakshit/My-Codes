def encrypt(string):
    lst = list(string[::-1])
    dictionary = {
        'a': '0',
        'e': '1',
        'i': '2',
        'o': '2',
        'u': '3'
    }
    i = 0
    while(i < len(lst)):
        if lst[i] in dictionary.keys():
            lst[i] = dictionary[lst[i]]
        i += 1
    lst.append("aca")
    encoded_msg = ""
    for i in lst:
        encoded_msg += i
    return encoded_msg


print(encrypt("banana"))
print(encrypt("karaca"))
print(encrypt("burak"))
print(encrypt("alpaca"))
