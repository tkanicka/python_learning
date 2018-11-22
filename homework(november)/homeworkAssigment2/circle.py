def print_circle(r):
    d = 2*r

    for horizontal in range(d+1):
        for vertical in range(d+1):
            circuit_distance = ((horizontal - r)**2 + (vertical - r)**2)**0.5           # distance  will be +/- some number

            if (circuit_distance > r - 1 and circuit_distance < r + 1):  # making a tolerance
                print("*", end = " ")
            else:
                print(" ", end = " ")

        print()         # goes to another line without making extra space


r = int(input("give me your radius: "))
print_circle(r)


