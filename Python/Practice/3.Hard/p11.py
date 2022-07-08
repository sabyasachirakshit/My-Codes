def bar_chart(dict):
    lst = list(dict.values())
    print(lst)
    no_of_pass = len(lst)
    temp = 1
    while(no_of_pass != 0):
        for i in range(0, len(lst)):
            for j in range(1, len(lst)):
                if lst[i-1] >= lst[j-1]:
                    temp = lst[i-1]
                    lst[i-1] = lst[j-1]
                    lst[j-1] = temp
        no_of_pass -= 1
    print(lst)
    i = 0

    def get_key(val, dict):
        for key, value in dict.items():
            if value == val:
                return key
    while(i < len(lst)):
        key = get_key(lst[i], dict)
        no_of_hash = lst[i]//50
        print(f"{key} |", end="")
        print("#"*no_of_hash, end="")
        print(lst[i], end="")
        print('\n')
        i += 1


bar_chart({"Q4": 250, "Q1": 300, "Q2": 150, "Q3": 0})
