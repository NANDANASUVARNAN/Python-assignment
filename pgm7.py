Write a python program to find the largest of two numbers.
Code
a = int(input("Enter the first number: "))  
b = int(input("Enter the second number: ")) 

if a > b:
    print(f"The larger number is {a}.")
elif a < b:
    print(f"The larger number is {b}.")
else:
    print("Both numbers are equal.")
Output
Enter the first number: 8  
Enter the second number: 12
The larger number is 12.