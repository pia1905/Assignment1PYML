#Write a python program that generates the first n numbers in the Fibonacci sequence.
n = int(input("Enter the number of Fibonacci numbers to generate: "))


fib = [0, 1]

for i in range(2, n):
    next= fib[-1] + fib[-2]
    fib.append(next)

print(f"The first {n} numbers in the Fibonacci sequence are:")
print(fib[:n])
