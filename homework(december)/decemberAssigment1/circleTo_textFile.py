r = int(input("give me your radius: "))
d = 2*r
circle = []
for column in range(d + 1):
    for row in range(d + 1):
        circuit_distance = ((column - r)**2 + (row - r)**2)**0.5

        if (circuit_distance > r -  0.5 and circuit_distance < r + 0.5):
            circle.append("*")
        else:
            circle.append(" ")


list_2d = []
step = (2 * r) + 1

for i in range(0, len(circle), step):
    list_2d.append(circle[i: i + step])
circle = list_2d


with open("circle.txt", "w") as c:
    for x in circle:
        for y in x:
            c.write(y)
            c.write(" ")
        c.write("\n")


