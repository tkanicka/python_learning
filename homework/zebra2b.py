def zebra_2(x):
    pattern=["/","/","/","-","-","-"]
    y=0
    while y<x:
        for i in range(0,x):
            print(pattern[i % len(pattern)], end='')
        y+=1
        print("\n")


x=int(input("give me a number of charcters for the rows and collums:" ))
zebra_2(x)