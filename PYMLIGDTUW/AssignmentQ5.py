user=input("enter the input:")
file="output.txt"
with open(file,"w") as f:
    f.write(user)
print("The input has been written to",file)