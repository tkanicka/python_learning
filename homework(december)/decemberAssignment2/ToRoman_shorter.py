def ToRoman_2(number):

    if number <= 0 or type(number) not in [int]:
        raise ValueError("your input needs to be an positive integer")
    elif number > 3999:
        raise ValueError("Your input must not exceed the value of 3000 ")

    numerals = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"),
                (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

    roman_number = ''

    for (integer, roman) in numerals:
        while number >= integer:
            roman_number += roman
            number -= integer

    return roman_number


number = int(input(" give me a positive integer not exceeding the value of 3999: "))

print(ToRoman_2(number))