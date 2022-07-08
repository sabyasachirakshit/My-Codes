import random
import time
character = input(
    "Choose Yor Character\n1.Alex Mercer[PROTOTYPE] [FAST LIKE BLADE,DEADLY IN ATTACK]\n2.James Heller[PROTOTYPE 2] [AGGRESSIVE IN COMBAT,TOUGH AS MOUNTAIN]\nWhich character you choose(1-2):")
if character == '1':
    print("You have chosen Alex Mercer from Prototype")
    print("\nPutting Mercer on War Zone..Please Wait..")
    print("0%...")
    time.sleep(5)
    print("30%...")
    time.sleep(8)
    print("70%...")
    time.sleep(3)
    print("100%...")
    time.sleep(1)
    print("Alex Mercer has landed successfully on the War Zone.\n\n")
    player = "Mercer"
elif character == '2':
    print("You have chosen James Heller from Prototype 2")
    print("\nPutting Heller on War Zone..Please Wait..")
    print("0%...")
    time.sleep(5)
    print("30%...")
    time.sleep(8)
    print("70%...")
    time.sleep(3)
    print("100%...")
    time.sleep(1)
    print("James Heller has landed successfully on the War Zone.\n\n")
    player = "Heller"
demon_list = [1, 2, 3, 4, 5]
demon_spawn = random.choice(demon_list)
demon_life = 100
hero_life = 100
hero_stamina = 100
time.sleep(2)
DEMON_APPEARANCE = f"Level {demon_spawn} demon has appeared!"
if demon_spawn == 1:
    print(DEMON_APPEARANCE)
elif demon_spawn == 2:
    print(DEMON_APPEARANCE)
elif demon_spawn == 3:
    print(DEMON_APPEARANCE)
elif demon_spawn == 4:
    print(DEMON_APPEARANCE)
elif demon_spawn == 5:
    print(DEMON_APPEARANCE)
print("\n")
time.sleep(3)
hero_power = int(input(
    "Choose Powerup\n1.Whip Fist\n2.Hammer Fist\n3.Blade Claws\n4.Tendrils Attack\nChoose(1-4):"))
if hero_power == 1:
    hero_weapon = "Whip Fist"
elif hero_power == 2:
    hero_weapon = "Hammer Fist"
elif hero_power == 3:
    hero_weapon = "Blade Claws"
elif hero_power == 4:
    hero_weapon = "Tendrils"
else:
    hero_weapon = "Whip Fist"
arm = input("Wear Body Armor(y/n):")
if arm == 'y' or arm == 'Y':
    body_armor = True
else:
    body_armor = False
