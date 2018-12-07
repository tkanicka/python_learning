def ToRoman(number):
    if number <= 0 or type(number) not in [int]:
        raise ValueError("your input needs to be an positive integer")
    elif number > 3999:
        raise ValueError("Your input must not exceed the value of 3000 ")

    numerals = [(1, "I"), (4, "IV"), (5, "V"), (9, "IX"), (10, "X"), (40, "XL"), (90, "XC"), (100, "C"), (400, "CD"),
                (500, "D"), (900, "CM"), (1000, "M")]

print(ToRoman(10000))