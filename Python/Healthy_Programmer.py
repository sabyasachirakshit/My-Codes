"""
                           Healthy Programmer Project
 
? The objective of this project is to remind the programmer to complete three 
? mandatory things which are-- drinking water 3.5 L per day, do eyes exercise 
?e very 30 minutes and lastly do physical exercise every 45 min. This project
? notifies the programmer to do the objectives within 9am-5pm everyday and save 
? the progress in a text log file.

! After drinking water, programmer needs to type 'drank', and only then, the 
! reminder of water.mp3 would stop playing else it will continue to play.
! Same for Eyes, he has to type 'EyDone' and for physical activities  he has 
! to type 'ExDone'. And the timestamp of when he did would be saved in a text log file.

"""
import datetime
import time  # * To check real time
from os import system  # * To access paths
import pygame  # * For audio play
from plyer import notification  # * For popping up notification in desktop
pygame.mixer.init()
pl = 'Progress_Log.txt'


def writefile_water(wt):
    f = open(pl, 'a')
    x = "Drank Water on:  "
    f.write(x)
    f.write(str(wt))
    f.write("\n")
    f.close()


def writefile_eyes(et):
    f = open(pl, 'a')
    x = "Performed Eye Exercise on:  "
    f.write(x)
    f.write(str(et))
    f.write("\n")
    f.close()


def writefile_physical(pt):
    f = open(pl, 'a')
    x = "Performed Physical Exercise on:  "
    f.write(x)
    f.write(str(pt))
    f.write("\n")
    f.close()


def water_objective():
    pygame.mixer.music.load('water.mp3')
    pygame.mixer.music.play(-1)
    notification.notify(
        title='Alert', message='DRINK WATER 2 GLASS', timeout=30)
    water = str(input())
    if(water.upper() == "DRANK"):
        water_time = datetime.datetime.now()
        writefile_water(water_time)
        pygame.mixer.music.stop()
    else:
        water_objective()


def eyes_objective():
    pygame.mixer.music.load('eyes.mp3')
    pygame.mixer.music.play(-1)
    notification.notify(title='Alert', message='DO EYE EXERCISE', timeout=30)
    eye = str(input())
    if(eye.upper() == "EYDONE"):
        eye_time = datetime.datetime.now()
        writefile_eyes(eye_time)
        pygame.mixer.music.stop()
    else:
        eyes_objective()


def physical_objective():
    pygame.mixer.music.load('physical.mp3')
    pygame.mixer.music.play(-1)
    notification.notify(
        title='Alert', message='DO PHYSICAL EXERCISE', timeout=30)
    py = str(input())
    if(py.upper() == "EXDONE"):
        pt_time = datetime.datetime.now()
        writefile_physical(pt_time)
        pygame.mixer.music.stop()
    else:
        physical_objective()


def start():
    while(True):
        now = datetime.datetime.now()
        system("cls")
        current_time = now.strftime("%H:%M:%S")
        print(f"Current Time:{current_time}")
        time.sleep(1)
        if(current_time == "09:30:00" or current_time == "10:00:00" or current_time == "11:00:00" or current_time == "11:30:00" or current_time == "12:30:00" or current_time == "13:00:00" or current_time == "14:00:00" or current_time == "14:30:00" or current_time == "15:30:00" or current_time == "16:00:00" or current_time == "17:00:00"):
            eyes_objective()
        if(current_time == "09:45:00" or current_time == "11:15:00" or current_time == "12:45:00" or current_time == "14:15:00" or current_time == "15:45:00"):
            physical_objective()
        if(current_time == "10:30:00" or current_time == "12:00:00" or current_time == "13:30:00" or current_time == "15:00:00" or current_time == "16:30:00"):
            eyes_objective()
            physical_objective()
        if(current_time == "10:20:00" or current_time == "11:20:00" or current_time == "12:20:00" or current_time == "13:20:00" or current_time == "14:20:00" or current_time == "15:20:00" or current_time == "16:20:00"):
            water_objective()
        if(current_time >= "17:00:00"):
            quit()
        else:
            continue


start()
print('\nHit Enter to End.......')
input()
