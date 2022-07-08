import random as r
import time as t


class Jungle:
    """THERE ARE 9 SNAKES AND 9 LADDERS IN THE JUNGLE, WHOEVER REACHES THE HOME(BOX 100) FIRST WINS THE GAME!!"""
    snakes_coordinates = {99: 12, 91: 7, 85: 31,
                          72: 34, 63: 10, 69: 19, 54: 15, 47: 3, 37: 11}
    ladder_coordinates = {13: 45, 25: 67, 32: 73,
                          49: 93, 57: 83, 60: 88, 70: 98, 89: 94, 90: 97}

    bullet_coordinates = [2, 14, 20, 27, 39, 43, 55, 61, 76, 84, 96]

    MIGHTY_SNAKES_coordinates = [r.choice([11, 12, 13, 14, 15]), r.choice([16, 17, 18, 19, 20]), r.choice([21, 22, 23, 24, 25]), r.choice([26, 27, 28, 29, 30]), r.choice([31, 32, 33, 34, 35]), r.choice([36, 37, 38, 39, 40]), r.choice([41, 42, 43, 44, 45]), r.choice([46, 47, 48, 49, 50]), r.choice(
        [51, 52, 53, 54, 55]), r.choice([56, 57, 58, 59, 60]), r.choice([61, 62, 63, 64, 65]), r.choice([66, 67, 68, 69, 70]), r.choice([71, 72, 73, 74, 75]), r.choice([76, 77, 78, 79, 80]), r.choice([81, 82, 83, 84, 85]), r.choice([86, 87, 88, 89, 90]), r.choice([91, 92, 93, 94, 95]), r.choice([96, 97, 98, 99])]


class Nightmare_Jungle:
    """ In this mode, you will be going alone. There are 20 mighty poisonous snakes, if you encounter any one of them, you die.
    But dont worry, you are given a mighty gun with 2 bullets. So, you have 2 chances to survive. And you can get ressurected only once after death. Can you make it to home? """

    def __init__(self, player) -> None:
        self.player = player

    def survival(self):
        mighty_bullets = 2
        box = 0
        ressurection = True
        win = False
        dice_outcome = 0
        while(box != 100):
            print(f"\nRoll the dice...type 'roll' or hit 'enter' to roll the dice.\n")
            if(input().upper() == "ROLL"):
                dice_outcome = r.choice([1, 2, 3, 4, 5, 6])
            else:
                dice_outcome = r.choice([1, 2, 3, 4, 5, 6])
            print(f"Dice Value = {dice_outcome}")
            box += dice_outcome
            if box > 100:
                box -= dice_outcome
            if box in Jungle.MIGHTY_SNAKES_coordinates:
                print("Oh no, you encountered the giant snake")
                if mighty_bullets != 0:
                    print("Type 'Fire' to kill the giant snake.\n")
                    if(input().upper() == "FIRE"):
                        mighty_bullets -= 1
                        print(
                            f"You killed the giant snake. Wonderful, you have remaining bullets = {mighty_bullets} continue...")
                    else:
                        print("You failed to shoot the giant snake. And sadly he swallows you.")
                        if ressurection is True: 
                            print("Type 'ressurect' to get ressurected")
                            if(input().upper()=="RESSURECT"):
                                box=box+1
                                print(f"You are ressurected in box {box}")
                                ressurection = False
                            else:
                                print("\nYou failed to get ressurected! Unfortunately you remain dead while the snakes devour you!")
                                win=False
                                break
                        else:   
                            win = False
                            break
                else:
                    print(
                        "You do not have any bullets left in your gun. The mighty snake eats you.")
                    if ressurection is True: 
                        print("Type 'ressurect' to get ressurected")
                        if(input().upper()=="RESSURECT"):
                            box=box+1
                            print(f"You are ressurected in box {box}")
                            ressurection = False
                    else:   
                        win = False
                        break
            print(f"You are in Box {box}")
            if box == 100:
                print("You successfully escaped the jungle.")
                win = True
                break
        if win is True:
            print(f"Congratulations {self.player}, you won!")
        else:
            print(
                f"Sorry {self.player}, but now you have become food for the giant snake.")


