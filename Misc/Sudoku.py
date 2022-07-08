print("SUDOKU")
row1 = [4, 0, 7, 0, 0, 0, 1, 6, 2]
row2 = [0, 8, 0, 0, 0, 2, 4, 7, 0]
row3 = [9, 1, 2, 7, 6, 0, 0, 3, 8]
row4 = [0, 4, 0, 9, 0, 5, 6, 0, 0]
row5 = [0, 0, 5, 0, 2, 0, 9, 1, 0]
row6 = [7, 9, 0, 0, 0, 0, 2, 0, 4]
row7 = [6, 0, 0, 0, 0, 1, 3, 4, 0]
row8 = [0, 0, 8, 0, 4, 0, 0, 0, 6]
row9 = [0, 0, 0, 2, 5, 6, 0, 0, 0]
col1 = []
col2 = []
col3 = []
col4 = []
col5 = []
col6 = []
col7 = []
col8 = []
col9 = []

col1.append(row1[0])
col1.append(row2[0])
col1.append(row3[0])
col1.append(row4[0])
col1.append(row5[0])
col1.append(row6[0])
col1.append(row7[0])
col1.append(row8[0])
col1.append(row9[0])


col2.append(row1[1])
col2.append(row2[1])
col2.append(row3[1])
col2.append(row4[1])
col2.append(row5[1])
col2.append(row6[1])
col2.append(row7[1])
col2.append(row8[1])
col2.append(row9[1])

col3.append(row1[2])
col3.append(row2[2])
col3.append(row3[2])
col3.append(row4[2])
col3.append(row5[2])
col3.append(row6[2])
col3.append(row7[2])
col3.append(row8[2])
col3.append(row9[2])

col4.append(row1[3])
col4.append(row2[3])
col4.append(row3[3])
col4.append(row4[3])
col4.append(row5[3])
col4.append(row6[3])
col4.append(row7[3])
col4.append(row8[3])
col4.append(row9[3])

col5.append(row1[4])
col5.append(row2[4])
col5.append(row3[4])
col5.append(row4[4])
col5.append(row5[4])
col5.append(row6[4])
col5.append(row7[4])
col5.append(row8[4])
col5.append(row9[4])

col6.append(row1[5])
col6.append(row2[5])
col6.append(row3[5])
col6.append(row4[5])
col6.append(row5[5])
col6.append(row6[5])
col6.append(row7[5])
col6.append(row8[5])
col6.append(row9[5])

col7.append(row1[6])
col7.append(row2[6])
col7.append(row3[6])
col7.append(row4[6])
col7.append(row5[6])
col7.append(row6[6])
col7.append(row7[6])
col7.append(row8[6])
col7.append(row9[6])

col8.append(row1[7])
col8.append(row2[7])
col8.append(row3[7])
col8.append(row4[7])
col8.append(row5[7])
col8.append(row6[7])
col8.append(row7[7])
col8.append(row8[7])
col8.append(row9[7])

col9.append(row1[8])
col9.append(row2[8])
col9.append(row3[8])
col9.append(row4[8])
col9.append(row5[8])
col9.append(row6[8])
col9.append(row7[8])
col9.append(row8[8])
col9.append(row9[8])

print(f"{row1[0]} {row1[1]} {row1[2]} | {row1[3]} {row1[4]} {row1[5]} | {row1[6]} {row1[7]} {row1[8]}")
print(f"{row2[0]} {row2[1]} {row2[2]} | {row2[3]} {row2[4]} {row2[5]} | {row2[6]} {row2[7]} {row2[8]}")
print(f"{row3[0]} {row3[1]} {row3[2]} | {row3[3]} {row3[4]} {row3[5]} | {row3[6]} {row3[7]} {row3[8]}")
print("---------------------")
print(f"{row4[0]} {row4[1]} {row4[2]} | {row4[3]} {row4[4]} {row4[5]} | {row4[6]} {row4[7]} {row4[8]}")
print(f"{row5[0]} {row5[1]} {row5[2]} | {row5[3]} {row5[4]} {row5[5]} | {row5[6]} {row5[7]} {row5[8]}")
print(f"{row6[0]} {row6[1]} {row6[2]} | {row6[3]} {row6[4]} {row6[5]} | {row6[6]} {row6[7]} {row6[8]}")
print("---------------------")
print(f"{row7[0]} {row7[1]} {row7[2]} | {row7[3]} {row7[4]} {row7[5]} | {row7[6]} {row7[7]} {row7[8]}")
print(f"{row8[0]} {row8[1]} {row8[2]} | {row8[3]} {row8[4]} {row8[5]} | {row8[6]} {row8[7]} {row8[8]}")
print(f"{row9[0]} {row9[1]} {row9[2]} | {row9[3]} {row9[4]} {row9[5]} | {row9[6]} {row9[7]} {row9[8]}")


def check_col(pos):
    if pos == 0:
        return col1
    elif pos == 1:
        return col2
    elif pos == 2:
        return col3
    elif pos == 3:
        return col4
    elif pos == 4:
        return col5
    elif pos == 5:
        return col6
    elif pos == 6:
        return col7
    elif pos == 7:
        return col8
    elif pos == 8:
        return col9


def col_return(pos):
    if pos == 0:
        return "Column 1"
    elif pos == 1:
        return "Column 2"
    elif pos == 2:
        return "column 3"
    elif pos == 3:
        return "Column 4"
    elif pos == 4:
        return "Column 5"
    elif pos == 5:
        return "Column 6"
    elif pos == 6:
        return "Column 7"
    elif pos == 7:
        return "Column 8"
    elif pos == 8:
        return "Column 9"


def count(lst, value):
    c = 0
    for i in lst:
        if i == value:
            c += 1
    return c


wrong = False
b_reason = ""
r_reason = ""
c_reason = ""
g_reason = ""

for pos, value in enumerate(row1):
    if value != 0:
        if count(row1, value) != 1:
            wrong = True
            r_reason = f"Repeatation of number {value} in Row 1"

        if count(check_col(pos), value) != 1:
            wrong = True
            c_reason = f"Repeatation of number {value} in {col_return(pos)}"
            break
else:
    for pos, value in enumerate(row2):
        if value != 0:
            if count(row2, value) != 1:
                wrong = True
                r_reason = f"Repeatation of number {value} in Row 2"

            if count(check_col(pos), value) != 1:
                wrong = True
                c_reason = f"Repeatation of number {value} in {col_return(pos)}"
                break
    else:
        for pos, value in enumerate(row3):
            if value != 0:
                if count(row3, value) != 1:
                    wrong = True
                    r_reason = f"Repeatation of number {value} in Row 3"

                if count(check_col(pos), value) != 1:
                    wrong = True
                    c_reason = f"Repeatation of number {value} in {col_return(pos)}"
                    break
        else:
            for pos, value in enumerate(row4):
                if value != 0:
                    if count(row4, value) != 1:
                        wrong = True
                        r_reason = f"Repeatation of number {value} in Row 4"

                    if count(check_col(pos), value) != 1:
                        wrong = True
                        c_reason = f"Repeatation of number {value} in {col_return(pos)}"
                        break
            else:
                for pos, value in enumerate(row5):
                    if value != 0:
                        if count(row5, value) != 1:
                            wrong = True
                            r_reason = f"Repeatation of number {value} in Row 5"

                        if count(check_col(pos), value) != 1:
                            wrong = True
                            c_reason = f"Repeatation of number {value} in {col_return(pos)}"
                            break
                else:
                    for pos, value in enumerate(row6):
                        if value != 0:
                            if count(row6, value) != 1:
                                wrong = True
                                r_reason = f"Repeatation of number {value} in Row 6"

                            if count(check_col(pos), value) != 1:
                                wrong = True
                                c_reason = f"Repeatation of number {value} in {col_return(pos)}"
                                break
                    else:
                        for pos, value in enumerate(row7):
                            if value != 0:
                                if count(row7, value) != 1:
                                    wrong = True
                                    r_reason = f"Repeatation of number {value} in Row 7"

                                if count(check_col(pos), value) != 1:
                                    wrong = True
                                    c_reason = f"Repeatation of number {value} in {col_return(pos)}"
                                    break
                        else:
                            for pos, value in enumerate(row8):
                                if value != 0:
                                    if count(row8, value) != 1:
                                        wrong = True
                                        r_reason = f"Repeatation of number {value} in Row 8"

                                    if count(check_col(pos), value) != 1:
                                        wrong = True
                                        c_reason = f"Repeatation of number {value} in {col_return(pos)}"
                                        break
                            else:
                                for pos, value in enumerate(row9):
                                    if value != 0:
                                        if count(row9, value) != 1:
                                            wrong = True
                                            r_reason = f"Repeatation of number {value} in Row 9"

                                        if count(check_col(pos), value) != 1:
                                            wrong = True
                                            c_reason = f"Repeatation of number {value} in {col_return(pos)}"
                                            break

