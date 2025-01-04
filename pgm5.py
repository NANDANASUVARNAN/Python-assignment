Write a python program to check a word whether it is pallindrome or not.
Code
word = input("Enter a word: ")
reversed_word = ""
for char in word:
    reversed_word = char + reversed_word
print("Reversed word:", reversed_word)