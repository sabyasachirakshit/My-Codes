# *************** This is Date and Time Module **********************
import time
# *************** This is Local Time Module *************************
from datetime import datetime
# *************** This Module Is For Play Music *********************
import pygame
# ************************ These Variables Contains Reminder Time **************************************
A, B, C, D, E, F, G = "09:25:00", "09:50:00", "10:25:00", "10:50:00", "11:25:00", "11:50:00", "12:25:00"
H, I, J, K, L, M, N = "12:50:00", "13:25:00", "13:50:00", "14:25:00", "14:50:00", "15:25:00", "15:50:00"
O, P = "16:25:00", "16:50:00"
A1, B1, C1, D1, E1, F1, G1 = "09:30:00", "10:00:00", "10:30:00", "11:00:00", "11:30:00", "12:00:00", "12:30:00"
H1, I1, J1, K1, L1, M1, N1 = "13:00:00", "13:30:00", "14:00:00", "14:30:00", "15:00:00", "15:30:00", "16:00:00"
O1, P1 = "16:30:00", "17:00:00"
A2, B2, C2, D2, E2 = "09:45:00", "11:15:00", "12:45:00", "14:15:00", "15:45:00"
# *********************************** Time Variables **********************************************************
while(True):
    localtime1 = time.asctime(time.localtime(time.time()))
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    pygame.mixer.init()               # pygame mixer Module Initializing
# ****************************** Water Drinking Reminder *****************************************************
    if current_time == A or current_time == C or current_time == E or current_time == G or current_time == I \
        or current_time == K or current_time == M or current_time == O:
        pygame.mixer.music.load('water.MP3')
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(100)
        print("Please Drink 250ml Water. \nIf you have dranked,Press d")
        dranked1 = input()
        if dranked1 == "d":
            f1 = open("DrinkWater.txt", "a")
            f1.write(f"\nYou Drinked 250ml Water on {localtime1}")
            f1.close()
            pygame.mixer.music.stop()
    elif current_time == B or current_time == D or current_time == F or current_time == H or current_time == J \
        or current_time == L or current_time == N or current_time == P:
        pygame.mixer.music.load('water.MP3')
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(100)
        print("Please Drink 200ml Water. \nIf you have dranked,Press d")
        dranked2 = input()
        if dranked2 == "d":
            f1 = open("DrinkWater.txt", "a")
            f1.write(f"\nYou Drinked 200ml Water on {localtime1}")
            f1.close()
            pygame.mixer.music.stop()
# ****************************** Eyes Exercise Reminder ***********************************************
    elif current_time == A1 or current_time == B1 or current_time == C1 or current_time == D1 \
        or current_time == E1 or current_time == F1 or current_time == G1 or current_time == H1:
        pygame.mixer.music.load('eyes.wav')
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(100)
        print("This is your eyes exercise Reminder\n press s to turn off")
        off1 = input("Enter s\n")
        if off1 == "s":
            f1 = open("DrinkWater.txt", "a")
            f1.write(f"\nYou turned off eyes exercise reminder on {localtime1}")
            f1.close()
            pygame.mixer.music.stop()
# *************************** Physical Exercise Reminder ***********************************************
            pygame.mixer.music.load('water.MP3')
            pygame.mixer.music.set_volume(1.0)
            pygame.mixer.music.play(100)
            print("This is your Physical exercise Reminder\n press s to turn off")
            off4 = input()
            if off4 == "s":
                f1 = open("DrinkWater.txt", "a")
                f1.write(f"\nYou turned off Physical exercise reminder on {localtime1}")
                f1.close()
                pygame.mixer.music.stop()
# ********************************* Eyes Exercise Reminder **************************************************
    elif current_time == I1 or current_time == J1 or current_time == K1 or current_time == L1 \
            or current_time == M1 or current_time == N1 or current_time == O1 or current_time == P1:
        pygame.mixer.music.load('eyes.wav')
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(100)
        print("This is your eyes exercise Reminder\n press s to turn off")
        off2 = input()
        if off2 == "s":
            f1 = open("DrinkWater.txt", "a")
            f1.write(f"\nYou turned off eyes exercise reminder on {localtime1}")
            f1.close()
            pygame.mixer.music.stop()
# ************************ Physical Exercise Reminder ******************************************
            pygame.mixer.music.load('water.MP3')
            pygame.mixer.music.set_volume(1.0)
            pygame.mixer.music.play(100)
            print("This is your Physical exercise Reminder\n press s to turn off")
            off5 = input()
            if off5 == "s":
                f1 = open("DrinkWater.txt", "a")
                f1.write(f"\nYou turned off Physical exercise reminder on {localtime1}")
                f1.close()
                pygame.mixer.music.stop()
# ************************ Physical Exercise Reminder ******************************************
    elif current_time == A2 or current_time == B2 or current_time == C2 or current_time == D2 \
            or current_time == E2:
        pygame.mixer.music.load('eyes.wav')
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(100)
        print("This is your Physical exercise Reminder\n press s to turn off")
        off3 = input()
        if off3 == "s":
            f1 = open("DrinkWater.txt", "a")
            f1.write(f"\nYou turned off Physical exercise reminder on {localtime1}")
            f1.close()
            pygame.mixer.music.stop()
            continue



