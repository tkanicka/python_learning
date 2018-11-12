x = int(input("first number: "))
y = int(input("second number: "))
def LCM(x,y):
    startingNumber = max(abs(x),abs(y))
    for multiple in range(startingNumber,abs(x*y) + 1,startingNumber):
        if multiple % x == 0 and multiple % y == 0:
            return multiple
print("lest common multiple of your imputs is: ", LCM(x,y))