x = int(input("first number: "))
y = int(input("second number: "))
def GCD(x,y):
    highestNumber = min(abs(x),abs(y))
    for divisor in range(1,highestNumber + 1):
        if x % divisor == 0 and y % divisor == 0:
           gcd = divisor
    return gcd
print(" greatest common divisor of your imputs is: ", GCD(x,y))