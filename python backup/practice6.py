import random
print("Please Enter The Value Of A")
A=int(input())
print("Please Enter The Value Of B")
B=int(input())
C=random.randint(A,B)
i=1
j=1
list1=[]
while True:
  print(" Player 1:")
  print(f"Please Guess The Number Between {A} and {B}")
  G=int(input())
  if G==C:
     print(f"Correct, You Took {i} Trial")
     list1.append(i)
     break
  else:
      if G<=C:
          print("Wrong,Guess a greater number Again")
      else:
          print("Wrong,Guess a smaller number Again")
      i+=1
      continue

print("\n")
while True:
  print(" Player 2:")
  print(f"Please Guess The Number Between {A} and {B}")
  G=int(input())
  if G==C:
     print(f"Correct, You Took {j} Trial")
     list1.append(j)
     break
  else:
      if G<=C:
          print("Wrong,Guess a greater number Again")
      else:
          print("Wrong,Guess a smaller number Again")
      j+=1
      continue

print("\n")
if list1[0]<=list1[1]:
    print(f"Player 1 is the Winner, Because Player 1: Took {i} And Player 2: Took {j} Trial")
elif list1[0]>=list1[1]:
    print(f"Player 2 is the Winner, Because Player 2: Took {j} And Player 1: Took {i} Trial")
else:
    print("Game result is Tie")
