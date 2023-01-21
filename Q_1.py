# 1. A school has following rules for grading system: 
#     a. Below 25 - F 
#     b. 25 to 45 - E 
#     c. 45 to 50 - D 
#     d. 50 to 60 - C 
#     e. 60 to 80 - B 
#     f. Above 80 - A 
#    Ask user to enter marks and print the corresponding grade.

marks = int(input("Enter your marks\n"))

if marks>80:
    print("You got A grade")

elif marks>60 & marks<=80:
    print("You got B grade")

elif marks>50 & marks<=60:
    print("You got C grade")

elif marks>45 & marks<=50:
    print("You got D grade")

elif marks>25 & marks<=45:
    print("You got E grade")

else:
    print("You got F grade")

