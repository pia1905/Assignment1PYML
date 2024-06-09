#Write a python program that calculates the sum of the digits of a given number
a=input("Enter a number:")
sum=0
for i in a:
    if i.isdigit():
        sum=sum+int(i)
print("the sum of the digits of the  numnber is:",sum)