import random
import matplotlib.pyplot as plt
import math


def TossDie_regular():
    x = random.randint(1, 6)
    return x


def TossDie_influenced1():
    x = random.sample([1, 1, 2, 2, 3, 3, 4, 5, 6], 1)   # sample(values, k): Chooses k unique random elements
    return x[0]                                         # from a sequence or set and creates a new list from them

def TossDie_influenced2():

    random_value = random.random()
    if random_value <= 0.6:
        x = random.randint(1, 3)
        return x
    else:
        x = random.randint(4, 6)
        return x


def TossDie_influenced3():

    probability = [6/21, 5/21, 4/21, 3/21, 2/21, 1/21]
    probability_sum = 0
    x = 1
    random_determination = random.random()

    for value in probability:
        probability_sum += value                        # smaller die values have larger range in interval(0, 1)s
        if random_determination <= probability_sum:     # according to which interval the random number falls it
            return x                                    # it assigns value to the toss die
        x += 1

def TossDie_influenced4():
    _lambda = 0.5
    probability = []

    for y in range(1, 7):
        p = _lambda * math.exp(- _lambda * y)  # probability of exponential distribution
        probability.append(p)

    sp = 0
    for i in probability:
        sp += i

    probability_sum = 0
    x = 1
    random_determination = random.uniform(0, sp)

    for value in probability:
        probability_sum += value
        if random_determination <= probability_sum:
            return x
        x += 1


def TossDie_infliencedExp():

    return random.randint(1, TossDie_regular())


def TossFiveSideDie_uniform():

    while True:
        x = TossDie_regular()

        if x <= 5:
            return x


def TossSevenSideDie_uniform():

    # function returning uniformly random 2 bits of entropy as 1 to 4
    def TwoRandomBits():

        while True:
            x = TossDie_regular()
            if x <= 4:
                return x - 1

    while True:
        # random numbers from 0 to 15 (4 bits of entropy)
        largerUniformRandomNumber = (TwoRandomBits() << 2) | TwoRandomBits()

        if largerUniformRandomNumber <= 6:
            return largerUniformRandomNumber + 1


def plot_histogram(functionName, n = 6):

    generated_values = []
    for i in range(10**4):
        generated_values.append(functionName())
    plt.hist(generated_values, n, rwidth=0.9)
    plt.grid(True)
    plt.xlabel("values")
    plt.ylabel("number of generated values")
    plt.title("die toss distribution")
    plt.show()


print(TossDie_regular())
print(TossDie_influenced1())
print(TossDie_influenced2())
print(TossDie_influenced3())
print(TossDie_influenced4())

print(TossDie_infliencedExp())
print(TossFiveSideDie_uniform())
print(TossSevenSideDie_uniform())

plot_histogram(TossDie_regular)
plot_histogram(TossDie_influenced1)
plot_histogram(TossDie_influenced2)
plot_histogram(TossDie_influenced3)
plot_histogram(TossDie_influenced4)

plot_histogram(TossDie_infliencedExp)
plot_histogram(TossFiveSideDie_uniform, 5)
plot_histogram(TossSevenSideDie_uniform, 7)

