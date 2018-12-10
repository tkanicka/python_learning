def toArabic(roman):
    if type(roman) not in [str]:
        raise ValueError("your input needs to be a string")


    numerals = [(1, "I"), (4, "IV"), (5, "V"), (9, "IX"), (10, "X"), (40, "XL"), (90, "XC"), (100, "C"), (400, "CD"),
                (500, "D"), (900, "CM"), (1000, "M")]
