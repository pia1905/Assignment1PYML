#Write a python program that takes a list of numbers and returns their sum
a=list(input("Enter a list of numbers:"))
sum=0
for i in a:
    if i.isdigit():
        sum+=int(i)
print("The sum of numbers present in the list is:",sum)
