#utf-8
#random movie generator
#this code help you to generate a random video from the IMDB's trends


import imdb as IMDb
import random
#random movie importing


class ChooseMovie(object):
    def __init__(self):
        self.cursor = IMDb()
        self.top100 = self.cursor.get_top100_movies()

#here top100 means the top 100 movies from IMDb

def __repr__(self):
    num = int(random.randint(0,99))
    return str(f"{num}: {self.top100[num]}")

#random movies will be displayed to you for free only within 100

if __name__ == '__main__':
    print(ChooseMovie())

#DONE,FUCK OFF :^  