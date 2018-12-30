
class Node:
    def __init__(self, node=0):
        self.node = node
        self.next_node = None
        self.previous_node = None


class Chain:
    def __init__(self):
        self.first_node = None
        self.last_node = None

    def PrintChain(self):
        print_node = self.first_node

        while print_node:

            print(print_node.node)
            print_node = print_node.next_node

    def PrintChain_backwards(self):
        print_node = self.last_node

        while print_node:

            print(print_node.node)
            print_node = print_node.previous_node


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
