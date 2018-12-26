import random
import matplotlib.pyplot as plt


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


def plot_histogram(functionName):

    generated_values = []
    for i in range(10**4):
        generated_values.append(functionName())
    plt.hist(generated_values, 6, rwidth=0.9)
    plt.grid(True)
    plt.xlabel("values")
    plt.ylabel("number of generated values")
    plt.title("die toss distribution")
    plt.show()


print(TossDie_regular())
print(TossDie_influenced1())
print(TossDie_influenced2())
print(TossDie_influenced3())

plot_histogram(TossDie_regular)
plot_histogram(TossDie_influenced1)
plot_histogram(TossDie_influenced2)
plot_histogram(TossDie_influenced3)
