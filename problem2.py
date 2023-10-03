#2. Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

dict1 = {}    #empty dictionary.

for letter in range(ord('a'), ord('z') + 1):
    dict1[chr(letter)] = letter

print("ASCII dictionary is:",dict1)


