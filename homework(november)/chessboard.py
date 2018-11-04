def chessboard(x,y):
    a = "*"
    b = "-"
    z=x*y    #number of characters in a row/number of rows(in characters)
    patternA = x*a + x*b
    patternB = x*b + x*a

    rowNumber = 0
    while rowNumber < y:
        nA = 0  #number of rows in one field(patternA)
        nB = 0  #number of rows in one field(patternB)
        while nA < x:
            for i in range(0,z):
                print(patternA[i % len(patternA)], end='   ')       # The free spaces are there to make it look a bit more square shaped...
            nA += 1
            print("\n")                                             # makes y fields in one row

        rowNumber += 1

        if rowNumber < y:
            while nB < x:
                for i in range(0,z):
                    print(patternB[i % len(patternB)], end='   ')   # other row in opposite order
                nB += 1
                print("\n")

        rowNumber += 1


x=int(input("field size:" ))
y=int(input("chessboard size(number of fields in one row: " ))
chessboard(x,y)