import random
import csv

variance = 0                  # variance of the generated random numbers
data = []
average_number = 0            # the average value of random numbers
y = 0
for k in range(0, 20):                              # k is an index
    data.append([round(y, 2)])                      # creating subintervals and 2d list
    y += 0.05
    data[k].append(0)
    data[k].append(0)                               # filling with beginning values
    data[k].append(0)

for i in range(10**4):
    number = random.random()
    k = int(number*20)
    data[k][1] += 1                 # counting the number of random numbers falling into each subinterval
    data[k][2] += number

for k in range(20):
    data[k][2] = data[k][2] / data[k][1]    # the average value of random numbers falling in the subintervals
    data[k][2] = round(data[k][2], 4)

for a in range(20):
    average_number += data[a][2]            # average random number counted from the subinterval's averages
average_number = average_number/20

for k in range(20):
    data[k][3] = round((data[k][2] - average_number)**2, 5)      # variance of each subinterval
    variance += data[k][3]
variance = variance/19


headers = ["subintervals", "count", "average", "average variance"]              # headers of the file

with open("RandomData.csv", "w") as file:
    writer = csv.writer(file)                                                   # creating a CSV file
    writer.writerow(headers)
    writer.writerows(data)
