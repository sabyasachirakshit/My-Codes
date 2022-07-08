import random


class HeadQuarter:
    collection_of_words = ['COMPUTER', 'KEYBOARD', 'MOUSE', 'MONITOR', 'FLASHDRIVE', 'COMPACTDISC', 'HARDWARE',
                           'SOFTWARE', 'MEMORY', 'NETWORKING', 'CRYPTOGRAPHY', 'CYBERSECURITY', 'PROGRAMMING', 'HACKING', 'VIRUS', 'ANTIVIRUS']


class Hangman:
    def __init__(self, player_name):
        self.player_name = player_name

    def display(self):
        print(f"WELCOME TO HANMGMAN GAME! {self.player_name}")
        print('YOU HAVE TO GUESS THE LETTERS OF A WORD RELATED TO COMPUTER WORLD!! IF YOU GUESS THE WRONG WORD, TRIES WILL BE DEDUCTED BY 1')
        print('YOU ONLY HAVE 10 TRIES LEFT, GOOD LUCK!!')
        print('WARNING! TURN CAPSLOCK ON ~ ~ ~!')

    def flow_of_control(self):
        selected_word = random.choice(HeadQuarter.collection_of_words)
        sizeof_sw = len(selected_word)
        empty_box = []
        while sizeof_sw != 0:
            empty_box.append('-')
            sizeof_sw -= 1
        print(empty_box)
        tries = 10
        while True:
            if tries != 0:
                black_FLAG = 1
                if '-' in empty_box:

                    guessed_letter = input('Guess The Letter:')
                    lstwrd = list(selected_word)
                    for i, j in enumerate(lstwrd):
                        if guessed_letter == j and empty_box[i] == '-':
                            empty_box.pop(i)
                            empty_box.insert(i, guessed_letter)
                            black_FLAG = 0
                            break
                    print(empty_box)
                    if black_FLAG == 1:
                        tries -= 1
                    print(f'Tries Left:{tries}')
                else:
                    print(
                        f'Congrats! You did it!! The word is {selected_word}!!')
                    break
            else:
                print(f'Sorry! You lost! The word was {selected_word}!!')
                break


if __name__ == "__main__":
    name = input("Enter Your Name:")
    start = Hangman(f"{name.title()}")
    start.display()
    start.flow_of_control()
    print('\nHit Enter to End.......')
    input()
