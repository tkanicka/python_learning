import csv
from datetime import datetime

print(dir(csv), "\n")

file = open("data.csv", newline="")
reader = csv.reader(file)

headers = next(reader)


data = []
for row in reader:      # row = [date, str, int, str, str, date, float, float]
    Transaction_date = datetime.strptime(row[0], '%m/%d/%Y')                # conversion to individual data types
    Product = str(row[1])
    Price = int(row[2])
    Name = str(row[3])
    Country = str(row[4])
    Last_Login = datetime.strptime(row[5], '%m/%d/%Y')
    Latitude = float(row[6])
    Longitude = float(row[7])

    data.append([Transaction_date, Product, Price, Name, Country, Last_Login, Latitude, Longitude])

print(data, "\n")

for header in headers:
    print(header, end="      ")
print("\n")

for x in data:
    for y in x:
        print(y, end="    ")
    print()