box1, box2, box3, box4, box5, box6, box7, box8, box9 = [
], [], [], [], [], [], [], [], []
box1.append(row1[0])
box1.extend([row1[1], row1[2], row2[0], row2[1],
             row2[2], row3[0], row3[1], row3[2]])

box2.append(row1[3])
box2.extend([row1[4], row1[5], row2[3], row2[4],
             row2[5], row3[3], row3[4], row3[5]])

box3.append(row1[6])
box3.extend([row1[7], row1[8], row2[6], row2[7],
             row2[8], row3[6], row3[7], row3[8]])

box4.append(row4[0])
box4.extend([row4[1], row4[2], row5[0], row5[1],
             row5[2], row6[0], row6[1], row6[2]])

box5.append(row4[3])
box5.extend([row4[4], row4[5], row5[3], row5[4],
             row5[5], row6[3], row6[4], row6[5]])

box6.append(row4[6])
box6.extend([row4[7], row4[8], row5[6], row5[7],
             row5[8], row6[6], row6[7], row6[8]])

box7.append(row7[0])
box7.extend([row7[1], row7[2], row8[0], row8[1],
             row8[2], row9[0], row9[1], row9[2]])

box8.append(row7[3])
box8.extend([row7[4], row7[5], row8[3], row8[4],
             row8[5], row9[3], row9[4], row9[5]])

box9.append(row7[6])
box9.extend([row7[7], row7[8], row8[6], row8[7],
             row8[8], row9[6], row9[7], row9[8]])

for value in row1:
    if value > 9 or value < 0:
        wrong = True
        g_reason = "Sudoku contains number(s) which are not in range of [1-9]"

for value in row2:
    if value > 9 or value < 0:
        wrong = True
        g_reason = "Sudoku contains number(s) which are not in range of [1-9]"

for value in row3:
    if value > 9 or value < 0:
        wrong = True
        g_reason = "Sudoku contains number(s) which are not in range of [1-9]"

for value in row4:
    if value > 9 or value < 0:
        wrong = True
        g_reason = "Sudoku contains number(s) which are not in range of [1-9]"

for value in row5:
    if value > 9 or value < 0:
        wrong = True
        g_reason = "Sudoku contains number(s) which are not in range of [1-9]"

for value in row6:
    if value > 9 or value < 0:
        wrong = True
        g_reason = "Sudoku contains number(s) which are not in range of [1-9]"

for value in row7:
    if value > 9 or value < 0:
        wrong = True
        g_reason = "Sudoku contains number(s) which are not in range of [1-9]"

for value in row8:
    if value > 9 or value < 0:
        wrong = True
        g_reason = "Sudoku contains number(s) which are not in range of [1-9]"

for value in row9:
    if value > 9 or value < 0:
        wrong = True
        g_reason = "Sudoku contains number(s) which are not in range of [1-9]"

for i in box1:
    if i != 0:
        if count(box1, i) != 1:
            wrong = True
            b_reason = f"Repeation of number {i} in Box 1"
            break
for i in box2:
    if i != 0:
        if count(box2, i) != 1:
            wrong = True
            b_reason = f"Repeation of number {i} in Box 2"
            break

for i in box3:
    if i != 0:
        if count(box3, i) != 1:
            wrong = True
            b_reason = f"Repeation of number {i} in Box 3"
            break
for i in box4:
    if i != 0:
        if count(box4, i) != 1:
            wrong = True
            b_reason = f"Repeation of number {i} in Box 4"
            break
for i in box5:
    if i != 0:
        if count(box5, i) != 1:
            wrong = True
            b_reason = f"Repeation of number {i} in Box 5"
            break
for i in box6:
    if i != 0:
        if count(box6, i) != 1:
            wrong = True
            b_reason = f"Repeation of number {i} in Box 6"
            break
for i in box7:
    if i != 0:
        if count(box7, i) != 1:
            wrong = True
            b_reason = f"Repeation of number {i} in Box 7"
            break
for i in box8:
    if i != 0:
        if count(box8, i) != 1:
            wrong = True
            b_reason = f"Repeation of number {i} in Box 8"
            break
for i in box9:
    if i != 0:
        if count(box9, i) != 1:
            wrong = True
            b_reason = f"Repeation of number {i} in Box 9"
            break

if wrong is True:
    print("Sudoku is not ok. Reasons listed below:\n")
    if b_reason != "":
        print(b_reason)
    if c_reason != "":
        print(c_reason)
    if g_reason != "":
        print(g_reason)
    if r_reason != "":
        print(r_reason)
else:
    print("Sudoku is ok")

number=[1,2,3,4,5,6,7,8,9]
unique_lst_row1=[]
unique_lst_col1=[]
unique_lst_box1=[]
for value in row1:
    if value!=0:
        unique_lst_row1.append(value)
for value in col1:
    if value!=0:
        unique_lst_col1.append(value)
for value in box1:
    if value!=0:
        unique_lst_box1.append(value)

unique_lst_row2=[]
unique_lst_col2=[]
unique_lst_box2=[]
for value in row2:
    if value!=0:
        unique_lst_row2.append(value)
for value in col2:
    if value!=0:
        unique_lst_col2.append(value)
for value in box2:
    if value!=0:
        unique_lst_box2.append(value)

unique_lst_row3=[]
unique_lst_col3=[]
unique_lst_box3=[]
for value in row3:
    if value!=0:
        unique_lst_row3.append(value)
for value in col3:
    if value!=0:
        unique_lst_col3.append(value)
for value in box3:
    if value!=0:
        unique_lst_box3.append(value)

unique_lst_row4=[]
unique_lst_col4=[]
unique_lst_box4=[]
for value in row4:
    if value!=0:
        unique_lst_row4.append(value)
for value in col4:
    if value!=0:
        unique_lst_col4.append(value)
for value in box4:
    if value!=0:
        unique_lst_box4.append(value)

unique_lst_row5=[]
unique_lst_col5=[]
unique_lst_box5=[]
for value in row5:
    if value!=0:
        unique_lst_row5.append(value)
for value in col5:
    if value!=0:
        unique_lst_col5.append(value)
for value in box5:
    if value!=0:
        unique_lst_box5.append(value)

unique_lst_row6=[]
unique_lst_col6=[]
unique_lst_box6=[]
for value in row6:
    if value!=0:
        unique_lst_row6.append(value)
for value in col6:
    if value!=0:
        unique_lst_col6.append(value)
for value in box6:
    if value!=0:
        unique_lst_box6.append(value)

