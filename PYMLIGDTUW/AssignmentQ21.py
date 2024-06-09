#Write a python program that counts the occurrences of a specific element in a list.
list = [1, 2, 3, 4, 1, 1, 2, 3, 4, 5]

count = 1

count1 = 0
for item in list:
    if item == count:
        count1 += 1

print(f"The element {count} occurs {count1} times in the list.")
