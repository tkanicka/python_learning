<<<<<<< HEAD
def is_prime(x):
    for y in range(3,int(x**0.5)+1,2):
        if x%y==0:
            return False
        else:
            continue
    return True

x= int(input("give me an integer: "))
print(is_prime(x))

=======
def is_prime(x):
    if x%2 ==0:
        return False
    for y in range(3,int(x**0.5)+1,2):
        if x%y==0:
            return False
        else:
            continue
    return True

x= int(input("give me an integer: "))
print(is_prime(x))


>>>>>>> 2c5305d57565d89bbfa02107a09df73229220870