unique_lst_row7=[]
unique_lst_col7=[]
unique_lst_box7=[]
for value in row7:
    if value!=0:
        unique_lst_row7.append(value)
for value in col7:
    if value!=0:
        unique_lst_col7.append(value)
for value in box7:
    if value!=0:
        unique_lst_box7.append(value)

unique_lst_row8=[]
unique_lst_col8=[]
unique_lst_box8=[]
for value in row8:
    if value!=0:
        unique_lst_row8.append(value)
for value in col8:
    if value!=0:
        unique_lst_col8.append(value)
for value in box8:
    if value!=0:
        unique_lst_box8.append(value)

unique_lst_row9=[]
unique_lst_col9=[]
unique_lst_box9=[]
for value in row9:
    if value!=0:
        unique_lst_row9.append(value)
for value in col9:
    if value!=0:
        unique_lst_col9.append(value)
for value in box9:
    if value!=0:
        unique_lst_box9.append(value)

import random

def check_col_solve(pos):
    if pos == 0:
        return unique_lst_col1
    elif pos == 1:
        return unique_lst_col2
    elif pos == 2:
        return unique_lst_col3
    elif pos == 3:
        return unique_lst_col4
    elif pos == 4:
        return unique_lst_col5
    elif pos == 5:
        return unique_lst_col6
    elif pos == 6:
        return unique_lst_col7
    elif pos == 7:
        return unique_lst_col8
    elif pos == 8:
        return unique_lst_col9

def check_box_pos(row,index):
    if row==1 and index==0:
        return unique_lst_box1
    if row==1 and index==1:
        return unique_lst_box1
    if row==1 and index==2:
        return unique_lst_box1
    if row==1 and index==3:
        return unique_lst_box2
    if row==1 and index==4:
        return unique_lst_box2
    if row==1 and index==5:
        return unique_lst_box2
    if row==1 and index==6:
        return unique_lst_box3
    if row==1 and index==7:
        return unique_lst_box3
    if row==1 and index==8:
        return unique_lst_box3

    if row==2 and index==0:
        return unique_lst_box1
    if row==2 and index==1:
        return unique_lst_box1
    if row==2 and index==2:
        return unique_lst_box1
    if row==2 and index==3:
        return unique_lst_box2
    if row==2 and index==4:
        return unique_lst_box2
    if row==2 and index==5:
        return unique_lst_box2
    if row==2 and index==6:
        return unique_lst_box3
    if row==2 and index==7:
        return unique_lst_box3
    if row==2 and index==8:
        return unique_lst_box3

    if row==3 and index==0:
        return unique_lst_box1
    if row==3 and index==1:
        return unique_lst_box1
    if row==3 and index==2:
        return unique_lst_box1
    if row==3 and index==3:
        return unique_lst_box2
    if row==3 and index==4:
        return unique_lst_box2
    if row==3 and index==5:
        return unique_lst_box2
    if row==3 and index==6:
        return unique_lst_box3
    if row==3 and index==7:
        return unique_lst_box3
    if row==3 and index==8:
        return unique_lst_box3

    if row==4 and index==0:
        return unique_lst_box4
    if row==4 and index==1:
        return unique_lst_box4
    if row==4 and index==2:
        return unique_lst_box4
    if row==4 and index==3:
        return unique_lst_box5
    if row==4 and index==4:
        return unique_lst_box5
    if row==4 and index==5:
        return unique_lst_box5
    if row==4 and index==6:
        return unique_lst_box6
    if row==4 and index==7:
        return unique_lst_box6
    if row==4 and index==8:
        return unique_lst_box6

    if row==5 and index==0:
        return unique_lst_box4
    if row==5 and index==1:
        return unique_lst_box4
    if row==5 and index==2:
        return unique_lst_box4
    if row==5 and index==3:
        return unique_lst_box5
    if row==5 and index==4:
        return unique_lst_box5
    if row==5 and index==5:
        return unique_lst_box5
    if row==5 and index==6:
        return unique_lst_box6
    if row==5 and index==7:
        return unique_lst_box6
    if row==5 and index==8:
        return unique_lst_box6

    if row==6 and index==0:
        return unique_lst_box4
    if row==6 and index==1:
        return unique_lst_box4
    if row==6 and index==2:
        return unique_lst_box4
    if row==6 and index==3:
        return unique_lst_box5
    if row==6 and index==4:
        return unique_lst_box5
    if row==6 and index==5:
        return unique_lst_box5
    if row==6 and index==6:
        return unique_lst_box6
    if row==6 and index==7:
        return unique_lst_box6
    if row==6 and index==8:
        return unique_lst_box6
    
    if row==7 and index==0:
        return unique_lst_box7
    if row==7 and index==1:
        return unique_lst_box7
    if row==7 and index==2:
        return unique_lst_box7
    if row==7 and index==3:
        return unique_lst_box8
    if row==7 and index==4:
        return unique_lst_box8
    if row==7 and index==5:
        return unique_lst_box8
    if row==7 and index==6:
        return unique_lst_box9
    if row==7 and index==7:
        return unique_lst_box9
    if row==7 and index==8:
        return unique_lst_box9

    if row==8 and index==0:
        return unique_lst_box7
    if row==8 and index==1:
        return unique_lst_box7
    if row==8 and index==2:
        return unique_lst_box7
    if row==8 and index==3:
        return unique_lst_box8
    if row==8 and index==4:
        return unique_lst_box8
    if row==8 and index==5:
        return unique_lst_box8
    if row==8 and index==6:
        return unique_lst_box9
    if row==8 and index==7:
        return unique_lst_box9
    if row==8 and index==8:
        return unique_lst_box9

    if row==9 and index==0:
        return unique_lst_box7
    if row==9 and index==1:
        return unique_lst_box7
    if row==9 and index==2:
        return unique_lst_box7
    if row==9 and index==3:
        return unique_lst_box8
    if row==9 and index==4:
        return unique_lst_box8
    if row==9 and index==5:
        return unique_lst_box8
    if row==9 and index==6:
        return unique_lst_box9
    if row==9 and index==7:
        return unique_lst_box9
    if row==9 and index==8:
        return unique_lst_box9

col_solve_1=[]
col_solve_2=[]
col_solve_3=[]
col_solve_4=[]
col_solve_5=[]
col_solve_6=[]
col_solve_7=[]
col_solve_8=[]

box_solve_1=[]
box_solve_2=[]
box_solve_3=[]
box_solve_4=[]
box_solve_5=[]
box_solve_6=[]
box_solve_7=[]
box_solve_8=[]
box_solve_9=[]

for value,pos in enumerate(row1):
    if value==0: 
        col_solve_1=check_col_solve(pos)
        box_solve_1=check_box_pos(1,pos)
        row1.remove(value)
        value=random.choice(number)
        while value in unique_lst_row1 or value in col_solve_1 or value in unique_lst_box1:
            value=random.choice(number)

        row1.insert(pos,value)
        unique_lst_row1.append(value)
        col_solve_1.append(value)
        box_solve_1.append(value)

for value,pos in enumerate(row2):
    if value==0:
        col_solve_2=check_col_solve(pos)
        box_solve_2=check_box_pos(2,pos)
        row2.remove(value)
        value=random.choice(number)
        while value in unique_lst_row2 or value in unique_lst_col2 or value in unique_lst_box2:
            value=random.choice(number)

        row2.insert(pos,value)
        unique_lst_row2.append(value)
        col_solve_2.append(value)
        box_solve_2.append(value)
    
for value,pos in enumerate(row3):
    if value==0:
        col_solve_3=check_col_solve(pos)
        box_solve_3=check_box_pos(3,pos)
        row3.remove(value)
        value=random.choice(number)
        while value in unique_lst_row3 or value in unique_lst_col3 or value in unique_lst_box3:
            value=random.choice(number)

        row3.insert(pos,value)
        unique_lst_row3.append(value)
        col_solve_3.append(value)
        box_solve_3.append(value)

