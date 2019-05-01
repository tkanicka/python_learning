import unittest
from state_generator import StateGenerator


class TestStateGenerator(unittest.TestCase):
    def setUp(self):
        prices = [5, 10, 25]
        weights = [1, 2, 3]

        self.empty_state = StateGenerator(0, [0] * len(prices), 0, 0, prices, weights)
        self.end_state = StateGenerator(2, [0, 0, 1], 25, 3, prices, weights)
        self.state1 = StateGenerator(1, [0, 1, 0], 10, 2, prices, weights)

    def test_get_NextState(self):

        self.assertEqual([1, 0, 0], self.empty_state.get_NextState().taken)
        self.assertEqual(1, self.empty_state.get_NextState().index)
        self.assertEqual([0, 1, 1], self.state1.get_NextState().taken)


    def test_get_NextState_None(self):
        self.assertEqual(None, self.empty_state.get_NextState().get_NextState().get_NextState().get_NextState())
        self.assertEqual(None, self.state1.get_NextState().get_NextState())
        self.assertEqual(None, self.end_state.get_NextState())

if __name__ == "__main__":
    unittest.main()