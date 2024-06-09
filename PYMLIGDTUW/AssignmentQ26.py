#Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
a=input("Enter a string:")
b=input("Enter a prefix:")
c=input("Enter a suffix:")
if a.startswith(b):
    print("The string starts with the prefix",b)
else:
    print("The string does'nt start with the prefix",b)
if a.endswith(c):
    print("The string starts with the suffix",c)
else:
    print("The string does'nt start with the suffix",c)

