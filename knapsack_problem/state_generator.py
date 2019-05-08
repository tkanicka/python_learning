
class StateGenerator:

    def __init__(self, index, taken, prices, weights ):

        if len(prices) == len(weights):         # checking the entries
            self.prices = prices
            self.weights = weights

            if index <= len(prices):
                self.index = index

            else:
                raise ValueError("your index is out of range")

            if len(taken) == len(prices):
                self.taken = taken

            else:
                raise ValueError("your list of taken items must have the same length as your list of items")

                self.value = 0
                self.weight = 0
                for i in range(len(self.taken)):        # calculating value and weight according to your taken items
                    if self.taken[i] == 1:
                        self.value += self.prices[i]
                        self.weight += self.weights[i]

        else:
            raise ValueError("lists of values and prices must have the same length")

    def get_NextState(self, print_taken = False):

        if self.index < len(self.prices) and self.taken[self.index] != 1:
            new_taken = list(self.taken)
            new_taken[self.index] = 1

            new_state = StateGenerator(self.index +1, new_taken,
                                       self.prices, self.weights)
            if print_taken:
                print(new_state.taken)

            return new_state

        elif self.index < len(self.prices) and self.taken[self.index] == 1:
            new_state = StateGenerator(self.index + 1, self.taken,       # if current item is taken, just increase your index
                                       self.prices, self.weights)      # and try to generate next state
            return new_state.get_NextState(print_taken)

        else:
            return None


    def get_allNextStates(self,print_taken = False):
        i = self.index
        while self.get_NextState():        # goes over all possible states that can be generated from your current state
           self.get_NextState(print_taken)
           self.index += 1

        self.index = i

    def get_AllPotentialStates(self, print_taken = False):    # goes through all possible combinations from your items that can be made further from your current state
        i = self.index                                       # develops the branch you are in. It is done in DFS order
        while self.index < len(self.prices):

            self.get_NextState(print_taken).get_AllPotentialStates(print_taken)
            self.index += 1
        self.index = i


if __name__ == "__main__":

    prices = [5, 10, 25]
    weights = [1, 2, 3]

    empty_state = StateGenerator(0, [0] * len(prices), prices, weights)
    end_state = StateGenerator(2, [0, 0, 1], prices, weights)

    print(end_state.value, end_state.weight)

    empty_state.get_AllPotentialStates(True)

    print("\n")

    print(empty_state.get_NextState().value)

    empty_state.get_NextState().get_allNextStates(True)

    print("\n")

    empty_state.get_allNextStates(True)

    print("\n")
    empty_state.index = 1
    empty_state.get_AllPotentialStates()

    print("\n")
    empty_state.index = 0
    empty_state.get_NextState()


