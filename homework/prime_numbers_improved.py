def is_prime(x):
    for y in range(3,int(x**0.5)+1,2):
        if x%y==0:
            return False
        else:
            continue
    return True

x= int(input("give me an integer: "))
print(is_prime(x))

