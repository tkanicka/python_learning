import math
import matplotlib.pyplot as graph
import random

#  Fx(x): y = 1 - e^(-_lambda*x)  y ∈ (0,1) X = Fx^-1(y) X = -(1/_lambda) * log(x)

_lambda = 10
uniform_numbers = []

for i in range(10**4):
    number = random.random()
    uniform_numbers.append(number)


def to_exp(y, _lambda):

    X = -(1/_lambda) * math.log(y)
    return X


exp_numbers = []

for y in uniform_numbers:
    exp_numbers.append(to_exp(y, _lambda))


exp_numbers.sort()
print(exp_numbers)


graph.hist(exp_numbers, 20, rwidth=0.9)
graph.grid(True)
graph.xlabel("value of X")
graph.ylabel("number of generated numbers")
graph.title("random numbers distribution")
graph.show()



