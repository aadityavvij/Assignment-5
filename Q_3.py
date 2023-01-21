# 3. Write a multiplication game program for kids. The program should give the player 
#    ten randomly generated multiplication questions to do. After each, the program 
#    should tell them whether they got it right or wrong and what the correct answer is. 
#     Question 1: 3 x 4 = 12 
#     Right! 
#     Question 2: 8 x 6 = 44 
#     Wrong. The answer is 48. 
#     ... 
#     ... 
#     Question 10: 7 x 7 = 49 
#     Right.

import random

i=0

string = "123456789"

r = 0
w = 0

while i<10:
    a = int(random.choice(string))
    b = int(random.choice(string))
    ans = int(input(f"Question {i+1}:  {a} x {b} = "))

    if (ans==a*b):
        print("Right.\n")
        r = r+1
    else:
        print(f"Wrong. The answer is {a*b}\n")
        w = w+1

    i = i+1

print(f"You scored {r*10}%")