<<<<<<< HEAD
def rhomb(x):
    a = "*"
    b = "-"
    n = int((x-1)/2)      # half of the rhomb
    y = 1
    z = n
    pattern = z*b + y*a + z*b
    middle_row = x*a         # pattern for the full row

    for i in range(0, n):
        print(pattern)
        z -= 1
        y += 2                              # adds stars in first half
        pattern = z*b + y*a + z*b

    print(middle_row)

    z = x-2
    y = 1
    pattern = y*b + z*a + y*b

    for i in range(0, n):
        print(pattern)
        y += 1                                    # removes stars in second half
        z -= 2
        pattern = y*b + z*a + y*b


x = int(input("field size(just odd numbers): "))
if x < 0:
    print("what makes you think I could possibly want a negative input?!")
    x = int(input("Try to use your brain next time(if you have one) and give me a positive number, jackass!: "))

rhomb(x)

=======
def rhomb(x):
    a = "*"
    b = "-"
    n = int((x-1)/2)      # half of the rhomb
    y = 1
    z = n
    pattern = z*b + y*a + z*b
    middle_row = x*a         # pattern for the full row

    for i in range(0, n):
        print(pattern)
        z -= 1
        y += 2                              # adds stars in first half
        pattern = z*b + y*a + z*b

    print(middle_row)

    z = x-2
    y = 1
    pattern = y*b + z*a + y*b

    for i in range(0, n):
        print(pattern)
        y += 1                                    # removes stars in second half
        z -= 2
        pattern = y*b + z*a + y*b


x = int(input("field size(just odd numbers): "))
if x < 0:
    print("what makes you think I could possibly want a negative input?!")
    x = int(input("Try to use your brain next time(if you have one) and give me a positive number, jackass!: "))

rhomb(x)

>>>>>>> 599bc3afc62b2f337cfca2794bff30547fa5f38e
