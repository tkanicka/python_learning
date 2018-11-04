def prime_factorization(x):
    for y in range (2,int(x+1)):
        if x%y == 0 :
            print(y,"*",end="")
            x = x/y
            prime_factorization(x)
            break

x = int(input("give me an integer: "))
print(prime_factorization(x))
