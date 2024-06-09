#Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
operators=input("Enter the operator:+,-,*,/:")
if operators == "+":
    print("The sum of two numbers is:",a+b)
elif operators == "-":
    print("The result after subtraction is:",a-b)
elif operators=="*":
    print("The product of two numbers is:",a*b)
elif operators=="/":
    print("The division of two numbers is:",a/b)
else:
    print("invalid operator")