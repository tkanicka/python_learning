class CreateList:

    def __init__(self, size):
        self.list = []
        for number in range(size):
            self.list.append(number)

    def call_value(self, x):
        print(self.list[x])

    def print_list(self):
        print(self.list)


class CreateList2D(CreateList):

    def make_2d(self, step):
        list_2d = []
        for i in range(0, len(self.list), step):
            list_2d.append(self.list[i: i + step])
        self.list = list_2d

    def call_value(self, x, y):
        print(self.list[x][y])

    def print_2d(self):

        for rows in self.list:
            for column in rows:
                print(column, end="")
            print()


list1 = CreateList(10)
list1.print_list()
list1.call_value(2)

list2 = CreateList2D(10)
list2.make_2d(3)
list2.print_list()
list2.call_value(2, 2)

print("\n")

list2.print_2d()
