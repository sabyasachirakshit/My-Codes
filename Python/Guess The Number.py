"""
todo:In this program our objective is to make a mini game of guessing a number through python code.
! User has to correctly guess a randomly generated number within a limit
"""
import random
while(True):
    number = random.randint(10, 30)
    tries_left = 10
    attempts = 1
    i = 0
    while(i < 10):
        tries_left -= 1
        if(tries_left == -1):
            break
        guess = int(input('Guess the number between 10-30 within 10 tries:'))
        if(guess == number):
            print('Correct Guess!')
            print('You guessed the number correctly within ',
                  attempts, 'attempts..')
            break
        elif(guess < number):
            print('Wrong Guess!')
            print('Tries Left:', tries_left)
            if(tries_left != 0):
                print('Suggestions: Increase the number')
            else:
                break
        elif(guess > number):
            print('Wrong Guess!')
            print('Tries Left:', tries_left)
            if(tries_left != 0):
                print('Suggestions: Decrease the number')
            else:
                break
        i += 1
        attempts += 1
    if(tries_left == 0):
        print('\nThe correct number was:', number)
        print('Better Luck Next Time')
    print("Do you want to play again? Press 'y' for yes or any other key to exit..")
    c = str(input())
    if(c.upper() == 'Y'):
        continue
    else:
        print('Thank You For Playing This Game :) Hope you enjoyed it..!')
        break
print('\nHit Enter to End.......')
input()
