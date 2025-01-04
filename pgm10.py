Write a python program to check a number lies in a range
Code.
number = int(input("Enter a number: "))
if 1 <= number <= 100:
    print(f"{number} lies within the range of 1 to 100.")
else:
    print(f"{number} is outside the range.")
Output
Input: 50  
Output: 50 lies within the range of 1 to 100.