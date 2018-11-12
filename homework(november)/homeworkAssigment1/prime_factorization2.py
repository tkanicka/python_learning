def primeFactorization(x):
    def is_prime(x):
        if x % 2 == 0:
            return False
        for y in range(3, int(x ** 0.5) + 1, 2):    # check if input is a composite number
            if x % y == 0:
               return False

        return True

    is_prime(x)

    if is_prime(x) == True:
        print(int(x))
    elif is_prime(x) == False :
        for y in range (2,int(x+1)):
            if x%y == 0 :
                print(y,"*",end="")
                x=x/y
                primeFactorization(x)
                break


x=int(input("give me an integer: "))
print(primeFactorization(x))