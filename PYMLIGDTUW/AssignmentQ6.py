#Write a program that reads the content of a text file and prints it to the console.
file= "output.txt"
try:
    with open(file, "r") as f:
        content = f.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("The file",file,"does not exist.")