def print_circle(r):
    d = 2*r

    for column in range(d+1):
        for row in range(d+1):
            circuit_distance = ((column - r)**2 + (row - r)**2)**0.5          

            if (circuit_distance > r - 0.5 and circuit_distance < r + 0.5):  # making a tolerance so the distance is +- r
                print("*", end = " ")
            else:
                print(" ", end = " ")

        print()         # goes to another line without making extra space


r = int(input("give me your radius: "))
print_circle(r)


