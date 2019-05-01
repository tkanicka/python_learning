
class StateGenerator:

    def __init__(self, index, taken, value, weight, prices, weights ):

        self.value = value
        self.weight = weight
        self.taken = taken
        self.index = index
        self.prices = prices
        self.weights = weights

    def get_NextState(self):
        if self.index < len(self.prices) and self.taken[self.index] != 1:
            new_taken = list(self.taken)
            new_taken[self.index] = 1

            new_state = StateGenerator(self.index +1, new_taken, self.value + self.prices[self.index],
                                       self.weight + self.weights[self.index], self.prices, self.weights)
            print(new_state.taken)
            return new_state

        elif self.index < len(self.prices) and self.taken[self.index] == 1:
            new_state = StateGenerator(self.index + 1, self.taken, self.value,      # if current item is taken, just increase your index
                                       self.weight, self.prices, self.weights)      # and try to generate next state
            return new_state.get_NextState()

        else:
            return None

    def get_allNextStates(self):

        while self.index < len(self.prices):        # goes over all possible states that can be generated from your current state
            self.get_NextState()
            self.index += 1

    def get_AllPotentialStates(self):    # goes through all possible combinations from your items that can be made further from your current state
                                         # develops the branch you are in. It is done in DFS order
            while self.index < len(self.prices):
                self.get_NextState().get_AllPotentialStates()
                self.index += 1


if __name__ == "__main__":
    prices = [5, 10, 25]
    weights = [1, 2, 3]

    empty_state = StateGenerator(0, [0] * len(prices), 0, 0, prices, weights)
    end_state = StateGenerator(2, [0, 0, 1], 25, 3, prices, weights)

    empty_state.get_AllPotentialStates()

    print("\n")
    empty_state.index = 0
    empty_state.get_NextState().get_allNextStates()

    print("\n")
    empty_state.index = 1
    empty_state.get_allNextStates()

    print("\n")
    empty_state.index = 1
    empty_state.get_AllPotentialStates()

    print("\n")
    empty_state.index = 0
    empty_state.get_allNextStates()