for value,pos in enumerate(row4):
    if value==0:
        col_solve_4=check_col_solve(pos)
        box_solve_4=check_box_pos(4,pos)
        row4.remove(value)
        value=random.choice(number)
        while value in unique_lst_row4 or value in unique_lst_col4 or value in unique_lst_box4:
            value=random.choice(number)

        row4.insert(pos,value)
        unique_lst_row4.append(value)
        col_solve_4.append(value)
        box_solve_4.append(value)

for value,pos in enumerate(row5):
    if value==0:
        col_solve_5=check_col_solve(pos)
        box_solve_5=check_box_pos(5,pos)
        row5.remove(value)
        value=random.choice(number)
        while value in unique_lst_row5 or value in unique_lst_col5 or value in unique_lst_box5:
            value=random.choice(number)

        row5.insert(pos,value)
        unique_lst_row5.append(value)
        col_solve_5.append(value)
        box_solve_5.append(value)

for value,pos in enumerate(row6):
    if value==0:
        col_solve_6=check_col_solve(pos)
        box_solve_6=check_box_pos(6,pos)
        row6.remove(value)
        value=random.choice(number)
        while value in unique_lst_row6 or value in unique_lst_col6 or value in unique_lst_box6:
            value=random.choice(number)

        row6.insert(pos,value)
        unique_lst_row6.append(value)
        col_solve_6.append(value)
        box_solve_6.append(value)

for value,pos in enumerate(row7):
    if value==0:
        col_solve_7=check_col_solve(pos)
        box_solve_7=check_box_pos(7,pos)
        row7.remove(value)
        value=random.choice(number)
        while value in unique_lst_row7 or value in unique_lst_col7 or value in unique_lst_box7:
            value=random.choice(number)

        row7.insert(pos,value)
        unique_lst_row7.append(value)
        col_solve_7.append(value)
        box_solve_7.append(value)

for value,pos in enumerate(row8):
    if value==0:
        col_solve_8=check_col_solve(pos)
        box_solve_8=check_box_pos(8,pos)
        row8.remove(value)
        value=random.choice(number)
        while value in unique_lst_row8 or value in unique_lst_col8 or value in unique_lst_box8:
            value=random.choice(number)

        row8.insert(pos,value)
        unique_lst_row8.append(value)
        col_solve_8.append(value)
        box_solve_8.append(value)

for value,pos in enumerate(row9):
    if value==0:
        col_solve_9=check_col_solve(pos)
        box_solve_9=check_box_pos(9,pos)
        row9.remove(value)
        value=random.choice(number)
        while value in unique_lst_row9 or value in unique_lst_col9 or value in unique_lst_box9:
            value=random.choice(number)

        row9.insert(pos,value)
        unique_lst_row9.append(value)
        col_solve_9.append(value)
        box_solve_9.append(value)

for value,pos in enumerate(row1):
    if value==0: 
        col_solve_1=check_col_solve(pos)
        box_solve_1=check_box_pos(1,pos)
        row1.remove(value)
        value=random.choice(number)
        print(unique_lst_row1,unique_lst_col1,unique_lst_box1)
        while value in unique_lst_row1 or value in col_solve_1 or value in unique_lst_box1:
            print(value)
            value=random.choice(number)

        row1.insert(pos,value)
        unique_lst_row1.append(value)
        col_solve_1.append(value)
        box_solve_1.append(value)

for value,pos in enumerate(row2):
    if value==0:
        col_solve_2=check_col_solve(pos)
        box_solve_2=check_box_pos(2,pos)
        row2.remove(value)
        value=random.choice(number)
        while value in unique_lst_row2 or value in unique_lst_col2 or value in unique_lst_box2:
            value=random.choice(number)

        row2.insert(pos,value)
        unique_lst_row2.append(value)
        col_solve_2.append(value)
        box_solve_2.append(value)
    
for value,pos in enumerate(row3):
    if value==0:
        col_solve_3=check_col_solve(pos)
        box_solve_3=check_box_pos(3,pos)
        row3.remove(value)
        value=random.choice(number)
        while value in unique_lst_row3 or value in unique_lst_col3 or value in unique_lst_box3:
            value=random.choice(number)

        row3.insert(pos,value)
        unique_lst_row3.append(value)
        col_solve_3.append(value)
        box_solve_3.append(value)

for value,pos in enumerate(row4):
    if value==0:
        col_solve_4=check_col_solve(pos)
        box_solve_4=check_box_pos(4,pos)
        row4.remove(value)
        value=random.choice(number)
        while value in unique_lst_row4 or value in unique_lst_col4 or value in unique_lst_box4:
            value=random.choice(number)

        row4.insert(pos,value)
        unique_lst_row4.append(value)
        col_solve_4.append(value)
        box_solve_4.append(value)

for value,pos in enumerate(row5):
    if value==0:
        col_solve_5=check_col_solve(pos)
        box_solve_5=check_box_pos(5,pos)
        row5.remove(value)
        value=random.choice(number)
        while value in unique_lst_row5 or value in unique_lst_col5 or value in unique_lst_box5:
            value=random.choice(number)

        row5.insert(pos,value)
        unique_lst_row5.append(value)
        col_solve_5.append(value)
        box_solve_5.append(value)

for value,pos in enumerate(row6):
    if value==0:
        col_solve_6=check_col_solve(pos)
        box_solve_6=check_box_pos(6,pos)
        row6.remove(value)
        value=random.choice(number)
        while value in unique_lst_row6 or value in unique_lst_col6 or value in unique_lst_box6:
            value=random.choice(number)

        row6.insert(pos,value)
        unique_lst_row6.append(value)
        col_solve_6.append(value)
        box_solve_6.append(value)

for value,pos in enumerate(row7):
    if value==0:
        col_solve_7=check_col_solve(pos)
        box_solve_7=check_box_pos(7,pos)
        row7.remove(value)
        value=random.choice(number)
        while value in unique_lst_row7 or value in unique_lst_col7 or value in unique_lst_box7:
            value=random.choice(number)

        row7.insert(pos,value)
        unique_lst_row7.append(value)
        col_solve_7.append(value)
        box_solve_7.append(value)

for value,pos in enumerate(row8):
    if value==0:
        col_solve_8=check_col_solve(pos)
        box_solve_8=check_box_pos(8,pos)
        row8.remove(value)
        value=random.choice(number)
        while value in unique_lst_row8 or value in unique_lst_col8 or value in unique_lst_box8:
            value=random.choice(number)

        row8.insert(pos,value)
        unique_lst_row8.append(value)
        col_solve_8.append(value)
        box_solve_8.append(value)

for value,pos in enumerate(row9):
    if value==0:
        col_solve_9=check_col_solve(pos)
        box_solve_9=check_box_pos(9,pos)
        row9.remove(value)
        value=random.choice(number)
        while value in unique_lst_row9 or value in unique_lst_col9 or value in unique_lst_box9:
            value=random.choice(number)

        row9.insert(pos,value)
        unique_lst_row9.append(value)
        col_solve_9.append(value)
        box_solve_9.append(value)

for value,pos in enumerate(row1):
    if value==0: 
        col_solve_1=check_col_solve(pos)
        box_solve_1=check_box_pos(1,pos)
        row1.remove(value)
        value=random.choice(number)
        print(unique_lst_row1,unique_lst_col1,unique_lst_box1)
        while value in unique_lst_row1 or value in col_solve_1 or value in unique_lst_box1:
            print(value)
            value=random.choice(number)

        row1.insert(pos,value)
        unique_lst_row1.append(value)
        col_solve_1.append(value)
        box_solve_1.append(value)

