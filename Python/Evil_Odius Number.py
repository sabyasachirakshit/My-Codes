"""
todo: In this program, our objective is to develop a python code that enables users to check if a number is evil or odius or not.
todo: User can also generate all evil and odius number within a desired range if he wants to..
! Note: A number is odius if there are odd numbers of 1 in the binary equivalent of a number!
! A number is evil which contains even number of 1 in the binary equivalent of a number!
? Example of Odius Number is : 1 [Binary Equivalent=0001 which contains odd numbers of 1]
? Example of Odius Number is : 3 [Binary Equivalent=0011 which contains odd numbers of 1]
"""
print('1.Check if a number evil or odius')
print('2.Generate Evil and Odius numbers within a desired range')
choice = int(input('Select your choice(1-2):'))
if choice == 1:
    num = int(input('Enter number:'))
    div = 1
    c = 0
    RM_list = []
    while(num != 0):
        rem = num % 2
        num = num//2
        RM_list.append(rem)
    RM_list = RM_list[::-1]
    for i, j in enumerate(RM_list):
        if RM_list[i] == 1:
            c += 1
    if c % 2 == 0:
        print('Evil Number!')
    else:
        print('Odius Number!')
elif choice == 2:
    print('All Evil and Odius numbers shall be generated within a given input range..')
    minx = int(input('Enter the starting number of the range:'))
    maxx = int(input('Enter the ending number of the range:'))
    print(
        f'All Evil and Odius numbers between {minx} and {maxx} are generated in their respective list:')
    Evil = []
    Odius = []
    while(minx <= maxx):
        div = 1
        temp = minx
        c = 0
        RM_list = []
        while(temp != 0):
            rem = temp % 2
            temp = temp//2
            RM_list.append(rem)
        RM_list = RM_list[::-1]
        for i, j in enumerate(RM_list):
            if RM_list[i] == 1:
                c += 1
        if c % 2 == 0:
            Evil.append(minx)
        else:
            Odius.append(minx)
        minx += 1
    print('Evil Numbers------------------->>')
    print(Evil)
    print('\n\nOdius Numbers------------------->>')
    print(Odius)
print('\nHit Enter to End.......')
input()