class Solo_Journey:
    """In this solo journey, you will have limited amount of footsteps. [footsteps=number of chances of throwing dice]
    You will be given a pistol carrying 1 bullet only to save yourself from snakes. You will find bullets
    as you explore the jungle, and it will be picked up automatically. It's also possible that your shotgun breaks due to attack of snake.
    TIPS:

    1. Snakes present below 50 box needs 1 bullets to get killed.
    2. Snakes present above 50 box needs 2 bullets to get killed.
    3. Snakes present above 90 box needs 3 bullets to get killed.

    USE PISTOL WISELY"""

    def __init__(self, player, footsteps, bullets):
        self.player = player
        self.footsteps = footsteps
        self.bullets = bullets
        self.walked_footsteps=0

    def survival(self):
        dice_outcome = 0
        box = 0
        pistol_alive = True
        win = False
        self.bullets = 1
        while(box != 100 or self.footsteps != 0):
            print(f"\nRoll the dice...type 'roll' or hit 'enter' to roll the dice.\n")
            if(input().upper() == "ROLL"):
                dice_outcome = r.choice([1, 2, 3, 4, 5, 6])
            else:
                dice_outcome = r.choice([1, 2, 3, 4, 5, 6])
            print(f"Dice Value = {dice_outcome}")
            box += dice_outcome
            if box > 100:
                box -= dice_outcome
            if box in Jungle.bullet_coordinates:
                self.bullets += 1
                print(
                    f"Wow! You found and picked up a bullet. Now you have {self.bullets} bullets.")
            if box in list(Jungle.snakes_coordinates.keys()):
                print(f"{self.player} encountered a SNAKE")
                if box < 50:
                    chances = [1, 2, 3, 4, 5, 6]
                elif box >= 50 and box < 90:
                    chances = [1, 2, 3, 4]
                else:
                    chances = [1, 2, 3]
                break_pistol = r.choice(chances)
                if(break_pistol == 3):
                    print("The snake broke your pistol")
                    pistol_alive = False
                if pistol_alive is True:
                    if box < 50:
                        if self.bullets >= 1:
                            shoot_bullet = input(
                                "Type 'fire' to shoot the snake or hit enter to do nothing..")
                            if shoot_bullet.upper() == "FIRE":
                                print(f"{self.player} shoots the snake.")
                                print(
                                    f"1 bullet fired on the snake.. bullets left -> {self.bullets-1}")
                                box=box+1
                                print(f"{self.player} is in box {box}")
                                if box == 100:
                                    print(
                                        f"Congratulations! You reached home within {self.footsteps} footsteps!")
                                    win = True
                                    break
                                print(f"You are in box {box}")
                                self.footsteps -= 1
                                self.walked_footsteps+=1
                                print(f"Footsteps Remaining -> {self.footsteps}")
                                continue
                            else:
                                print("You decided to stand still. The snake eats you.")
                        else:
                            print(
                                f"You do not have enough bullets to kill this snake present in box {box}")
                    elif box >= 50 and box < 90:
                        if self.bullets >= 2:
                            shoot_bullet = input(
                                "Type 'fire' to shoot the snake or hit enter to do nothing..")
                            if shoot_bullet.upper() == "FIRE":
                                print(f"{self.player} shoots the snake.")
                                print(
                                    f"2 bullets fired on the snake.. bullets left -> {self.bullets-2}")
                                box=box+1
                                print(f"{self.player} is in box {box}")
                                if box == 100:
                                    print(
                                        f"Congratulations! You reached home within {self.footsteps} footsteps!")
                                    win = True
                                    break
                                print(f"You are in box {box}")
                                self.footsteps -= 1
                                self.walked_footsteps+=1
                                print(f"Footsteps Remaining -> {self.footsteps}")
                                continue
                            else:
                                print("You decided to stand still. The snake eats you.")
                        else:
                            print(
                                f"You do not have enough bullets to kill this snake present in box {box}")
                    else:
                        if self.bullets >= 3:
                            shoot_bullet = input(
                                "Type 'fire' to shoot the snake or hit enter to do nothing..")
                            if shoot_bullet.upper() == "FIRE":
                                print(f"{self.player} shoots the snake.")
                                print(
                                    f"3 bullets fired on the snake.. bullets left -> {self.bullets-3}")
                                box=box+1
                                print(f"{self.player} is in box {box}")
                                if box == 100:
                                    print(
                                        f"Congratulations! You reached home within {self.footsteps} footsteps!")
                                    win = True
                                    break
                                print(f"You are in box {box}")
                                self.footsteps -= 1
                                self.walked_footsteps+=1
                                print(f"Footsteps Remaining -> {self.footsteps}")
                                continue
                            else:
                                print("You decided to stand still. The snake eats you.")
                        else:
                            print(
                                f"You do not have enough bullets to kill this snake present in box {box}")
                for i in Jungle.snakes_coordinates:
                    if i == box:
                        print(
                            f"\n{self.player} was eaten by snake and hence, fell through {i-Jungle.snakes_coordinates[i]} boxes.")
                        box = Jungle.snakes_coordinates[i]
            elif box in list(Jungle.ladder_coordinates.keys()):
                print(f"{self.player} encountered a LADDER")
                for i in Jungle.ladder_coordinates:
                    if i == box:
                        print(
                            f"\n{self.player} climbed the ladder and hence, rose through {Jungle.ladder_coordinates[i]-i} boxes.")
                        box = Jungle.ladder_coordinates[i]
            print(f"{self.player} is in box {box}")
            if box == 100:
                print(
                    f"Congratulations! You reached home within {self.walked_footsteps} footsteps!")
                win = True
                break
            self.footsteps -= 1
            self.walked_footsteps+=1
            print(f"Footsteps Remaining -> {self.footsteps}")
            if(self.footsteps == 0):
                print("Oh no, it seems you lost all your footsteps! And all the snakes in the jungle spotted you and ate you. Game Over!")
                win = False
                break
        t.sleep(2)
        if win is True:
            print(
                f"{self.player} Congratulatons..you have survived the jungle alone!")
        else:
            print(
                f"{self.player} snakes are still eating you...how about trying again?")


