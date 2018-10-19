def zebra_2(x,y):
    pattern=["/","/","/","-","-","-"]
    z=0
    while z<y:
        for i in range(0,x):
            print(pattern[i % len(pattern)], end='')
        z+=1
        print("\n")
x=int(input("give me a number of charcters in the row:" ))
y=int(input("give me a number of rows:" ))
zebra_2(x,y)
