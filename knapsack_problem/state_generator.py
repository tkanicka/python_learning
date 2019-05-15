
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

    def get_NextState(self):

        if self.index < len(self.prices) and self.taken[self.index] != 1:
            new_taken = list(self.taken)
            new_taken[self.index] = 1

            new_state = StateGenerator(self.index +1, new_taken,
                                       self.prices, self.weights)

            return new_state

        elif self.index < len(self.prices) and self.taken[self.index] == 1:
            new_state = StateGenerator(self.index + 1, self.taken,       # if current item is taken, just increase your index
                                       self.prices, self.weights)      # and try to generate next state
            return new_state.get_NextState()

        else:
            return None


    def get_allNextStates(self,print_taken = False):
        i = self.index
        while self.get_NextState():        # goes over all possible states that can be generated from your current state
           if print_taken:
               print(self.get_NextState().taken)
           else:
               self.get_NextState()

           self.index += 1

        self.index = i

    def get_AllPotentialStates(self, print_taken = False):    # goes through all possible combinations from your items that can be made further from your current state
        i = self.index                                       # develops the branch you are in. It is done in DFS order
        while self.index < len(self.prices):
            next_state = self.get_NextState()
            if print_taken:
                print(next_state.taken)
            next_state.get_AllPotentialStates(print_taken)
            self.index += 1
        self.index = i



class KnapsackProblem:

    def __init__(self, capacity, prices, weights):
        self.capacity = capacity
        self.prices = prices
        self.weights = weights

    def solver(self):
        best_state = StateGenerator(0, [0] * len(self.prices), self.prices, self.weights)
        root_state = StateGenerator(0, [0] * len(self.prices), self.prices, self.weights)
        stack = [root_state]
        max_index = len(root_state.prices)

        while len(stack) > 0:
            current_state = stack.pop()
            index = current_state.index

            if current_state.value >= best_state.value:
                best_state = current_state

            if index < max_index:
                if current_state.weight + self.weights[index] <= self.capacity:
                    next_taken = current_state.get_NextState()
                    if next_taken.value > best_state.value:
                        best_state = next_taken

                    stack.append(next_taken)

                next_nonTaken = StateGenerator(index+1,current_state.taken,prices,weights)
                stack.append(next_nonTaken)

        return best_state

if __name__ == "__main__":
    prices = [5, 10, 25, 13, 42, 12, 10, 17, 25, 35]
    weights = [5, 75, 15, 10, 20, 25, 20, 15, 10, 5]


    knapsack = KnapsackProblem(15,prices,weights)
    print(knapsack.solver().value)