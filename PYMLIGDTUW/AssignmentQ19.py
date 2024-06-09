#Write a python program that removes all punctuation from a given string.
import string
s = input("Enter a string with punctuation: ")
s1 = s.translate(str.maketrans('', '', string.punctuation))


print("String without punctuation:", s1)