class Journey_VsPc:
    def __init__(self, player) -> None:
        self.player = player

    def survival(self):
        dice_outcome = 0
        p1_box = 0
        p2_box = 0
        winner = "NA"
        loser = "NA"
        p2 = "PC"
        while(p1_box != 100 or p2_box != 100):
            print(
                f"\n{self.player} rolls dice...type 'roll' or hit 'enter' to roll the dice.\n")
            if(input().upper() == "ROLL"):
                dice_outcome = r.choice([1, 2, 3, 4, 5, 6])
            else:
                dice_outcome = r.choice([1, 2, 3, 4, 5, 6])
            print(f"Dice Value = {dice_outcome}")
            p1_box += dice_outcome
            if p1_box > 100:
                p1_box -= dice_outcome
            if p1_box in list(Jungle.snakes_coordinates.keys()):
                print(f"{self.player} encountered a SNAKE")
                for i in Jungle.snakes_coordinates:
                    if i == p1_box:
                        print(
                            f"\n{self.player} was eaten by snake and hence, fell through {i-Jungle.snakes_coordinates[i]} boxes.")
                        p1_box = Jungle.snakes_coordinates[i]
            elif p1_box in list(Jungle.ladder_coordinates.keys()):
                print(f"{self.player} encountered a LADDER")
                for i in Jungle.ladder_coordinates:
                    if i == p1_box:
                        print(
                            f"\n{self.player} climbed the ladder and hence, rose through {Jungle.ladder_coordinates[i]-i} boxes.")
                        p1_box = Jungle.ladder_coordinates[i]
            print(f"{self.player} is in box {p1_box}")

            print(f"\n{self.player} -> BOX {p1_box}")
            print(f"{p2} -> BOX {p2_box}")

            if p1_box == 100:
                winner = self.player
                loser = p2
                break

            print(f"\n{p2} rolls dice..\n")
            dice_outcome = r.choice([1, 2, 3, 4, 5, 6])
            print(f"Dice Value = {dice_outcome}")
            p2_box += dice_outcome
            if p2_box > 100:
                p2_box -= dice_outcome
            if p2_box in list(Jungle.snakes_coordinates.keys()):
                print(f"{p2} encountered a SNAKE")
                for i in Jungle.snakes_coordinates:
                    if i == p2_box:
                        print(
                            f"\n{p2} was eaten by snake and hence, fell through {i-Jungle.snakes_coordinates[i]} boxes.")
                        p2_box = Jungle.snakes_coordinates[i]
            elif p2_box in list(Jungle.ladder_coordinates.keys()):
                print(f"{p2} encountered a LADDER")
                for i in Jungle.ladder_coordinates:
                    if i == p2_box:
                        print(
                            f"\n{p2} climbed the ladder and hence, rose through {Jungle.ladder_coordinates[i]-i} boxes.")
                        p2_box = Jungle.ladder_coordinates[i]
            print(f"{p2} is in box {p2_box}")
            print(f"\n{self.player} -> BOX {p1_box}")
            print(f"{p2} -> BOX {p2_box}")
            if p2_box == 100:
                winner = p2
                loser = self.player
                break
        print(f"{winner} reaches home! {loser} gets eaten by snakes!")


