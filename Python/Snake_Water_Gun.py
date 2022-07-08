""" 
todo: In this program, our objective is to make a game named Snake Water Gun using Python..
? The user has to play either snake or water or gun. Then the computer will also paly either sanke or water or gun.
! Snake beats water,water beats gun,gun beats snake!
"""

import random
print('Welcome to snake water gun game...')
print("\nDo you want to know the rules of the game? ")
print("Press 'y' for yes or any other key for no and directly play the game.")
c = str(input())
p = 'Python wins this round'
u = 'You won this round'
if(c.upper() == 'Y'):
    print('\nYou would be playing this game with Python as your opponent.')
    print('All you have to do is to choose either snake or water or gun each time')
    print('And in response for that, Python would also choose snake or water or gun.')
    print('The rules are quite simple. If you show snake and Python shows water, you would win because snake drinks all the water')
    print('If you show water and Python shows gun, you would win because the gun would drown in water')
    print('If you show gun and Python shows Snake, you would win because gun would kill the snake')
    print('In simple words, water beats gun ; gun beats  snake ; snake beats water')


def im_decision(pss):
    flag = 0
    if(pss.upper() == 'S'):
        print('You: Snake ; Python: Gun')
        print(p)
        flag = 0
        return flag
    elif(pss.upper() == 'W'):
        print('You: Water ; Python: Snake')
        print(p)
        flag = 0
        return flag
    else:
        print('You: Gun ; Python: Water')
        print(p)
        flag = 0
        return flag


def decision(ps, py):
    flag = 1
    if(py % 2 != 0):
        if(ps.upper() == 'S'):
            print('You: Snake ; Python: Gun')
            print(p)
            flag = 0
            return flag
        elif(ps.upper() == 'W'):
            print('You: Water ; Python: Snake')
            print(p)
            flag = 0
            return flag
        else:
            print('You: Gun ; Python: Water')
            print(p)
            flag = 0
            return flag
    else:
        if(ps.upper() == 'S'):
            print('You: Snake ; Python: Water')
            print(u)
            return flag
        elif(ps.upper() == 'W'):
            print('You: Water ; Python: Gun')
            print(u)
            return flag
        else:
            print('You: Gun ; Python: Snake')
            print(u)
            return flag


while(True):
    print('\nChoose Difficulty Level---->')
    print('1.Easy 2.Medium 3.Hard 4.Impossible')
    diff_level = int(input(
        'Press 1 for easy ; Press 2 for medium ; Press 3 for Hard ; Press 4 for impossible---->'))
    if(diff_level == 4):
        print('Warning... ')
        print('Preparing the toughest Python A.I BOT..')
    rounds = int(input('How many rounds you want to play against Python:'))
    o_rounds = rounds
    player_score = 0
    python_score = 0
    while(rounds > 0):
        rounds -= 1
        player_choice = input(
            "Press 's' for snake, 'w' for water and 'g' for gun:")
        if(diff_level == 1):
            python_choice = random.randint(1, 10)
            result = decision(player_choice, python_choice)
        elif(diff_level == 2):
            python_choice = random.randint(1, 5)
            result = decision(player_choice, python_choice)
        elif(diff_level == 3):
            python_choice = random.randint(2, 4)
            result = decision(player_choice, python_choice)
        else:
            result = im_decision(player_choice)
        if(result == 0):
            python_score += 1
        else:
            player_score += 1
        print('Rounds Left:', rounds)
    print("-------------------------")
    print('\nYour Score:', player_score)
    print("Python's score:", python_score)
    if(python_score > player_score):
        print('\nSorry, Better Luck Next Time..')
        if(diff_level == 4):
            print(
                "Don't be upset. You were playing against the imposssible Python A.I bot!")
            print("How about trying again? ;)")
    elif(python_score == player_score):
        if(o_rounds >= 10):
            print(
                "What a nice Coincidence..! A tie is not that bad. Let's play again ..shall we?")
        else:
            print("It was a Tie..! Too bad isn't it??")
    else:
        if(diff_level == 1):
            print(
                'Congratulations..You sucessfully able to beat Python in easy difficulty')
        elif(diff_level == 2):
            print(
                'Wonderful..You were sucessfully able to beat Python in medium difficulty')
        else:
            print(
                'Amazing!! Wow..You were sucessfully able to beat Python in hard difficulty')
    choice = input(
        "Want to play again? Press 'y' for yes or any other key to exit---> ")
    if(choice.upper() != 'Y'):
        print(
            '\nThanks for playing this game. Hope you enjoyed it.. Come back soon again..')
        print('Developer--> SABYASACHI RAKSHIT')
        break
print('\nHit Enter to End.......')
input()
