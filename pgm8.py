Write a python program to check whether a number is divisible by 3 or not
Code
number = int(input("Enter a number: "))
if number % 3 == 0:
    print(f"{number} is divisible by 3.")
else:
    print(f"{number} is not divisible by 3.")
Output
Enter a number: 9
9 is divisible by 3.