for value,pos in enumerate(row2):
    if value==0:
        col_solve_2=check_col_solve(pos)
        box_solve_2=check_box_pos(2,pos)
        row2.remove(value)
        value=random.choice(number)
        while value in unique_lst_row2 or value in unique_lst_col2 or value in unique_lst_box2:
            value=random.choice(number)

        row2.insert(pos,value)
        unique_lst_row2.append(value)
        col_solve_2.append(value)
        box_solve_2.append(value)
    
for value,pos in enumerate(row3):
    if value==0:
        col_solve_3=check_col_solve(pos)
        box_solve_3=check_box_pos(3,pos)
        row3.remove(value)
        value=random.choice(number)
        while value in unique_lst_row3 or value in unique_lst_col3 or value in unique_lst_box3:
            value=random.choice(number)

        row3.insert(pos,value)
        unique_lst_row3.append(value)
        col_solve_3.append(value)
        box_solve_3.append(value)

for value,pos in enumerate(row4):
    if value==0:
        col_solve_4=check_col_solve(pos)
        box_solve_4=check_box_pos(4,pos)
        row4.remove(value)
        value=random.choice(number)
        while value in unique_lst_row4 or value in unique_lst_col4 or value in unique_lst_box4:
            value=random.choice(number)

        row4.insert(pos,value)
        unique_lst_row4.append(value)
        col_solve_4.append(value)
        box_solve_4.append(value)

for value,pos in enumerate(row5):
    if value==0:
        col_solve_5=check_col_solve(pos)
        box_solve_5=check_box_pos(5,pos)
        row5.remove(value)
        value=random.choice(number)
        while value in unique_lst_row5 or value in unique_lst_col5 or value in unique_lst_box5:
            value=random.choice(number)

        row5.insert(pos,value)
        unique_lst_row5.append(value)
        col_solve_5.append(value)
        box_solve_5.append(value)

for value,pos in enumerate(row6):
    if value==0:
        col_solve_6=check_col_solve(pos)
        box_solve_6=check_box_pos(6,pos)
        row6.remove(value)
        value=random.choice(number)
        while value in unique_lst_row6 or value in unique_lst_col6 or value in unique_lst_box6:
            value=random.choice(number)

        row6.insert(pos,value)
        unique_lst_row6.append(value)
        col_solve_6.append(value)
        box_solve_6.append(value)

for value,pos in enumerate(row7):
    if value==0:
        col_solve_7=check_col_solve(pos)
        box_solve_7=check_box_pos(7,pos)
        row7.remove(value)
        value=random.choice(number)
        while value in unique_lst_row7 or value in unique_lst_col7 or value in unique_lst_box7:
            value=random.choice(number)

        row7.insert(pos,value)
        unique_lst_row7.append(value)
        col_solve_7.append(value)
        box_solve_7.append(value)

for value,pos in enumerate(row8):
    if value==0:
        col_solve_8=check_col_solve(pos)
        box_solve_8=check_box_pos(8,pos)
        row8.remove(value)
        value=random.choice(number)
        while value in unique_lst_row8 or value in unique_lst_col8 or value in unique_lst_box8:
            value=random.choice(number)

        row8.insert(pos,value)
        unique_lst_row8.append(value)
        col_solve_8.append(value)
        box_solve_8.append(value)

for value,pos in enumerate(row9):
    if value==0:
        col_solve_9=check_col_solve(pos)
        box_solve_9=check_box_pos(9,pos)
        row9.remove(value)
        value=random.choice(number)
        while value in unique_lst_row9 or value in unique_lst_col9 or value in unique_lst_box9:
            value=random.choice(number)

        row9.insert(pos,value)
        unique_lst_row9.append(value)
        col_solve_9.append(value)
        box_solve_9.append(value)

for value,pos in enumerate(row1):
    if value==0: 
        col_solve_1=check_col_solve(pos)
        box_solve_1=check_box_pos(1,pos)
        row1.remove(value)
        value=random.choice(number)
        print(unique_lst_row1,unique_lst_col1,unique_lst_box1)
        while value in unique_lst_row1 or value in col_solve_1 or value in unique_lst_box1:
            print(value)
            value=random.choice(number)

        row1.insert(pos,value)
        unique_lst_row1.append(value)
        col_solve_1.append(value)
        box_solve_1.append(value)

for value,pos in enumerate(row2):
    if value==0:
        col_solve_2=check_col_solve(pos)
        box_solve_2=check_box_pos(2,pos)
        row2.remove(value)
        value=random.choice(number)
        while value in unique_lst_row2 or value in unique_lst_col2 or value in unique_lst_box2:
            value=random.choice(number)

        row2.insert(pos,value)
        unique_lst_row2.append(value)
        col_solve_2.append(value)
        box_solve_2.append(value)
    
for value,pos in enumerate(row3):
    if value==0:
        col_solve_3=check_col_solve(pos)
        box_solve_3=check_box_pos(3,pos)
        row3.remove(value)
        value=random.choice(number)
        while value in unique_lst_row3 or value in unique_lst_col3 or value in unique_lst_box3:
            value=random.choice(number)

        row3.insert(pos,value)
        unique_lst_row3.append(value)
        col_solve_3.append(value)
        box_solve_3.append(value)

for value,pos in enumerate(row4):
    if value==0:
        col_solve_4=check_col_solve(pos)
        box_solve_4=check_box_pos(4,pos)
        row4.remove(value)
        value=random.choice(number)
        while value in unique_lst_row4 or value in unique_lst_col4 or value in unique_lst_box4:
            value=random.choice(number)

        row4.insert(pos,value)
        unique_lst_row4.append(value)
        col_solve_4.append(value)
        box_solve_4.append(value)

for value,pos in enumerate(row5):
    if value==0:
        col_solve_5=check_col_solve(pos)
        box_solve_5=check_box_pos(5,pos)
        row5.remove(value)
        value=random.choice(number)
        while value in unique_lst_row5 or value in unique_lst_col5 or value in unique_lst_box5:
            value=random.choice(number)

        row5.insert(pos,value)
        unique_lst_row5.append(value)
        col_solve_5.append(value)
        box_solve_5.append(value)

for value,pos in enumerate(row6):
    if value==0:
        col_solve_6=check_col_solve(pos)
        box_solve_6=check_box_pos(6,pos)
        row6.remove(value)
        value=random.choice(number)
        while value in unique_lst_row6 or value in unique_lst_col6 or value in unique_lst_box6:
            value=random.choice(number)

        row6.insert(pos,value)
        unique_lst_row6.append(value)
        col_solve_6.append(value)
        box_solve_6.append(value)

for value,pos in enumerate(row7):
    if value==0:
        col_solve_7=check_col_solve(pos)
        box_solve_7=check_box_pos(7,pos)
        row7.remove(value)
        value=random.choice(number)
        while value in unique_lst_row7 or value in unique_lst_col7 or value in unique_lst_box7:
            value=random.choice(number)

        row7.insert(pos,value)
        unique_lst_row7.append(value)
        col_solve_7.append(value)
        box_solve_7.append(value)

for value,pos in enumerate(row8):
    if value==0:
        col_solve_8=check_col_solve(pos)
        box_solve_8=check_box_pos(8,pos)
        row8.remove(value)
        value=random.choice(number)
        while value in unique_lst_row8 or value in unique_lst_col8 or value in unique_lst_box8:
            value=random.choice(number)

        row8.insert(pos,value)
        unique_lst_row8.append(value)
        col_solve_8.append(value)
        box_solve_8.append(value)

for value,pos in enumerate(row9):
    if value==0:
        col_solve_9=check_col_solve(pos)
        box_solve_9=check_box_pos(9,pos)
        row9.remove(value)
        value=random.choice(number)
        while value in unique_lst_row9 or value in unique_lst_col9 or value in unique_lst_box9:
            value=random.choice(number)

        row9.insert(pos,value)
        unique_lst_row9.append(value)
        col_solve_9.append(value)
        box_solve_9.append(value)

