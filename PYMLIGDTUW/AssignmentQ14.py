#Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.

lines = []

print("Enter your lines. Press Enter on an empty line to finish:")
while True:
    line = input()
    if line == "":
        break
    lines.append(line)

print("Here are the lines you entered:")
for line in lines:
    print(line)