class Journey_2P:
    def __init__(self, p1, p2) -> None:
        self.p1 = p1
        self.p2 = p2

    def survival(self):
        dice_outcome = 0
        p1_box = 0
        p2_box = 0
        winner = "NA"
        loser = "NA"
        while(p1_box != 100 or p2_box != 100):
            print(
                f"\n{self.p1} rolls dice...type 'roll' or hit 'enter' to roll the dice.\n")
            if(input().upper() == "ROLL"):
                dice_outcome = r.choice([1, 2, 3, 4, 5, 6])
            else:
                dice_outcome = r.choice([1, 2, 3, 4, 5, 6])
            print(f"Dice Value = {dice_outcome}")
            p1_box += dice_outcome
            if p1_box > 100:
                p1_box -= dice_outcome
            if p1_box in list(Jungle.snakes_coordinates.keys()):
                print(f"{self.p1} encountered a SNAKE")
                for i in Jungle.snakes_coordinates:
                    if i == p1_box:
                        print(
                            f"\n{self.p1} was eaten by snake and hence, fell through {i-Jungle.snakes_coordinates[i]} boxes.")
                        p1_box = Jungle.snakes_coordinates[i]
            elif p1_box in list(Jungle.ladder_coordinates.keys()):
                print(f"{self.p1} encountered a LADDER")
                for i in Jungle.ladder_coordinates:
                    if i == p1_box:
                        print(
                            f"\n{self.p1} climbed the ladder and hence, rose through {Jungle.ladder_coordinates[i]-i} boxes.")
                        p1_box = Jungle.ladder_coordinates[i]
            print(f"{self.p1} is in box {p1_box}")

            print(f"\n{self.p1} -> BOX {p1_box}")
            print(f"{self.p2} -> BOX {p2_box}")

            if p1_box == 100:
                winner = self.p1
                loser = self.p2
                break

            print(f"\n{self.p2} rolls dice...type 'roll' to roll the dice.\n")
            if(input().upper() == "ROLL"):
                dice_outcome = r.choice([1, 2, 3, 4, 5, 6])
            else:
                dice_outcome = r.choice([1, 2, 3, 4, 5, 6])
            print(f"Dice Value = {dice_outcome}")
            p2_box += dice_outcome
            if p2_box > 100:
                p2_box -= dice_outcome
            if p2_box in list(Jungle.snakes_coordinates.keys()):
                print(f"{self.p2} encountered a SNAKE")
                for i in Jungle.snakes_coordinates:
                    if i == p2_box:
                        print(
                            f"\n{p2} was eaten by snake and hence, fell through {i-Jungle.snakes_coordinates[i]} boxes.")
                        p2_box = Jungle.snakes_coordinates[i]
            elif p2_box in list(Jungle.ladder_coordinates.keys()):
                print(f"{self.p2} encountered a LADDER")
                for i in Jungle.ladder_coordinates:
                    if i == p2_box:
                        print(
                            f"\n{p2} climbed the ladder and hence, rose through {Jungle.ladder_coordinates[i]-i} boxes.")
                        p2_box = Jungle.ladder_coordinates[i]
            print(f"{self.p2} is in box {p2_box}")
            print(f"\n{self.p1} -> BOX {p1_box}")
            print(f"{self.p2} -> BOX {p2_box}")
            if p2_box == 100:
                winner = self.p2
                loser = self.p1
                break
        print(f"{winner} reaches home! {loser} gets eaten by snakes!")


