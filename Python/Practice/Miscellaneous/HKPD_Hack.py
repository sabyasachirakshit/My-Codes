import random
from collections import Counter
import time
def generate_ac_number():
    dig1=random.randint(0,9)
    dig2=random.randint(0,9)
    dig3=random.randint(0,9)
    dig4=random.randint(0,9)
    ac_number=str(dig1)+str(dig2)+str(dig3)+str(dig4)
    return ac_number
def start_cracking():
    while True:
        actual_number=generate_ac_number()
        c=Counter(actual_number)
        if any(count>1 for count in c.values()):
            continue
        else:
            break
    tries=5
    while tries!=0:
        dict1={}
        dict2={}
        num=input("Enter Passcode:")
        if num==actual_number:
            print(f"\nCongratulations! You Cracked The Code! The Code is {num}!")
            quit()
        else:
            ac_list=list(str(actual_number))
            num_list=list(num)
            for position,value in enumerate(ac_list):
                dict1[value]=position
            for position,value in enumerate(num_list):
                dict2[value]=position
            for key,value in dict2.items():
                if key in list(dict1.keys()):
                    if dict2[key]==dict1[key]:
                        print(f"{key} is correct digit placed in correct position")
                    else:
                        print(f"{key} is correct digit placed in wrong position")
                else:
                    print(f"{key} is wrong digit")
        print(f"\nTries Left:{tries-1}")
        tries-=1
    print("SECURITY BREACH!!")
    time.sleep(5)
    print("\n\n\n\n\n\n\n\n\n\n\nPASSWORD RESET!!!")
    c=input("Try Cracking again(y/n): ")
    if c=="y":
        start_cracking()
    else:
        quit()
start_cracking()