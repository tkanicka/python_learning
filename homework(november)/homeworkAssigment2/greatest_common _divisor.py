<<<<<<< HEAD
x = int(input("first number: "))
y = int(input("second number: "))
def GCD(x,y):
    smallerNumber = min(abs(x),abs(y))
    for divisor in range(1,smallerNumber + 1):
        if x % divisor == 0 and y % divisor == 0:
           gcd = divisor
    return gcd

def GCD_recursion(x,y):

    higher_number = max(abs(x), abs(y))
    smaller_number = min(abs(x), abs(y))

    if higher_number % smaller_number == 0:
        return smaller_number                   # example(15;9): 15%9 = 6 -> 9%6 = 3 -> 6%3 = 0 => 15,9,6,3 % 3 = 0

    else:
        return GCD_recursion(smaller_number, higher_number % smaller_number)

print(" greatest common divisor of your imputs is: ", GCD(x,y),",", GCD_recursion(x,y))


=======
x = int(input("first number: "))
y = int(input("second number: "))
def GCD(x,y):
    smallerNumber = min(abs(x),abs(y))
    for divisor in range(1,smallerNumber + 1):
        if x % divisor == 0 and y % divisor == 0:
           gcd = divisor
    return gcd

def GCD_recursion(x,y):
    if x == 0:
        return y                        # example 0 % 5; 5%5 = 0
    elif y == 0:
        return x

    higher_number = max(abs(x), abs(y))
    smaller_number = min(abs(x), abs(y))

    if higher_number % smaller_number == 0:
        return smaller_number                   # example(15;9): 15%9 = 6 -> 9%6 = 3 => 15,9,6,3 % 3 = 0

    else:
        return GCD_recursion(smaller_number, higher_number % smaller_number)

print(" greatest common divisor of your imputs is: ", GCD(x,y),",", GCD_recursion(x,y))


>>>>>>> 529875bd0eecec1fb0fec78c7a55efa210122850