for value,pos in enumerate(row1):
    if value==0: 
        col_solve_1=check_col_solve(pos)
        box_solve_1=check_box_pos(1,pos)
        row1.remove(value)
        value=random.choice(number)
        print(unique_lst_row1,unique_lst_col1,unique_lst_box1)
        while value in unique_lst_row1 or value in col_solve_1 or value in unique_lst_box1:
            print(value)
            value=random.choice(number)

        row1.insert(pos,value)
        unique_lst_row1.append(value)
        col_solve_1.append(value)
        box_solve_1.append(value)

for value,pos in enumerate(row2):
    if value==0:
        col_solve_2=check_col_solve(pos)
        box_solve_2=check_box_pos(2,pos)
        row2.remove(value)
        value=random.choice(number)
        while value in unique_lst_row2 or value in unique_lst_col2 or value in unique_lst_box2:
            value=random.choice(number)

        row2.insert(pos,value)
        unique_lst_row2.append(value)
        col_solve_2.append(value)
        box_solve_2.append(value)
    
for value,pos in enumerate(row3):
    if value==0:
        col_solve_3=check_col_solve(pos)
        box_solve_3=check_box_pos(3,pos)
        row3.remove(value)
        value=random.choice(number)
        while value in unique_lst_row3 or value in unique_lst_col3 or value in unique_lst_box3:
            value=random.choice(number)

        row3.insert(pos,value)
        unique_lst_row3.append(value)
        col_solve_3.append(value)
        box_solve_3.append(value)

for value,pos in enumerate(row4):
    if value==0:
        col_solve_4=check_col_solve(pos)
        box_solve_4=check_box_pos(4,pos)
        row4.remove(value)
        value=random.choice(number)
        while value in unique_lst_row4 or value in unique_lst_col4 or value in unique_lst_box4:
            value=random.choice(number)

        row4.insert(pos,value)
        unique_lst_row4.append(value)
        col_solve_4.append(value)
        box_solve_4.append(value)

for value,pos in enumerate(row5):
    if value==0:
        col_solve_5=check_col_solve(pos)
        box_solve_5=check_box_pos(5,pos)
        row5.remove(value)
        value=random.choice(number)
        while value in unique_lst_row5 or value in unique_lst_col5 or value in unique_lst_box5:
            value=random.choice(number)

        row5.insert(pos,value)
        unique_lst_row5.append(value)
        col_solve_5.append(value)
        box_solve_5.append(value)

for value,pos in enumerate(row6):
    if value==0:
        col_solve_6=check_col_solve(pos)
        box_solve_6=check_box_pos(6,pos)
        row6.remove(value)
        value=random.choice(number)
        while value in unique_lst_row6 or value in unique_lst_col6 or value in unique_lst_box6:
            value=random.choice(number)

        row6.insert(pos,value)
        unique_lst_row6.append(value)
        col_solve_6.append(value)
        box_solve_6.append(value)

for value,pos in enumerate(row7):
    if value==0:
        col_solve_7=check_col_solve(pos)
        box_solve_7=check_box_pos(7,pos)
        row7.remove(value)
        value=random.choice(number)
        while value in unique_lst_row7 or value in unique_lst_col7 or value in unique_lst_box7:
            value=random.choice(number)

        row7.insert(pos,value)
        unique_lst_row7.append(value)
        col_solve_7.append(value)
        box_solve_7.append(value)

for value,pos in enumerate(row8):
    if value==0:
        col_solve_8=check_col_solve(pos)
        box_solve_8=check_box_pos(8,pos)
        row8.remove(value)
        value=random.choice(number)
        while value in unique_lst_row8 or value in unique_lst_col8 or value in unique_lst_box8:
            value=random.choice(number)

        row8.insert(pos,value)
        unique_lst_row8.append(value)
        col_solve_8.append(value)
        box_solve_8.append(value)

for value,pos in enumerate(row9):
    if value==0:
        col_solve_9=check_col_solve(pos)
        box_solve_9=check_box_pos(9,pos)
        row9.remove(value)
        value=random.choice(number)
        while value in unique_lst_row9 or value in unique_lst_col9 or value in unique_lst_box9:
            value=random.choice(number)

        row9.insert(pos,value)
        unique_lst_row9.append(value)
        col_solve_9.append(value)
        box_solve_9.append(value)

for value,pos in enumerate(row1):
    if value==0: 
        col_solve_1=check_col_solve(pos)
        box_solve_1=check_box_pos(1,pos)
        row1.remove(value)
        value=random.choice(number)
        print(unique_lst_row1,unique_lst_col1,unique_lst_box1)
        while value in unique_lst_row1 or value in col_solve_1 or value in unique_lst_box1:
            print(value)
            value=random.choice(number)

        row1.insert(pos,value)
        unique_lst_row1.append(value)
        col_solve_1.append(value)
        box_solve_1.append(value)

for value,pos in enumerate(row2):
    if value==0:
        col_solve_2=check_col_solve(pos)
        box_solve_2=check_box_pos(2,pos)
        row2.remove(value)
        value=random.choice(number)
        while value in unique_lst_row2 or value in unique_lst_col2 or value in unique_lst_box2:
            value=random.choice(number)

        row2.insert(pos,value)
        unique_lst_row2.append(value)
        col_solve_2.append(value)
        box_solve_2.append(value)
    
for value,pos in enumerate(row3):
    if value==0:
        col_solve_3=check_col_solve(pos)
        box_solve_3=check_box_pos(3,pos)
        row3.remove(value)
        value=random.choice(number)
        while value in unique_lst_row3 or value in unique_lst_col3 or value in unique_lst_box3:
            value=random.choice(number)

        row3.insert(pos,value)
        unique_lst_row3.append(value)
        col_solve_3.append(value)
        box_solve_3.append(value)

for value,pos in enumerate(row4):
    if value==0:
        col_solve_4=check_col_solve(pos)
        box_solve_4=check_box_pos(4,pos)
        row4.remove(value)
        value=random.choice(number)
        while value in unique_lst_row4 or value in unique_lst_col4 or value in unique_lst_box4:
            value=random.choice(number)

        row4.insert(pos,value)
        unique_lst_row4.append(value)
        col_solve_4.append(value)
        box_solve_4.append(value)

for value,pos in enumerate(row5):
    if value==0:
        col_solve_5=check_col_solve(pos)
        box_solve_5=check_box_pos(5,pos)
        row5.remove(value)
        value=random.choice(number)
        while value in unique_lst_row5 or value in unique_lst_col5 or value in unique_lst_box5:
            value=random.choice(number)

        row5.insert(pos,value)
        unique_lst_row5.append(value)
        col_solve_5.append(value)
        box_solve_5.append(value)

for value,pos in enumerate(row6):
    if value==0:
        col_solve_6=check_col_solve(pos)
        box_solve_6=check_box_pos(6,pos)
        row6.remove(value)
        value=random.choice(number)
        while value in unique_lst_row6 or value in unique_lst_col6 or value in unique_lst_box6:
            value=random.choice(number)

        row6.insert(pos,value)
        unique_lst_row6.append(value)
        col_solve_6.append(value)
        box_solve_6.append(value)

for value,pos in enumerate(row7):
    if value==0:
        col_solve_7=check_col_solve(pos)
        box_solve_7=check_box_pos(7,pos)
        row7.remove(value)
        value=random.choice(number)
        while value in unique_lst_row7 or value in unique_lst_col7 or value in unique_lst_box7:
            value=random.choice(number)

        row7.insert(pos,value)
        unique_lst_row7.append(value)
        col_solve_7.append(value)
        box_solve_7.append(value)

