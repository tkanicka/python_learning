import unittest
from object_chain import Chain
from object_chain import Node


class TestChainClass(unittest.TestCase):

    def setUp(self):
        self.node1 = Node(1)
        self.node2 = Node(2)
        self.node3 = Node(3)

        self.node1.next_node = self.node2
        self.node2.next_node = self.node3                           # setup for basic chain

        self.node2.previous_node = self.node1
        self.node3.previous_node = self.node2

        self.test_chain = Chain()
        self.test_chain.first_node = self.node1
        self.test_chain.last_node = self.node3

        self.chain1 = Chain()       # setup for testing empty chain

    def test_pushEnd(self):
        self.test_chain.pushEnd(4)
        self.assertEqual(4, self.test_chain.last_node.value)
        self.assertEqual(self.node3, self.test_chain.last_node.previous_node)

        self.chain1.pushEnd(1)
        self.assertEqual(1, self.chain1.last_node.value)
        self.assertEqual(self.chain1.first_node, self.chain1.last_node)

    def test_popEnd(self):
        self.test_chain.popEnd()
        self.assertEqual(2, self.test_chain.last_node.value)

        self.chain1.first_node = Node(3)
        self.chain1.last_node = self.chain1.first_node
        self.chain1.popEnd()
        self.assertEqual(None, self.chain1.first_node)

    def test_push_start_node(self):
        self.test_chain.pushFront(4)
        self.assertEqual(4, self.test_chain.first_node.value)
        self.assertEqual(self.node1, self.test_chain.first_node.next_node)

        self.chain1.pushFront(1)
        self.assertEqual(1, self.chain1.first_node.value)

    def test_pop_start_node(self):

        self.test_chain.popFront()
        self.assertEqual(self.node2, self.test_chain.first_node)
        self.assertEqual(self.node3, self.test_chain.first_node.next_node)

        self.chain1.first_node = Node(0)
        self.chain1.last_node = self.chain1.first_node
        self.chain1.popFront()
        self.assertEqual(None, self.chain1.first_node)

    def test_chain_size(self):
        self.assertEqual(3, self.test_chain.size())
        self.test_chain.pushFront(10)
        self.assertEqual(4, self.test_chain.size())

        self.assertEqual(0, self.chain1.size())

        self.chain1.first_node = Node(1)
        self.assertEqual(1, self.chain1.size())

    def test_chain_change_insert(self):
        self.test_chain.insert(1, 44)
        self.assertEqual(44, self.test_chain.first_node.next_node.value)
        self.assertEqual(44, self.node2.previous_node.value)
        self.test_chain.insert(3, 10)
        self.assertEqual(self.node3, self.test_chain.last_node.previous_node)

        self.chain1.insert(0, 25)
        self.assertEqual(25, self.chain1.first_node.value)

    def test_chain_change_erase(self):
        self.test_chain.erase(1)
        self.assertEqual(self.test_chain.first_node, self.node3.previous_node)
        self.assertEqual(3, self.test_chain.first_node.next_node.value)

        self.test_chain.erase(1)
        self.assertEqual(1, self.test_chain.last_node.value)

        self.chain1.last_node = Node(11)
        self.chain1.first_node = self.chain1.last_node
        self.chain1.erase(0)
        self.assertEqual(None, self.chain1.first_node)

    def test_chain_change_set(self):
        self.test_chain.set_value(2, 5)
        self.assertEqual(5, self.node3.value)

        self.chain1.set_value(0, 1)
        self.assertEqual(1, self.chain1.first_node.value)

    def test_chain_change_get(self):
        self.assertEqual(1, self.test_chain.get_value(0))

        self.assertEqual(None, self.chain1.get_value(0))

        self.chain1.set_value(0, 25)
        self.assertEqual(25, self.chain1.get_value(0))


    def test_input_set(self):
        self.assertRaises(ValueError, self.test_chain.set_value, 3)
        self.assertRaises(ValueError, self.test_chain.set_value, 4)

        self.assertRaises(ValueError, self.chain1.set_value, 1)
        self.assertRaises(ValueError, self.chain1.set_value, 2)

    def test_input_get(self):
        self.assertRaises(ValueError, self.test_chain.get_value, 3)
        self.assertRaises(ValueError, self.test_chain.get_value, 8)

        self.assertRaises(ValueError, self.chain1.get_value, 1)
        self.assertRaises(ValueError, self.chain1.get_value, 4)


    def test_to_pythonList(self):
        self.assertEqual([1, 2, 3], self.test_chain.to_pythonList())
        self.assertEqual([], self.chain1.to_pythonList())

    def test_swap_nodes(self):
        self.test_chain.swap_nodes(2, 0)

        self.assertEqual(3, self.test_chain.first_node.value)
        self.assertEqual(1, self.test_chain.last_node.value)

        self.assertRaises(ValueError, self.chain1.swap_nodes, 2)

    def test_sort(self):
        self.test_chain.pushFront(5)
        self.test_chain.pushEnd(7)
        self.test_chain.insert(1, 4)
        self.test_chain.sort()

        self.assertEqual([1, 2, 3, 4, 5, 7], self.test_chain.to_pythonList())

    def test_check_ifSorted(self):
        self.assertEqual(True, self.test_chain.check_ifSorted())

if __name__ == "__main__":
    unittest.main()
