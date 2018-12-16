
size = int(input("give me a size of your 2D list: "))
squareList = [[0] * size] * size

print(squareList)

for x in squareList:
    for y in x:                     # printing out the values in the form of 2d list
        print(y, end=" ")
    print()

print(" a for loop version")

list_square = []
for add_item in range(size):
     list_square.append([0]*size)

print(list_square)
