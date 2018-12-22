import numpy
import random

variance = 0                  # variance of the generated random numbers
random_numbers = []           # list of random numbers for the histogram
data = numpy.zeros((20, 4))   # 2D list for dividing values into the subintervals(filled with zeros in the beginning)
average_number = 0            # the average value of random numbers
print(data)
for k in range(1, 20):                              # k is an index
    data[k][0] = round(data[k-1][0] + 0.05, 2)      # creating subintervals

for i in range(10**4):
    number = random.random()
    k = int(number*20)
    data[k][1] += 1                 # counting the number of random numbers falling into each subinterval
    data[k][2] += number
    random_numbers.append(number)

for k in range(20):
    data[k][2] = data[k][2] / data[k][1]    # the average value of random numbers falling in the subintervals
    data[k][2] = round(data[k][2], 4)

for a in range(20):
    average_number += data[a][2]            # average random number counted from the subinterval's averages
average_number = average_number/20

for k in range(20):
    data[k][3] = round((data[k][2] - average_number)**2, 4)      # variance of each subinterval
    variance += data[k][3]
variance = variance/19

numpy.savetxt("random.csv", data, delimiter=", ", header="sub intervals, count, average, variance")
