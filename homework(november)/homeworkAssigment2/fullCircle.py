def print_circle(r):
    r = abs(r)
    d = 2*r

    for column in range(d+1):
        for row in range(d+1):
            circuit_distance = ((r - column)**2 + (r - row)**2)**0.5

            if r > circuit_distance:
                print("*", end = " ")
            else:
                print(" ", end = " ")

        print()         # goes to another line without making extra space


r = int(input("give me your radius: "))

print_circle(r)