print(f"Level {demon_spawn} demon and {player} face each other..!\n\n")
print("Battle Starts in 3....")
time.sleep(1)
print("Battle Starts in 2....")
time.sleep(1)
print("Battle Starts in 1....")
time.sleep(1)
print("BATTLE STARTS!")
round = 1
while True:
    time.sleep(3)
    print(f"\n\n~~~~~~~~~~~~~~~~~~~~~~~~~ROUND {round}~~~~~~~~~~~~~~~~")
    print(f"Demon's Life -> {demon_life}")
    print(f"{player}'s Life -> {hero_life}  ; {player}'s Stamina -> {hero_stamina}")
    print(
        f"\n\n----------------------------{player}'s TURN---------------------")
    option = int(input(("1.Normal Attack\n2.Heavy Attack\n3.Devastating Attack(only used if stamina>80)\n4.Consume Zombies to increase Health And Stamina\nEnter Choice(1-4):")))
    if option == 1:
        normal_damage = [5, 6, 7, 8, 9, 10]
        normal_damage_dealt = random.choice(normal_damage)
        demon_life -= normal_damage_dealt
        time.sleep(3)
        print(
            f"\nLevel {demon_spawn} demon dealt a normal {hero_weapon} attack damage of {normal_damage_dealt}+ points.")
    elif option == 2:
        heavy_damage = [15, 16, 17, 18, 19, 20]
        heavy_damage_dealt = random.choice(heavy_damage)
        demon_life -= heavy_damage_dealt
        time.sleep(3)
        print(
            f"Level {demon_spawn} demon dealt a heavy {hero_weapon} attack damage of {heavy_damage_dealt}+ points.")
    elif option == 3:
        if hero_stamina > 80:
            devastating_attack_damage = [30, 35, 40]
            devastating_attack_dealt = random.choice(devastating_attack_damage)
            demon_life -= devastating_attack_dealt
            hero_stamina_lose = [5, 10]
            hero_stamina_lost = random.choice(hero_stamina_lose)
            hero_stamina -= hero_stamina_lost
            time.sleep(3)
            print(f"Level {demon_spawn} demon dealt a devastating attack damage of {devastating_attack_dealt}+ points and {player} lost {hero_stamina_lost}- stamina points.")
        else:
            time.sleep(3)
            print("Stamina not enough to use devastating attack! Attack Failed!")
    elif option == 4:
        zombie_health = [10, 15, 20]
        zombie_health_consumed = random.choice(zombie_health)
        zombie_stamina = [5, 6, 7, 8, 9, 10]
        zombie_stamina_consumed = random.choice(zombie_stamina)
        hero_life += zombie_health_consumed
        hero_stamina += zombie_stamina_consumed
        time.sleep(3)
        if hero_life > 100:
            hero_life = 100
        if hero_stamina > 100:
            hero_stamina = 100
        print(f"{player}'s health increased by {zombie_health_consumed}+ points!")
        print(f"{player}'s stamina increased by {zombie_stamina_consumed}+ points!")
    else:
        time.sleep(3)
        print("Invalid Move! Turn Wasted!")
    time.sleep(3)
    if demon_life <= 0:
        print(
            f"\n{player} HEALTH LEFT--->{hero_life}\nLevel {demon_spawn} Demon's HEALTH LEFT--->{demon_life}")
        HERO_WIN = 1
        DEMON_WIN = 0
        break
    print("\n----------------------------DEMON's TURN---------------------")
    if demon_spawn == 1:
        hero_damage_dealt_with_armor_on = [2, 3, 4, 5]
        hero_damage_dealt_with_armor_off = [6, 7, 8, 9, 10]
        stamina_attack_probability = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        stamina_attacked_by_demon = random.choice(stamina_attack_probability)
        if body_armor is True:
            demon_attacked_damage = random.choice(
                hero_damage_dealt_with_armor_on)
        else:
            demon_attacked_damage = random.choice(
                hero_damage_dealt_with_armor_off)
        hero_life -= demon_attacked_damage
        time.sleep(3)
        print(f"{player} dealt a health damage from Level {demon_spawn} demon of {demon_attacked_damage}+ points")
        if stamina_attacked_by_demon >= 8:
            hero_stamina -= 10
            time.sleep(3)
            print(
                f"{player} dealt a stamina damage from Level {demon_spawn} demon of {stamina_attacked_by_demon}+ points")
        probability_of_increasing_demons_life = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        chances_of_increasing_life = random.choice(
            probability_of_increasing_demons_life)
        if chances_of_increasing_life >= 8:
            demon_life += 5
            time.sleep(3)
            if demon_life > 100:
                demon_life = 100
            print(
                f"Level {demon_spawn} demon increased his own health by 5+ points")
    elif demon_spawn == 2:
        hero_damage_dealt_with_armor_on = [10, 11, 12, 13, 14, 15]
        hero_damage_dealt_with_armor_off = [16, 17, 18, 19, 20]
        stamina_attack_probability = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        stamina_attacked_by_demon = random.choice(stamina_attack_probability)
        if body_armor is True:
            demon_attacked_damage = random.choice(
                hero_damage_dealt_with_armor_on)
        else:
            demon_attacked_damage = random.choice(
                hero_damage_dealt_with_armor_off)
        hero_life -= demon_attacked_damage
        time.sleep(3)
        print(f"{player} dealt a health damage from Level {demon_spawn} demon of {demon_attacked_damage}+ points")
        if stamina_attacked_by_demon >= 7:
            hero_stamina -= 10
            time.sleep(3)
            print(
                f"{player} dealt a stamina damage from Level {demon_spawn} demon of {stamina_attacked_by_demon}+ points")
        probability_of_increasing_demons_life = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        chances_of_increasing_life = random.choice(
            probability_of_increasing_demons_life)
        if chances_of_increasing_life >= 7:
            demon_life += 10
            time.sleep(3)
            if demon_life > 100:
                demon_life = 100
            print(
                f"Level {demon_spawn} demon increased his own health by 10+ points")
    elif demon_spawn == 3:
        hero_damage_dealt_with_armor_on = [16, 17, 18, 19, 20]
        hero_damage_dealt_with_armor_off = [21, 22, 23, 24, 25]
        stamina_attack_probability = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        stamina_attacked_by_demon = random.choice(stamina_attack_probability)
        if body_armor is True:
            demon_attacked_damage = random.choice(
                hero_damage_dealt_with_armor_on)
        else:
            demon_attacked_damage = random.choice(
                hero_damage_dealt_with_armor_off)
        hero_life -= demon_attacked_damage
        time.sleep(3)
        print(f"{player} dealt a health damage from Level {demon_spawn} demon of {demon_attacked_damage}+ points")
        if stamina_attacked_by_demon >= 6:
            hero_stamina -= 10
            time.sleep(3)
            print(
                f"{player} dealt a stamina damage from Level {demon_spawn} demon of {stamina_attacked_by_demon}+ points")
        probability_of_increasing_demons_life = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        chances_of_increasing_life = random.choice(
            probability_of_increasing_demons_life)
        if chances_of_increasing_life >= 7:
            demon_life += 15
            time.sleep(3)
            if demon_life > 100:
                demon_life = 100
            print(
                f"Level {demon_spawn} demon increased his own health by 15+ points")
    elif demon_spawn == 4:
        hero_damage_dealt_with_armor_on = [21, 22, 23, 24, 25]
        hero_damage_dealt_with_armor_off = [26, 27, 28, 29, 30]
        stamina_attack_probability = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        stamina_attacked_by_demon = random.choice(stamina_attack_probability)
        if body_armor is True:
            demon_attacked_damage = random.choice(
                hero_damage_dealt_with_armor_on)
        else:
            demon_attacked_damage = random.choice(
                hero_damage_dealt_with_armor_off)
        hero_life -= demon_attacked_damage
        time.sleep(3)
        print(f"{player} dealt a health damage from Level {demon_spawn} demon of {demon_attacked_damage}+ points")
        if stamina_attacked_by_demon >= 5:
            hero_stamina -= 10
            time.sleep(3)
            print(
                f"{player} dealt a stamina damage from Level {demon_spawn} demon of {stamina_attacked_by_demon}+ points")
        probability_of_increasing_demons_life = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        chances_of_increasing_life = random.choice(
            probability_of_increasing_demons_life)
        if chances_of_increasing_life >= 6:
            demon_life += 20
            time.sleep(3)
            if demon_life > 100:
                demon_life = 100
            print(
                f"Level {demon_spawn} demon increased his own health by 20+ points")
    else:
        hero_damage_dealt_with_armor_on = [26, 27, 28, 29, 30]
        hero_damage_dealt_with_armor_off = [31, 32, 33, 34, 35]
        stamina_attack_probability = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        stamina_attacked_by_demon = random.choice(stamina_attack_probability)
        if body_armor is True:
            demon_attacked_damage = random.choice(
                hero_damage_dealt_with_armor_on)
        else:
            demon_attacked_damage = random.choice(
                hero_damage_dealt_with_armor_off)
        hero_life -= demon_attacked_damage
        time.sleep(3)
        print(f"{player} dealt a health damage from Level {demon_spawn} demon of {demon_attacked_damage}+ points")
        if stamina_attacked_by_demon >= 4:
            hero_stamina -= 10
            time.sleep(3)
            print(
                f"{player} dealt a stamina damage from Level {demon_spawn} demon of {stamina_attacked_by_demon}+ points")
        probability_of_increasing_demons_life = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        chances_of_increasing_life = random.choice(
            probability_of_increasing_demons_life)
        if chances_of_increasing_life >= 5:
            demon_life += 25
            time.sleep(3)
            if demon_life > 100:
                demon_life = 100
            print(
                f"Level {demon_spawn} demon increased his own health by 25+ points")
    time.sleep(3)
    print(f"\n{player} HEALTH LEFT--->{hero_life}\nLevel {demon_spawn} Demon's HEALTH LEFT--->{demon_life}")
    if hero_life <= 0:
        DEMON_WIN = 1
        HERO_WIN = 0
        break
    elif demon_life <= 0:
        HERO_WIN = 1
        DEMON_WIN = 0
        break
    round += 1
if DEMON_WIN == 1:
    time.sleep(3)
    print(
        f"\nLevel {demon_spawn} Demon Defeated {player} within {round} rounds.")
if HERO_WIN == 1:
    time.sleep(3)
    print(f"\n{player} Defeated Level {demon_spawn} Demon within {round} rounds.")
print("\nGAME OVER")