for value,pos in enumerate(row8):
    if value==0:
        col_solve_8=check_col_solve(pos)
        box_solve_8=check_box_pos(8,pos)
        row8.remove(value)
        value=random.choice(number)
        while value in unique_lst_row8 or value in unique_lst_col8 or value in unique_lst_box8:
            value=random.choice(number)

        row8.insert(pos,value)
        unique_lst_row8.append(value)
        col_solve_8.append(value)
        box_solve_8.append(value)

for value,pos in enumerate(row9):
    if value==0:
        col_solve_9=check_col_solve(pos)
        box_solve_9=check_box_pos(9,pos)
        row9.remove(value)
        value=random.choice(number)
        while value in unique_lst_row9 or value in unique_lst_col9 or value in unique_lst_box9:
            value=random.choice(number)

        row9.insert(pos,value)
        unique_lst_row9.append(value)
        col_solve_9.append(value)
        box_solve_9.append(value)

for value,pos in enumerate(row1):
    if value==0: 
        col_solve_1=check_col_solve(pos)
        box_solve_1=check_box_pos(1,pos)
        row1.remove(value)
        value=random.choice(number)
        print(unique_lst_row1,unique_lst_col1,unique_lst_box1)
        while value in unique_lst_row1 or value in col_solve_1 or value in unique_lst_box1:
            print(value)
            value=random.choice(number)

        row1.insert(pos,value)
        unique_lst_row1.append(value)
        col_solve_1.append(value)
        box_solve_1.append(value)

for value,pos in enumerate(row2):
    if value==0:
        col_solve_2=check_col_solve(pos)
        box_solve_2=check_box_pos(2,pos)
        row2.remove(value)
        value=random.choice(number)
        while value in unique_lst_row2 or value in unique_lst_col2 or value in unique_lst_box2:
            value=random.choice(number)

        row2.insert(pos,value)
        unique_lst_row2.append(value)
        col_solve_2.append(value)
        box_solve_2.append(value)
    
for value,pos in enumerate(row3):
    if value==0:
        col_solve_3=check_col_solve(pos)
        box_solve_3=check_box_pos(3,pos)
        row3.remove(value)
        value=random.choice(number)
        while value in unique_lst_row3 or value in unique_lst_col3 or value in unique_lst_box3:
            value=random.choice(number)

        row3.insert(pos,value)
        unique_lst_row3.append(value)
        col_solve_3.append(value)
        box_solve_3.append(value)

for value,pos in enumerate(row4):
    if value==0:
        col_solve_4=check_col_solve(pos)
        box_solve_4=check_box_pos(4,pos)
        row4.remove(value)
        value=random.choice(number)
        while value in unique_lst_row4 or value in unique_lst_col4 or value in unique_lst_box4:
            value=random.choice(number)

        row4.insert(pos,value)
        unique_lst_row4.append(value)
        col_solve_4.append(value)
        box_solve_4.append(value)

for value,pos in enumerate(row5):
    if value==0:
        col_solve_5=check_col_solve(pos)
        box_solve_5=check_box_pos(5,pos)
        row5.remove(value)
        value=random.choice(number)
        while value in unique_lst_row5 or value in unique_lst_col5 or value in unique_lst_box5:
            value=random.choice(number)

        row5.insert(pos,value)
        unique_lst_row5.append(value)
        col_solve_5.append(value)
        box_solve_5.append(value)

for value,pos in enumerate(row6):
    if value==0:
        col_solve_6=check_col_solve(pos)
        box_solve_6=check_box_pos(6,pos)
        row6.remove(value)
        value=random.choice(number)
        while value in unique_lst_row6 or value in unique_lst_col6 or value in unique_lst_box6:
            value=random.choice(number)

        row6.insert(pos,value)
        unique_lst_row6.append(value)
        col_solve_6.append(value)
        box_solve_6.append(value)

for value,pos in enumerate(row7):
    if value==0:
        col_solve_7=check_col_solve(pos)
        box_solve_7=check_box_pos(7,pos)
        row7.remove(value)
        value=random.choice(number)
        while value in unique_lst_row7 or value in unique_lst_col7 or value in unique_lst_box7:
            value=random.choice(number)

        row7.insert(pos,value)
        unique_lst_row7.append(value)
        col_solve_7.append(value)
        box_solve_7.append(value)

for value,pos in enumerate(row8):
    if value==0:
        col_solve_8=check_col_solve(pos)
        box_solve_8=check_box_pos(8,pos)
        row8.remove(value)
        value=random.choice(number)
        while value in unique_lst_row8 or value in unique_lst_col8 or value in unique_lst_box8:
            value=random.choice(number)

        row8.insert(pos,value)
        unique_lst_row8.append(value)
        col_solve_8.append(value)
        box_solve_8.append(value)

for value,pos in enumerate(row9):
    if value==0:
        col_solve_9=check_col_solve(pos)
        box_solve_9=check_box_pos(9,pos)
        row9.remove(value)
        value=random.choice(number)
        while value in unique_lst_row9 or value in unique_lst_col9 or value in unique_lst_box9:
            value=random.choice(number)

        row9.insert(pos,value)
        unique_lst_row9.append(value)
        col_solve_9.append(value)
        box_solve_9.append(value)

for value,pos in enumerate(row1):
    if value==0: 
        col_solve_1=check_col_solve(pos)
        box_solve_1=check_box_pos(1,pos)
        row1.remove(value)
        value=random.choice(number)
        print(unique_lst_row1,unique_lst_col1,unique_lst_box1)
        while value in unique_lst_row1 or value in col_solve_1 or value in unique_lst_box1:
            print(value)
            value=random.choice(number)

        row1.insert(pos,value)
        unique_lst_row1.append(value)
        col_solve_1.append(value)
        box_solve_1.append(value)

for value,pos in enumerate(row2):
    if value==0:
        col_solve_2=check_col_solve(pos)
        box_solve_2=check_box_pos(2,pos)
        row2.remove(value)
        value=random.choice(number)
        while value in unique_lst_row2 or value in unique_lst_col2 or value in unique_lst_box2:
            value=random.choice(number)

        row2.insert(pos,value)
        unique_lst_row2.append(value)
        col_solve_2.append(value)
        box_solve_2.append(value)
    
for value,pos in enumerate(row3):
    if value==0:
        col_solve_3=check_col_solve(pos)
        box_solve_3=check_box_pos(3,pos)
        row3.remove(value)
        value=random.choice(number)
        while value in unique_lst_row3 or value in unique_lst_col3 or value in unique_lst_box3:
            value=random.choice(number)

        row3.insert(pos,value)
        unique_lst_row3.append(value)
        col_solve_3.append(value)
        box_solve_3.append(value)

for value,pos in enumerate(row4):
    if value==0:
        col_solve_4=check_col_solve(pos)
        box_solve_4=check_box_pos(4,pos)
        row4.remove(value)
        value=random.choice(number)
        while value in unique_lst_row4 or value in unique_lst_col4 or value in unique_lst_box4:
            value=random.choice(number)

        row4.insert(pos,value)
        unique_lst_row4.append(value)
        col_solve_4.append(value)
        box_solve_4.append(value)

for value,pos in enumerate(row5):
    if value==0:
        col_solve_5=check_col_solve(pos)
        box_solve_5=check_box_pos(5,pos)
        row5.remove(value)
        value=random.choice(number)
        while value in unique_lst_row5 or value in unique_lst_col5 or value in unique_lst_box5:
            value=random.choice(number)

        row5.insert(pos,value)
        unique_lst_row5.append(value)
        col_solve_5.append(value)
        box_solve_5.append(value)

