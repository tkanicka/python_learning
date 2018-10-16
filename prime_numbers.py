def is_prime(x):
    y=int(x/2)+1
    while y>1:
        if x%y==0:
            return False
        else:
            y-=2
    return True

x= int(input("give me an integer: "))
print(is_prime(x))

