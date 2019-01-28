import copy

class Node:
    def __init__(self, value=0):
        self.value = value
        self.next_node = None
        self.previous_node = None


class Chain:
    def __init__(self):
        self.first_node = None
        self.last_node = None

    def printChain(self):
        print_node = self.first_node

        while print_node:

            print(print_node.value)
            print_node = print_node.next_node

    def printChain_backwards(self):
        print_node = self.last_node

        while print_node:

            print(print_node.value)
            print_node = print_node.previous_node

    def pushEnd(self, value=0):
        end_node_pushed = Node(value)

        if self.last_node == None:
            self.last_node = end_node_pushed
            self.first_node = end_node_pushed
        else:
            end_node_pushed.previous_node = self.last_node
            self.last_node.next_node = end_node_pushed
            self.last_node = end_node_pushed

    def popEnd(self):
        if self.last_node.previous_node == None:
            self.last_node = None
            self.first_node = None
        else:
            self.last_node = self.last_node.previous_node
            self.last_node.next_node = None

    def pushFront(self, value=0):

        first_node_pushed = Node(value)

        if self.first_node == None:
            self.first_node = first_node_pushed
            self.last_node = first_node_pushed

        else:
            first_node_pushed.next_node = self.first_node
            self.first_node = first_node_pushed

    def popFront(self):

        if self.first_node.next_node == None:
            self.first_node = None
            self.last_node = None
        else:
            self.first_node = self.first_node.next_node
            self.first_node.previous_node = None

    def size(self):
        count = self.first_node
        size = 0
        while count:
            size += 1
            count = count.next_node

        return size

    def print_size(self):
        print(self.size())

    def __find_node(self, index):

        if self.first_node == None:
            return None

        current_node = self.first_node
        count = 0
        while current_node:
            if count == index:
                return current_node
            count += 1
            current_node = current_node.next_node

    def insert(self, index, value = 0):

        if index != 0 and index > self.size():
            raise ValueError("your index is out of range")

        if index == 0:
            self.pushFront(value)

        elif index == (self.size()-1):
            self.pushEnd(value)

        else:
            current_node = self.first_node
            insert = Node(value)
            count = 0
            previous = None

            while current_node:
                if count == index-1:
                    previous = current_node
                    current_node = current_node.next_node
                    previous.next_node = insert
                    current_node.previous_node = insert
                    insert.next_node = current_node
                    break

                count += 1
                current_node = current_node.next_node

    def erase(self, index):
        if index != 0 and index >= self.size():
            raise ValueError("your index is out of range")

        if self.first_node == None and index == 0:
            raise ValueError("your linked list is already empty")


        if index == 0:
            self.popFront()

        elif index == (self.size()-1):
            self.popEnd()

        else:
            current_node = self.first_node
            count = 0
            previous = None
            nextVal = None

            while count != index:

                count += 1
                current_node = current_node.next_node

            previous = current_node.previous_node
            nextVal = current_node.next_node
            previous.next_node = nextVal
            nextVal.previous_node = previous
            current_node.previous_node = None
            current_node.next_node = None

            del current_node


    def set_value(self, index, value = 0):

        if index != 0 and index >= self.size():
            raise ValueError("your index is out of range")

        if self.first_node == None and index == 0:
            self.first_node = Node(value)

        current_node = self.__find_node(index)

        current_node.value = value

    def get_value(self, index):

        if index != 0 and index >= self.size():
            raise ValueError("your index is out of range")

        current_node = self.__find_node(index)

        if current_node == None:
            return None

        return current_node.value

    def to_pythonList(self):            # making a classic python 1d list of values
        newList = []
        current_node = self.first_node

        while current_node:
            newList.append(current_node.value)
            current_node = current_node.next_node

        return newList

    def swap_nodes(self, index1 = 0, index2 = 1):
        list_size = self.size()

        if self.size() <= 1:
            raise ValueError("you can't swap(your linked list has less than 2 nodes")

        elif index1 >= list_size or index2 >= list_size:
            raise ValueError("your index is out of range")

        elif index1 == index2:
            return None

        current_node1 = self.__find_node(index1)
        current_node2 = self.__find_node(index2)

        value1 = current_node1.value

        current_node1.value = current_node2.value
        current_node2.value = value1

    def check_ifSorted(self):
        current = self.first_node

        while current:

            if current.value <= current.next_node.value:
                continue
            else:
                return False

            current = current.next_node

        return True

    def sort(self):
        list_size = self.size()

        if list_size == 0 or list_size == 1:
            return None

        if self.check_ifSorted()== True:
            return None

        for y in range(0, list_size):
            for x in range(0, list_size):
                current_node = self.__find_node(x)

                if current_node.next_node != None:

                    if current_node.value > current_node.next_node.value:
                        self.swap_nodes(x, x+1)


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)

    node1.next_node = node2
    node2.next_node = node3
    node3.next_node = node4
    node4.next_node = node5

    node2.previous_node = node1
    node3.previous_node = node2
    node4.previous_node = node3
    node5.previous_node = node4

    chain1 = Chain()
    chain1.first_node = node1
    chain1.last_node = node5

    chain1.PrintChain()
    chain1.PrintChain_backwards()

    chain1.pushEnd(6)
    print(chain1.last_node.value)
    print(chain1.last_node.previous_node.value)

