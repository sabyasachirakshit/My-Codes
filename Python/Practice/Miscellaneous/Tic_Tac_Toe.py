pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9 = " ", " ", " ", " ", " ", " ", " ", " ", " "


def game_board(pos, ps):
    global pos1
    global pos2
    global pos3
    global pos4
    global pos5
    global pos6
    global pos7
    global pos8
    global pos9
    if pos == 1 and pos1 == " ":
        if ps == "X":
            pos1 = "X"
        else:
            pos1 = "O"
    if pos == 2 and pos2 == " ":
        if ps == "X":
            pos2 = "X"
        else:
            pos2 = "O"
    if pos == 3 and pos3 == " ":
        if ps == "X":
            pos3 = "X"
        else:
            pos3 = "O"
    if pos == 4 and pos4 == " ":
        if ps == "X":
            pos4 = "X"
        else:
            pos4 = "O"
    if pos == 5 and pos5 == " ":
        if ps == "X":
            pos5 = "X"
        else:
            pos5 = "O"
    if pos == 6 and pos6 == " ":
        if ps == "X":
            pos6 = "X"
        else:
            pos6 = "O"
    if pos == 7 and pos7 == " ":
        if ps == "X":
            pos7 = "X"
        else:
            pos7 = "O"
    if pos == 8 and pos8 == " ":
        if ps == "X":
            pos8 = "X"
        else:
            pos8 = "O"
    if pos == 9 and pos9 == " ":
        if ps == "X":
            pos9 = "X"
        else:
            pos9 = "O"

    print("\t\t\t\t\t\t|\t|\t\t")
    print(f"\t\t\t\t\t    {pos1}   |   {pos2}   |   {pos3}")
    print(f"\t\t\t\t\t\t|\t|\t\t")
    print(f"\t\t\t\t\t------------------------")
    print(f"\t\t\t\t\t\t|\t|\t\t")
    print(f"\t\t\t\t\t    {pos4}   |   {pos5}   |   {pos6}")
    print(f"\t\t\t\t\t\t|\t|\t\t")
    print(f"\t\t\t\t\t------------------------")
    print(f"\t\t\t\t\t\t|\t|\t\t")
    print(f"\t\t\t\t\t    {pos7}   |   {pos8}   |   {pos9}")
    print(f"\t\t\t\t\t\t|\t|\t\t")
    if pos1 != " " and pos2 != " " and pos3 != " " and pos4 != " " and pos5 != " " and pos6 != " " and pos7 != " " and pos8 != " " and pos9 != " ":
        winner = "Tie"
        return winner
    elif pos1 == "X" and pos2 == "X" and pos3 == "X":
        winner = "X"
        return winner
    elif pos1 == "O" and pos2 == "O" and pos3 == "O":
        winner = "O"
        return winner
    elif pos1 == "X" and pos4 == "X" and pos7 == "X":
        winner = "X"
        return winner
    elif pos1 == "O" and pos4 == "O" and pos7 == "O":
        winner = "O"
        return winner
    elif pos1 == "X" and pos5 == "X" and pos9 == "X":
        winner = "X"
        return winner
    elif pos1 == "O" and pos5 == "O" and pos9 == "O":
        winner = "O"
        return winner
    elif pos2 == "X" and pos5 == "X" and pos8 == "X":
        winner = "X"
        return winner
    elif pos2 == "O" and pos5 == "O" and pos8 == "O":
        winner = "O"
        return winner
    elif pos3 == "X" and pos6 == "X" and pos9 == "X":
        winner = "X"
        return winner
    elif pos3 == "O" and pos6 == "O" and pos9 == "O":
        winner = "O"
        return winner
    elif pos3 == "X" and pos5 == "X" and pos8 == "X":
        winner = "X"
        return winner
    elif pos3 == "O" and pos5 == "O" and pos8 == "O":
        winner = "O"
        return winner
    elif pos4 == "X" and pos5 == "X" and pos6 == "X":
        winner = "X"
        return winner
    elif pos4 == "O" and pos5 == "O" and pos6 == "O":
        winner = "O"
        return winner
    elif pos7 == "X" and pos8 == "X" and pos9 == "X":
        winner = "X"
        return winner
    elif pos7 == "O" and pos8 == "O" and pos9 == "O":
        winner = "O"
        return winner


print("\t\t\t\t   ~~~~WELCOME TO TIC TAC TOE GAME!~~~~")
print("\n\nInstructions-> This is the following board structure. Place your marker(X/O) using numbers (1-9) according to given position.")
print("\t\t\t\t\t\t|\t|\t\t")
print("\t\t\t\t\t    1   |   2   |   3")
print("\t\t\t\t\t\t|\t|\t\t")
print("\t\t\t\t\t------------------------")
print("\t\t\t\t\t\t|\t|\t\t")
print("\t\t\t\t\t    4   |   5   |   6")
print("\t\t\t\t\t\t|\t|\t\t")
print("\t\t\t\t\t------------------------")
print("\t\t\t\t\t\t|\t|\t\t")
print("\t\t\t\t\t    7   |   8   |   9")
print("\t\t\t\t\t\t|\t|\t\t")
player1 = input("\nEnter Player1 name: ")
player2 = input("Enter Player2 name: ")
p1c = input(f"\nEnter {player1} choice (O or X): ")
p1c = p1c.title()
if p1c == 'O':
    p2c = 'X'
else:
    p2c = 'O'
print(f"\n{player1}'s choice is {p1c}")
print(f"{player2}'s choice is {p2c}")
game_board(None, None)
winner = ""
e = 1
while winner != "Tie":
    pos = int(input(f"\n{player1} choose position to put {p1c}: "))
    winner = game_board(pos, p1c)
    if winner == "Tie":
        break
    if winner == "X" and p1c == "X":
        print(f"\n{player1} won!")
        exit()
    elif winner == "X" and p2c == "X":
        print(f"\n{player2} won!")
        exit()
    elif winner == "O" and p1c == "O":
        print(f"\n{player1} won!")
        exit()
    elif winner == "O" and p2c == "O":
        print(f"\n{player2} won!")
        exit()
    pos = int(input(f"\n{player2} choose position to put {p2c}: "))
    winner = game_board(pos, p2c)
print("Game Tied!")
