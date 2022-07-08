import math,itertools
def check_armstrong(minx,maxx):
    armstrong_list=[]
    while(minx <= maxx):
        temp = minx
        sumx = 0
        while(temp > 0):
            digit = temp % 10
            sumx += digit**3
            temp //= 10
        if(sumx == minx):
            armstrong_list.append(sumx)
        minx += 1
    return armstrong_list

def check_disarium(minx,maxx):
    disarium_list=[]
    while(minx <= maxx):
        temp = minx
        lst_num = []
        sumx = 0
        while(temp > 0):
            digit = temp % 10
            lst_num.append(digit)
            temp //= 10
        fin_num = lst_num[::-1]
        for i in range(len(fin_num)):
            fin_num[i] = math.pow(fin_num[i], i+1)
        for i in range(len(fin_num)):
            sumx += fin_num[i]
        if(sumx == minx):
            disarium_list.append(sumx)
        minx += 1
    return disarium_list

def check_automorphic(minx,maxx):
    automorphic_list=[]
    while(minx <= maxx):
        black_flag = 0
        temp = minx
        c = 0
        while(temp > 0):
            c += 1
            temp //= 10
        sq_num = minx*minx
        temp = sq_num
        lst = []
        while(temp > 0):
            dig = temp % 10
            lst.append(dig)
            temp //= 10
        m_list = lst[::-1]
        if c == 1:
            if(m_list[-c] == minx):
                print(minx)
        else:
            lst = []
            temp = minx
            while(temp > 0):
                dig = temp % 10
                lst.append(dig)
                temp //= 10
            mm_list = lst[::-1]
            while(c != 0):
                if(m_list[-c] != mm_list[-c]):
                    black_flag = 1
                    break
                else:
                    c -= 1
            if(black_flag == 0):
                automorphic_list.append(minx)
        minx += 1
    return automorphic_list

def check_neon(minx,maxx):
    neon_list=[]
    while(minx <= maxx):
        sq = minx**2
        temp = sq
        s = 0
        while temp > 0:
            dig = temp % 10
            s += dig
            temp //= 10
        if s == minx:
            neon_list.append(minx)
        minx += 1
    return neon_list

def check_sunny(minx,maxx):
    sunny_list=[]
    while(minx <= maxx):
        next_number = minx+1
        sq_root = math.sqrt(next_number)
        for i in range(1, 100000):
            if float(i) == sq_root:
                sunny_list.append(minx)
                break
        minx += 1
    return sunny_list

def check_strong(min,max):
    strong_list=[]
    while(min <= max):
        temp = min
        sumx = 0
        factz = 1
        while(temp > 0):
            digit = temp % 10
            while digit != 0:
                factz *= digit
                digit -= 1
            sumx += factz
            factz = 1
            temp //= 10
        if(sumx == min):
            strong_list.append(sumx)
        min += 1
    return strong_list

def check_trimorphic(minx,maxx):
    trimorphic_list=[]
    while(minx <= maxx):
        black_flag = 0
        temp = minx
        c = 0
        while(temp > 0):
            c += 1
            temp //= 10
        cb_num = minx*minx*minx
        temp = cb_num
        lst = []
        while(temp > 0):
            dig = temp % 10
            lst.append(dig)
            temp //= 10
        m_list = lst[::-1]
        if c == 1:
            if(m_list[-c] == minx):
                print(minx)
        else:
            lst = []
            temp = minx
            while(temp > 0):
                dig = temp % 10
                lst.append(dig)
                temp //= 10
            mm_list = lst[::-1]
            while(c != 0):
                if(m_list[-c] != mm_list[-c]):
                    black_flag = 1
                    break
                else:
                    c -= 1
            if(black_flag == 0):
                trimorphic_list.append(minx)
        minx += 1
    return trimorphic_list

def check_vampire(minx,maxx):
    vampire_list=[]
    while(minx <= maxx):
        temp = minx
        c = 0
        while(temp > 0):
            c += 1
            temp //= 10
        if c % 2 == 0:
            num_lst = []
            temp = minx
            while temp > 0:
                digit = temp % 10
                num_lst.append(digit)
                temp //= 10
            num_lst = num_lst[::-1]
            lst1 = []
            lst2 = []
            mid = len(num_lst)//2
            for i in range(0, mid):
                lst1.append(str(num_lst[i]))
            for i in range(mid, len(num_lst)):
                lst2.append(str(num_lst[i]))
            for i, j in enumerate(lst1):
                lst1[i] = int(lst1[i])
            for i, j in enumerate(lst2):
                lst2[i] = int(lst2[i])
            s1 = list(itertools.permutations(lst1))
            x1 = []
            for i in s1:
                x1.append(list(i))
            new1 = []
            for i in x1:
                for j in i:
                    new1.append(j)
            for i, j in enumerate(new1):
                new1[i] = str(new1[i])
            concat = ''
            i = 1
            perm1 = []
            while i <= len(new1):
                if i % len(lst1) != 0:
                    concat += new1[i-1]
                else:
                    concat += new1[i-1]
                    perm1.append(concat)
                    concat = ''
                i += 1
            for i, j in enumerate(perm1):
                perm1[i] = int(perm1[i])
            s2 = list(itertools.permutations(lst2))
            x1 = []
            for i in s2:
                x1.append(list(i))
            new1 = []
            for i in x1:
                for j in i:
                    new1.append(j)
            for i, j in enumerate(new1):
                new1[i] = str(new1[i])
            concat = ''
            i = 1
            perm2 = []
            while i <= len(new1):
                if i % len(lst2) != 0:
                    concat += new1[i-1]
                else:
                    concat += new1[i-1]
                    perm2.append(concat)
                    concat = ''
                i += 1
            for i, j in enumerate(perm2):
                perm2[i] = int(perm2[i])
            mult = []
            for i in perm1:
                for j in perm2:
                    mult.append(i*j)
            for i in mult:
                if i == minx:
                    vampire_list.append(minx)
                    break
        minx += 1
    return vampire_list