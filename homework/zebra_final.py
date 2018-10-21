def zebra_final(x,y,z):
    a="/"
    b="-"
    pattern=x*(a,)+x*(b,)
    n=0
    while n<z:
        for i in range(0,y):
            print(pattern[i % len(pattern)], end='')
        n+=1
        print("\n")

x=int(input("give me a number of characters for the strips:" ))
y=int(input("give me a number of characters for the rows:" ))
z=int(input("give me a number of rows:" ))
zebra_final(x,y,z)