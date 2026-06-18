# Problem Statement: Develop a Python program to determine whether a given number is even or odd

userInput = int(input("Please Enter a Number: "))
Result = userInput % 2
if Result == 0:
    print("Given Number is a Even Number")
else:
    print("Given Number is an Odd Number")
    