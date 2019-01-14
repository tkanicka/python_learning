
class Node:
    def __init__(self, value=0):
        self.value = value
        self.next_node = None
        self.previous_node = None


class Chain:
    def __init__(self):
        self.first_node = None
        self.last_node = None

    def PrintChain(self):
        print_node = self.first_node

        while print_node:

            print(print_node.value)
            print_node = print_node.next_node

    def PrintChain_backwards(self):
        print_node = self.last_node

        while print_node:

            print(print_node.value)
            print_node = print_node.previous_node

    def pushEnd(self, value=0):
        end_node_pushed = Node(value)

        if self.last_node == None:
            self.last_node = end_node_pushed
            self.first_node = end_node_pushed

        end_node_pushed.previous_node = self.last_node
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

        print("your linked list size is: ", size)
        return size

    def insert(self, index, value = 0):
        return None

    def erase(self, index,):
        return None

    def set_value(self, index, value = 0):

        if index != 0 and index >= self.size():
            raise ValueError("your index is out of range")

        if self.first_node == None and index == 0:
            self.first_node = Node(value)

        current_node = self.first_node
        count = 0
        while current_node:
            if count == index:
                current_node.value = value
            count += 1
            current_node = current_node.next_node

    def get_value(self, index):

        if index != 0 and index >= self.size():
            raise ValueError("your index is out of range")

        current_node = self.first_node
        count = 0
        while current_node:
            if count == index:
                print("node value is: ", current_node.value)
                return current_node.value
            count += 1
            current_node = current_node.next_node


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
