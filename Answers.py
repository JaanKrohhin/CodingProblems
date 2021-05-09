from random import randint
## Problem 1: "How do you reverse a given string in place without using a loop only?"
def one():
    a = str(input("Type a word to reverse --- "))
    aray = list(a)
    if " " in aray:
        aray.pop(aray.index(" "))
    aray.reverse()
    print(aray)

## Problem 2: How do you check if a given string is a palindrome?  (e.g. “Taco cat”)
def two():
    a = str(input("Type a word to check if it is a palindrome --- "))
    aray = list(a)
    if " " in aray:
        aray.pop(aray.index(" "))
    aray2 = aray.copy()
    aray.reverse()
    for i in range(len(aray)):
        if aray[i] != aray2[i]:
            print("This word is not a palindrome.")
            break
        elif aray[i] == aray2[i] and i==len(aray)-1:
            print("This word is a palindrome.")

## Problem 3: Write a program to display the multiplication table of a given integer.
def three():
    print("Type an integrer to display its multiplication table")
    a = 0.0
    while type(a) != int:
        try:
            a = int(input("Integrer --- "))
        except:
            TypeError
    for j in range(1,11):
        print(f"{j} * {a} = {a*j}")

## Problem 4: Write a program to find the maximum and minimum element in an array. 
def four():
    aray = []
    for i in range(5):
        aray.append(randint(1,99))
    print("Created a list with 5 randomly generated numbers\n",aray)
    aray.sort()
    print(f"The largest element is {aray[-1]}\nThe smallest element is {aray[0]}")

## Problem 5: Write a program to find the largest of three given (input) numbers. (e.g. 8, 6, 10 → 10)
def five():
    print("Type 3 numbers to find out which one is the largest")
    aray = []
    for i in range(3):
        a = 0.0
        while type(a) != int:
            try:
                a = int(input(f"Number {i+1} --- "))
            except:
                TypeError
        aray.append(a)
    print("The largest number of the three is ",max(aray))

## Problem 6: Write a program to calculate the sum of elements in an array. (e.g. 1234 → 1 + 2 + 3 + 4 → 10)
def six():
    aray = []
    for i in range(4):
        aray.append(randint(0,9))
    print("Created a list with 4 randomly generated numbers",aray,f"\nThe sum of the elements is {sum(aray)}")
    

## Problem 7: Write a program to output a pyramid-like pattern  with an asterisk.
def seven():
    print("A cute little pyramid")
    a = 3
    for i in range(a):
            row = '*' * (2*i+1)
            print (row.center(2*a))

## Problem 8: Write a program to check if a given number is odd or even. Return “odd” if the number is odd, or “even” if the number is even.
def eight():
    print("Type a number to check if it is even or odd")
    a = 0.0
    while type(a) != int:
        try:
            a = int(input("Number to check --- "))
        except:
            TypeError
    if a%2==0:
        print("Even")
    else:
        print("Odd")

while True:
    print("Type the problem number to see the code in action. Type the number 9 to display the problems.")
    a = 0.0
    while type(a) != int or 9<a<1:
        try:
            a = int(input("Your choice (1-9) --- "))
        except:
            TypeError
    if a==1: one()
    elif a==2: two()
    elif a==3: three()
    elif a==4: four()
    elif a==5: five()
    elif a==6: six()
    elif a==7: seven()
    elif a==8: eight()
    elif a==9:
        print('''Problem 1: How do you reverse a given string in place without using a loop only?
        \nProblem 2: How do you check if a given string is a palindrome?  (e.g. “Taco cat”)
        \nProblem 3: Write a program to display the multiplication table of a given integer.
        \nProblem 4: Write a program to find the maximum and minimum element in an array.
        \nProblem 5: Write a program to find the largest of three given (input) numbers. (e.g. 8, 6, 10 → 10)
        \nProblem 6: Write a program to calculate the sum of elements in an array. (e.g. 1234 → 1 + 2 + 3 + 4 → 10)
        \nProblem 7: Write a program to output a pyramid-like pattern  with an asterisk.
        \nProblem 8: Write a program to check if a given number is odd or even. Return “odd” if the number is odd, or “even” if the number is even.''')
    print()
    