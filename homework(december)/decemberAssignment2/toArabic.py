roman = str(input("give me a roman numeral: "))
roman.upper()


def toArabic(roman):

    if type(roman) not in [str]:
        raise ValueError("your input needs to be a string")

    result = 0
    roman = "n" + roman

    for i in range(1, len(roman)):

        if roman[i] == "M":
            result += 1000
            if roman[i - 1] == "C":
                result -= 200

        elif roman[i] == "D":
            result += 500
            if roman[i - 1] == "C":
                result -= 200

        elif roman[i] == "C":
            result += 100
            if roman[i - 1] == "X":
                result -= 20

        elif roman[i] == "L":
            result += 50
            if roman[i - 1] == "X":
                result -= 20

        elif roman[i] == "X":
            result += 10
            if roman[i - 1] == "I":
                result -= 2

        elif roman[i] == "I":
            result += 1

        elif roman[i] == "V":
            result += 5
            if roman[i - 1] == "I":
                result -= 2

        elif roman[i] == "I":
            result += 1

    return result


print(toArabic(roman))
