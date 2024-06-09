#Write a python program that calculates the factorial of a given number.
n=int(input("enter an integer:"))
factorial=1
for i in range(1,n+1):
    factorial*=i
print("The factorial of",n,"is",factorial)