class Journey_3P:
    def __init__(self, p1, p2, p3) -> None:
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def survival(self):
        dice_outcome = 0
        p1_box = 0
        p2_box = 0
        p3_box = 0
        winner = "NA"
        loser1 = "NA"
        loser2 = "NA"
        while(p1_box != 100 or p2_box != 100 or p3_box != 100):
            print(
                f"\n{self.p1} rolls dice...type 'roll' or hit 'enter' to roll the dice.\n")
            if(input().upper() == "ROLL"):
                dice_outcome = r.choice([1, 2, 3, 4, 5, 6])
            else:
                dice_outcome = r.choice([1, 2, 3, 4, 5, 6])
            print(f"Dice Value = {dice_outcome}")
            p1_box += dice_outcome
            if p1_box > 100:
                p1_box -= dice_outcome
            if p1_box in list(Jungle.snakes_coordinates.keys()):
                print(f"{self.p1} encountered a SNAKE")
                for i in Jungle.snakes_coordinates:
                    if i == p1_box:
                        print(
                            f"\n{self.p1} was eaten by snake and hence, fell through {i-Jungle.snakes_coordinates[i]} boxes.")
                        p1_box = Jungle.snakes_coordinates[i]
            elif p1_box in list(Jungle.ladder_coordinates.keys()):
                print(f"{self.p1} encountered a LADDER")
                for i in Jungle.ladder_coordinates:
                    if i == p1_box:
                        print(
                            f"\n{self.p1} climbed the ladder and hence, rose through {Jungle.ladder_coordinates[i]-i} boxes.")
                        p1_box = Jungle.ladder_coordinates[i]
            print(f"{self.p1} is in box {p1_box}")

            print(f"\n{self.p1} -> BOX {p1_box}")
            print(f"{self.p2} -> BOX {p2_box}")
            print(f"{self.p3} -> BOX {p3_box}")

            if p1_box == 100:
                winner = self.p1
                loser1 = self.p2
                loser2 = self.p3
                break

            print(f"\n{self.p2} rolls dice...type 'roll' to roll the dice.\n")
            if(input().upper() == "ROLL"):
                dice_outcome = r.choice([1, 2, 3, 4, 5, 6])
            else:
                dice_outcome = r.choice([1, 2, 3, 4, 5, 6])
            print(f"Dice Value = {dice_outcome}")
            p2_box += dice_outcome
            if p2_box > 100:
                p2_box -= dice_outcome
            if p2_box in list(Jungle.snakes_coordinates.keys()):
                print(f"{self.p2} encountered a SNAKE")
                for i in Jungle.snakes_coordinates:
                    if i == p2_box:
                        print(
                            f"\n{self.p2} was eaten by snake and hence, fell through {i-Jungle.snakes_coordinates[i]} boxes.")
                        p2_box = Jungle.snakes_coordinates[i]
            elif p2_box in list(Jungle.ladder_coordinates.keys()):
                print(f"{self.p2} encountered a LADDER")
                for i in Jungle.ladder_coordinates:
                    if i == p2_box:
                        print(
                            f"\n{self.p2} climbed the ladder and hence, rose through {Jungle.ladder_coordinates[i]-i} boxes.")
                        p2_box = Jungle.ladder_coordinates[i]
            print(f"{self.p2} is in box {p2_box}")
            print(f"\n{self.p1} -> BOX {p1_box}")
            print(f"{self.p2} -> BOX {p2_box}")
            print(f"{self.p3} -> BOX {p3_box}")
            if p2_box == 100:
                winner = self.p2
                loser1 = self.p1
                loser2 = self.p3
                break

            print(f"\n{self.p3} rolls dice...type 'roll' to roll the dice.\n")
            if(input().upper() == "ROLL"):
                dice_outcome = r.choice([1, 2, 3, 4, 5, 6])
            else:
                dice_outcome = r.choice([1, 2, 3, 4, 5, 6])
            print(f"Dice Value = {dice_outcome}")
            p3_box += dice_outcome
            if p3_box > 100:
                p3_box -= dice_outcome
            if p3_box in list(Jungle.snakes_coordinates.keys()):
                print(f"{self.p3} encountered a SNAKE")
                for i in Jungle.snakes_coordinates:
                    if i == p3_box:
                        print(
                            f"\n{self.p3} was eaten by snake and hence, fell through {i-Jungle.snakes_coordinates[i]} boxes.")
                        p3_box = Jungle.snakes_coordinates[i]
            elif p3_box in list(Jungle.ladder_coordinates.keys()):
                print(f"{self.p3} encountered a LADDER")
                for i in Jungle.ladder_coordinates:
                    if i == p3_box:
                        print(
                            f"\n{self.p3} climbed the ladder and hence, rose through {Jungle.ladder_coordinates[i]-i} boxes.")
                        p2_box = Jungle.ladder_coordinates[i]
            print(f"{self.p3} is in box {p3_box}")
            print(f"\n{self.p1} -> BOX {p1_box}")
            print(f"{self.p2} -> BOX {p2_box}")
            print(f"{self.p3} -> BOX {p3_box}")
            if p3_box == 100:
                winner = self.p3
                loser1 = self.p1
                loser2 = self.p2
                break
        print(f"{winner} reaches home! {loser1} and {loser2} gets eaten by snakes!")


