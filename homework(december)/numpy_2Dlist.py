import numpy
row = int(input("give me a number of rows: "))
column = int(input("give me a number of rows: "))

a = numpy.zeros(shape=(row, column))

print(a)
print("\n")

for y in range(0, row):
    v = y*column
    x = (y+1) * column
    c = []
    for z in range(v, x):
        c.append(z)
    a[y] = c

print(a)
