
class CreateList:

    def __init__(self, size):
        self.list = []
        a = "*"
        b = "-"
        c = "="
        d = "+"
        number = 0
        while number < size:
            n = int((size - 1) / 2)
            outskirt_ch = size - 1
            centre_ch = n

            for j in range(size):
                
                 i= 0
                 
                 while i < size:
                     
                     self.list.append(abs(centre_ch) * b + (size - abs(outskirt_ch)) * a + abs(centre_ch) * b)
                     i += 1
                     if i < size:
                         
                         self.list.append(abs(centre_ch) * d + (size - abs(outskirt_ch)) * c + abs(centre_ch) * d)
                     i += 1
                     
                 outskirt_ch -= 2
                 centre_ch -= 1

            number += 1
            n = int((size - 1) / 2)
            outskirt_ch = size - 1
            centre_ch = n

            if number < size:
                for j in range(size):

                    i = 0

                    while i < size:

                        self.list.append(abs(centre_ch) * d + (size - abs(outskirt_ch)) * c + abs(centre_ch) * d)
                        i += 1
                        if i < size:
                            self.list.append(abs(centre_ch) * b + (size - abs(outskirt_ch)) * a + abs(centre_ch) * b)
                        i += 1

                    outskirt_ch -= 2
                    centre_ch -= 1

    def print_list(self):
        print(self.list)

    def print_len(self):
        print(len(self.list))

    def make_2d(self, step):
        list_2d = []
        for i in range(0, len(self.list), step):
            list_2d.append(self.list[i: i + step])
        self.list = list_2d

    def print_2d(self):

        for rows in self.list:
            for column in rows:
                print(column, end="")
            print()


x = int(input("give me a size(number) of yur field(fields):  "))

if x%2 == 0:
    print("Don't be a jackass and read the instructions for the input!")
    x = int(input("try to be less underdeveloped with your next input!:  "))
elif x < 0:
    print("How the hell even a half-witt like you could think I want an negative integer as an input!")
    x = int(input("try to be less underdeveloped with your next input!:  "))

list1 = CreateList(x)
list1.print_len()
list1.make_2d(x)
list1.print_2d()
