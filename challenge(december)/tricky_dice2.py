
import matplotlib.pyplot as plt
import csv

def make_int(data):

    final_data = []
    for x in data:
        for element in x:
            final_data.append(int(element))
    return final_data


file = open("tricky.csv")
reader = csv.reader(file)
data = []
for row in reader:
    data.append(row)

data = make_int(data)

data10 = []
for x in range(1, len(data), 3):
    data10.append(data[x])

plt.hist(data10, 6, rwidth=0.9)
plt.grid(True)
plt.xlabel("values ")
plt.ylabel("frequency")
plt.title("tricky every 3. number(from second)")
plt.show()


print(data10[:10])