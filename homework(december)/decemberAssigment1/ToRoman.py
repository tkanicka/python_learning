def ToRoman(number):

    if number <= 0 or type(number) not in [int]:
        raise ValueError("your input needs to be an positive integer")
    elif number > 3999:
        raise ValueError("Your input must not exceed the value of 3000 ")

    integers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    roman_number = ''

    for i in range(len(integers)):
        while number >= integers[i]:
            roman_number += romans[i]
            number -= integers[i]

    return roman_number


number = int(input(" give me a positive integer not exceeding the value of 3999: "))

print(ToRoman(number))