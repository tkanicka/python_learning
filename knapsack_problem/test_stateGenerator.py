import unittest
from state_generator import StateGenerator


class TestStateGenerator(unittest.TestCase):
    def setUp(self):
        prices = [5, 10, 25]
        weights = [1, 2, 3]
        wrong_prices = [1,2]

        self.empty_state = StateGenerator(0, [0] * len(prices), prices, weights)  # empty beginning state
        self.end_state = StateGenerator(2, [0, 0, 1], prices, weights)           # state which can't be developed
        self.state1 = StateGenerator(1, [0, 1, 0], prices, weights)              # common state with already explored index

        self.a = StateGenerator(0, [0] * len(prices), prices, weights)
    def test_get_NextState_true(self):

        self.assertEqual([1, 0, 0], self.empty_state.get_NextState().taken)
        self.assertEqual(1, self.empty_state.get_NextState().index)
        self.assertEqual([0, 1, 1], self.state1.get_NextState().taken)

        self.empty_state.get_NextState()                # checking if our start state became unchanged
        self.assertEqual(0, self.empty_state.index)


    def test_get_NextState_None(self):
        self.assertEqual(None, self.empty_state.get_NextState().get_NextState().get_NextState().get_NextState())
        self.assertEqual(None, self.state1.get_NextState().get_NextState())
        self.assertEqual(None, self.end_state.get_NextState())



if __name__ == "__main__":
    unittest.main()
