#Write a program that reads data from a CSV file and prints it to the console
import csv
csv_file = "data.csv"

try:
    with open(csv_file, "r") as file:
        reader = csv.reader(file)
        print("Data from the CSV file:")
        for row in reader:
            print(row)
except FileNotFoundError:
    print(f"The file {csv_file} does not exist.")
