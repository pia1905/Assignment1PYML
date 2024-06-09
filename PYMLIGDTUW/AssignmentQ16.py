#Write a program in python that counts the frequency of each character in a string.
# Get user input
string = input("Enter a string: ")

frequency = {}

for i in string:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print("Character frequencies:")
for char, freq in frequency.items():
    print(f"{char}: {freq}")
