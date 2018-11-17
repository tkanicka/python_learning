x = int(input("first number: "))
y = int(input("second number: "))
def LCM(x,y):
    startingNumber = max(abs(x),abs(y))
    for multiple in range(startingNumber,abs(x*y) + 1,startingNumber):
        if multiple % x == 0 and multiple % y == 0:
            return multiple


def GCD_recursion(x,y):

    higher_number = max(abs(x), abs(y))
    smaller_number = min(abs(x), abs(y))

    if higher_number % smaller_number == 0:
        return smaller_number

    else:
        return GCD_recursion(smaller_number, higher_number % smaller_number)

def LCM_factorization(x,y):
    return int((x*y)/(GCD_recursion(x,y)))

print("lest common multiple of your imputs is: ", LCM(x,y),", ", LCM_factorization(x,y))

'''explanation:
    example: 6(2*3), 15(3*5) 
            gcd is the common part of their prime factorization...3
            lcm is the higher number* uncommon part of smaller number... (3*5)*2 = 30
            so when we multiply 6*15(2*3*3*5) and divide it by their gcd(3...common part) we get lcm(2*3*5)'''