class Journey_4P:
    def __init__(self, p1, p2, p3, p4) -> None:
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

    def survival(self):
        dice_outcome = 0
        p1_box = 0
        p2_box = 0
        p3_box = 0
        p4_box = 0
        winner = "NA"
        loser1 = "NA"
        loser2 = "NA"
        loser3 = "NA"
        while(p1_box != 100 or p2_box != 100 or p3_box != 100 or p4_box != 100):
            print(
                f"\n{self.p1} rolls dice...type 'roll' or hit 'enter' to roll the dice.\n")
            if(input().upper() == "ROLL"):
                dice_outcome = r.choice([1, 2, 3, 4, 5, 6])
            else:
                dice_outcome = r.choice([1, 2, 3, 4, 5, 6])
            print(f"Dice Value = {dice_outcome}")
            p1_box += dice_outcome
            if p1_box > 100:
                p1_box -= dice_outcome
            if p1_box in list(Jungle.snakes_coordinates.keys()):
                print(f"{self.p1} encountered a SNAKE")
                for i in Jungle.snakes_coordinates:
                    if i == p1_box:
                        print(
                            f"\n{self.p1} was eaten by snake and hence, fell through {i-Jungle.snakes_coordinates[i]} boxes.")
                        p1_box = Jungle.snakes_coordinates[i]
            elif p1_box in list(Jungle.ladder_coordinates.keys()):
                print(f"{self.p1} encountered a LADDER")
                for i in Jungle.ladder_coordinates:
                    if i == p1_box:
                        print(
                            f"\n{self.p1} climbed the ladder and hence, rose through {Jungle.ladder_coordinates[i]-i} boxes.")
                        p1_box = Jungle.ladder_coordinates[i]
            print(f"{self.p1} is in box {p1_box}")

            print(f"\n{self.p1} -> BOX {p1_box}")
            print(f"{self.p2} -> BOX {p2_box}")
            print(f"{self.p3} -> BOX {p3_box}")
            print(f"{self.p4} -> BOX {p4_box}")

            if p1_box == 100:
                winner = self.p1
                loser1 = self.p2
                loser2 = self.p3
                loser3 = self.p4
                break

            print(f"\n{self.p2} rolls dice...type 'roll' to roll the dice.\n")
            if(input().upper() == "ROLL"):
                dice_outcome = r.choice([1, 2, 3, 4, 5, 6])
            else:
                dice_outcome = r.choice([1, 2, 3, 4, 5, 6])
            print(f"Dice Value = {dice_outcome}")
            p2_box += dice_outcome
            if p2_box > 100:
                p2_box -= dice_outcome
            if p2_box in list(Jungle.snakes_coordinates.keys()):
                print(f"{self.p2} encountered a SNAKE")
                for i in Jungle.snakes_coordinates:
                    if i == p2_box:
                        print(
                            f"\n{self.p2} was eaten by snake and hence, fell through {i-Jungle.snakes_coordinates[i]} boxes.")
                        p2_box = Jungle.snakes_coordinates[i]
            elif p2_box in list(Jungle.ladder_coordinates.keys()):
                print(f"{self.p2} encountered a LADDER")
                for i in Jungle.ladder_coordinates:
                    if i == p2_box:
                        print(
                            f"\n{self.p2} climbed the ladder and hence, rose through {Jungle.ladder_coordinates[i]-i} boxes.")
                        p2_box = Jungle.ladder_coordinates[i]
            print(f"{self.p2} is in box {p2_box}")
            print(f"\n{self.p1} -> BOX {p1_box}")
            print(f"{self.p2} -> BOX {p2_box}")
            print(f"{self.p3} -> BOX {p3_box}")
            print(f"{self.p4} -> BOX {p4_box}")
            if p2_box == 100:
                winner = self.p2
                loser1 = self.p1
                loser2 = self.p3
                loser3 = self.p4
                break

            print(f"\n{self.p3} rolls dice...type 'roll' to roll the dice.\n")
            if(input().upper() == "ROLL"):
                dice_outcome = r.choice([1, 2, 3, 4, 5, 6])
            else:
                dice_outcome = r.choice([1, 2, 3, 4, 5, 6])
            print(f"Dice Value = {dice_outcome}")
            p3_box += dice_outcome
            if p3_box > 100:
                p3_box -= dice_outcome
            if p3_box in list(Jungle.snakes_coordinates.keys()):
                print(f"{self.p3} encountered a SNAKE")
                for i in Jungle.snakes_coordinates:
                    if i == p3_box:
                        print(
                            f"\n{self.p3} was eaten by snake and hence, fell through {i-Jungle.snakes_coordinates[i]} boxes.")
                        p3_box = Jungle.snakes_coordinates[i]
            elif p3_box in list(Jungle.ladder_coordinates.keys()):
                print(f"{self.p3} encountered a LADDER")
                for i in Jungle.ladder_coordinates:
                    if i == p3_box:
                        print(
                            f"\n{self.p3} climbed the ladder and hence, rose through {Jungle.ladder_coordinates[i]-i} boxes.")
                        p3_box = Jungle.ladder_coordinates[i]
            print(f"{self.p3} is in box {p3_box}")
            print(f"\n{self.p1} -> BOX {p1_box}")
            print(f"{self.p2} -> BOX {p2_box}")
            print(f"{self.p3} -> BOX {p3_box}")
            print(f"{self.p4} -> BOX {p4_box}")
            if p3_box == 100:
                winner = self.p3
                loser1 = self.p1
                loser2 = self.p2
                loser3 = self.p4
                break

            print(f"\n{self.p4} rolls dice...type 'roll' to roll the dice.\n")
            if(input().upper() == "ROLL"):
                dice_outcome = r.choice([1, 2, 3, 4, 5, 6])
            else:
                dice_outcome = r.choice([1, 2, 3, 4, 5, 6])
            print(f"Dice Value = {dice_outcome}")
            p4_box += dice_outcome
            if p4_box > 100:
                p4_box -= dice_outcome
            if p4_box in list(Jungle.snakes_coordinates.keys()):
                print(f"{self.p4} encountered a SNAKE")
                for i in Jungle.snakes_coordinates:
                    if i == p4_box:
                        print(
                            f"\n{self.p4} was eaten by snake and hence, fell through {i-Jungle.snakes_coordinates[i]} boxes.")
                        p4_box = Jungle.snakes_coordinates[i]
            elif p4_box in list(Jungle.ladder_coordinates.keys()):
                print(f"{self.p4} encountered a LADDER")
                for i in Jungle.ladder_coordinates:
                    if i == p4_box:
                        print(
                            f"\n{self.p4} climbed the ladder and hence, rose through {Jungle.ladder_coordinates[i]-i} boxes.")
                        p4_box = Jungle.ladder_coordinates[i]
            print(f"{self.p4} is in box {p4_box}")
            print(f"\n{self.p1} -> BOX {p1_box}")
            print(f"{self.p2} -> BOX {p2_box}")
            print(f"{self.p3} -> BOX {p3_box}")
            print(f"{self.p4} -> BOX {p4_box}")
            if p4_box == 100:
                winner = self.p4
                loser1 = self.p1
                loser2 = self.p2
                loser3 = self.p3
                break
        print(
            f"{winner} reaches home! {loser1} and {loser2} and {loser3} gets eaten by snakes!")