for value,pos in enumerate(row6):
    if value==0:
        col_solve_6=check_col_solve(pos)
        box_solve_6=check_box_pos(6,pos)
        row6.remove(value)
        value=random.choice(number)
        while value in unique_lst_row6 or value in unique_lst_col6 or value in unique_lst_box6:
            value=random.choice(number)

        row6.insert(pos,value)
        unique_lst_row6.append(value)
        col_solve_6.append(value)
        box_solve_6.append(value)

for value,pos in enumerate(row7):
    if value==0:
        col_solve_7=check_col_solve(pos)
        box_solve_7=check_box_pos(7,pos)
        row7.remove(value)
        value=random.choice(number)
        while value in unique_lst_row7 or value in unique_lst_col7 or value in unique_lst_box7:
            value=random.choice(number)

        row7.insert(pos,value)
        unique_lst_row7.append(value)
        col_solve_7.append(value)
        box_solve_7.append(value)

for value,pos in enumerate(row8):
    if value==0:
        col_solve_8=check_col_solve(pos)
        box_solve_8=check_box_pos(8,pos)
        row8.remove(value)
        value=random.choice(number)
        while value in unique_lst_row8 or value in unique_lst_col8 or value in unique_lst_box8:
            value=random.choice(number)

        row8.insert(pos,value)
        unique_lst_row8.append(value)
        col_solve_8.append(value)
        box_solve_8.append(value)

for value,pos in enumerate(row9):
    if value==0:
        col_solve_9=check_col_solve(pos)
        box_solve_9=check_box_pos(9,pos)
        row9.remove(value)
        value=random.choice(number)
        while value in unique_lst_row9 or value in unique_lst_col9 or value in unique_lst_box9:
            value=random.choice(number)

        row9.insert(pos,value)
        unique_lst_row9.append(value)
        col_solve_9.append(value)
        box_solve_9.append(value)

for value,pos in enumerate(row1):
    if value==0: 
        col_solve_1=check_col_solve(pos)
        box_solve_1=check_box_pos(1,pos)
        row1.remove(value)
        value=random.choice(number)
        print(unique_lst_row1,unique_lst_col1,unique_lst_box1)
        while value in unique_lst_row1 or value in col_solve_1 or value in unique_lst_box1:
            print(value)
            value=random.choice(number)

        row1.insert(pos,value)
        unique_lst_row1.append(value)
        col_solve_1.append(value)
        box_solve_1.append(value)

for value,pos in enumerate(row2):
    if value==0:
        col_solve_2=check_col_solve(pos)
        box_solve_2=check_box_pos(2,pos)
        row2.remove(value)
        value=random.choice(number)
        while value in unique_lst_row2 or value in unique_lst_col2 or value in unique_lst_box2:
            value=random.choice(number)

        row2.insert(pos,value)
        unique_lst_row2.append(value)
        col_solve_2.append(value)
        box_solve_2.append(value)
    
for value,pos in enumerate(row3):
    if value==0:
        col_solve_3=check_col_solve(pos)
        box_solve_3=check_box_pos(3,pos)
        row3.remove(value)
        value=random.choice(number)
        while value in unique_lst_row3 or value in unique_lst_col3 or value in unique_lst_box3:
            value=random.choice(number)

        row3.insert(pos,value)
        unique_lst_row3.append(value)
        col_solve_3.append(value)
        box_solve_3.append(value)

for value,pos in enumerate(row4):
    if value==0:
        col_solve_4=check_col_solve(pos)
        box_solve_4=check_box_pos(4,pos)
        row4.remove(value)
        value=random.choice(number)
        while value in unique_lst_row4 or value in unique_lst_col4 or value in unique_lst_box4:
            value=random.choice(number)

        row4.insert(pos,value)
        unique_lst_row4.append(value)
        col_solve_4.append(value)
        box_solve_4.append(value)

for value,pos in enumerate(row5):
    if value==0:
        col_solve_5=check_col_solve(pos)
        box_solve_5=check_box_pos(5,pos)
        row5.remove(value)
        value=random.choice(number)
        while value in unique_lst_row5 or value in unique_lst_col5 or value in unique_lst_box5:
            value=random.choice(number)

        row5.insert(pos,value)
        unique_lst_row5.append(value)
        col_solve_5.append(value)
        box_solve_5.append(value)

for value,pos in enumerate(row6):
    if value==0:
        col_solve_6=check_col_solve(pos)
        box_solve_6=check_box_pos(6,pos)
        row6.remove(value)
        value=random.choice(number)
        while value in unique_lst_row6 or value in unique_lst_col6 or value in unique_lst_box6:
            value=random.choice(number)

        row6.insert(pos,value)
        unique_lst_row6.append(value)
        col_solve_6.append(value)
        box_solve_6.append(value)

for value,pos in enumerate(row7):
    if value==0:
        col_solve_7=check_col_solve(pos)
        box_solve_7=check_box_pos(7,pos)
        row7.remove(value)
        value=random.choice(number)
        while value in unique_lst_row7 or value in unique_lst_col7 or value in unique_lst_box7:
            value=random.choice(number)

        row7.insert(pos,value)
        unique_lst_row7.append(value)
        col_solve_7.append(value)
        box_solve_7.append(value)

for value,pos in enumerate(row8):
    if value==0:
        col_solve_8=check_col_solve(pos)
        box_solve_8=check_box_pos(8,pos)
        row8.remove(value)
        value=random.choice(number)
        while value in unique_lst_row8 or value in unique_lst_col8 or value in unique_lst_box8:
            value=random.choice(number)

        row8.insert(pos,value)
        unique_lst_row8.append(value)
        col_solve_8.append(value)
        box_solve_8.append(value)

for value,pos in enumerate(row9):
    if value==0:
        col_solve_9=check_col_solve(pos)
        box_solve_9=check_box_pos(9,pos)
        row9.remove(value)
        value=random.choice(number)
        while value in unique_lst_row9 or value in unique_lst_col9 or value in unique_lst_box9:
            value=random.choice(number)

        row9.insert(pos,value)
        unique_lst_row9.append(value)
        col_solve_9.append(value)
        box_solve_9.append(value)

print("Solved Sudoku-\n")
print(f"{row1[0]} {row1[1]} {row1[2]} | {row1[3]} {row1[4]} {row1[5]} | {row1[6]} {row1[7]} {row1[8]}")
print(f"{row2[0]} {row2[1]} {row2[2]} | {row2[3]} {row2[4]} {row2[5]} | {row2[6]} {row2[7]} {row2[8]}")
print(f"{row3[0]} {row3[1]} {row3[2]} | {row3[3]} {row3[4]} {row3[5]} | {row3[6]} {row3[7]} {row3[8]}")
print("---------------------")
print(f"{row4[0]} {row4[1]} {row4[2]} | {row4[3]} {row4[4]} {row4[5]} | {row4[6]} {row4[7]} {row4[8]}")
print(f"{row5[0]} {row5[1]} {row5[2]} | {row5[3]} {row5[4]} {row5[5]} | {row5[6]} {row5[7]} {row5[8]}")
print(f"{row6[0]} {row6[1]} {row6[2]} | {row6[3]} {row6[4]} {row6[5]} | {row6[6]} {row6[7]} {row6[8]}")
print("---------------------")
print(f"{row7[0]} {row7[1]} {row7[2]} | {row7[3]} {row7[4]} {row7[5]} | {row7[6]} {row7[7]} {row7[8]}")
print(f"{row8[0]} {row8[1]} {row8[2]} | {row8[3]} {row8[4]} {row8[5]} | {row8[6]} {row8[7]} {row8[8]}")
print(f"{row9[0]} {row9[1]} {row9[2]} | {row9[3]} {row9[4]} {row9[5]} | {row9[6]} {row9[7]} {row9[8]}")