if __name__ == "__main__":
    print("SNAKES AND LADDERS\n\n")
    print("1. Vs Computer")
    print("2. 2 Players")
    print("3. 3 Players")
    print("4. 4 Players")
    print("5. Solo Journey [SPECIAL MODE]")
    print("6. Nightmare Jungle [SPECIAL MODE] ")
    choice = input("Enter choice(1-5): ")
    if choice == "1":
        player = input("Enter your name: ")
        print(f"\n\nWELCOME TO THE JUNGLE! {Jungle.__doc__} ")
        Go = Journey_VsPc(player)
        Go.survival()
    elif choice == "2":
        p1 = input("Enter Player 1 name: ")
        p2 = input("Enter Player 2 name: ")
        print(f"\n\nWELCOME TO THE JUNGLE! {Jungle.__doc__} ")
        Go = Journey_2P(p1, p2)
        Go.survival()
    elif choice == "3":
        p1 = input("Enter Player 1 name: ")
        p2 = input("Enter Player 2 name: ")
        p3 = input("Enter Player 3 name: ")
        print(f"\n\nWELCOME TO THE JUNGLE! {Jungle.__doc__} ")
        Go = Journey_3P(p1, p2, p3)
        Go.survival()
    elif choice == "4":
        p1 = input("Enter Player 1 name: ")
        p2 = input("Enter Player 2 name: ")
        p3 = input("Enter Player 3 name: ")
        p4 = input("Enter Player 4 name: ")
        print(f"\n\nWELCOME TO THE JUNGLE! {Jungle.__doc__} ")
        Go = Journey_4P(p1, p2, p3, p4)
        Go.survival()
    elif choice == "5":
        footsteps = 0
        player = input("Enter Your Name:")
        print(f"\nWelcome to Special Mode. {Solo_Journey.__doc__}")
        print(
            "Please select difficulty level:\n1.Easy [FOOTSTEPS -> 50]\n2. Medium [FOOTSTEPS -> 30]\n3. Hard [FOOTSTEPS -> 15]\n4. Leave on fate [FOOTSTEPS -> UNKNOWN]")
        sub_choice = int(input())
        if sub_choice == 1:
            footsteps = 50
            Go = Solo_Journey(player, footsteps, 1)
            Go.survival()
        elif sub_choice == 2:
            footsteps = 30
            Go = Solo_Journey(player, footsteps, 1)
            Go.survival()
        elif sub_choice == 3:
            footsteps = 15
            Go = Solo_Journey(player, footsteps, 1)
            Go.survival()
        elif sub_choice == 4:
            footsteps = r.choice([30, 75, 50])
            print(f"You have {footsteps} footsteps available.")
            Go = Solo_Journey(player, footsteps, 1)
            Go.survival()
    elif choice == "6":
        player = input("Enter your name:")
        print(
            f"\nWelcome to Nightmare Jungle Mode. {Nightmare_Jungle.__doc__}")
        Go = Nightmare_Jungle(player)
        Go.survival()