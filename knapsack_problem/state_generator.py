def sort_items(prices, weights):  # sorting items according to the price/weight ratio
    items = []
    ratio = []

    for x in range(len(prices)):
        y = prices[x] / weights[x]
        ratio.append((y, x))
    ratio.sort(reverse=True)

    for x in range(len(ratio)):
        y = ratio[x][1]
        items.append([prices[y], weights[y]])

    return items

class StateGenerator:

    def __init__(self, index, taken, prices, weights):

        if len(prices) == len(weights):         # checking the entries
            self.items = sort_items(prices, weights)

            self.prices = prices
            self.weights = weights

            if index <= len(self.prices):
                self.index = index

            else:
                raise ValueError("your index is out of range")

            if len(taken) == len(self.prices):
                self.taken = taken

            else:
                raise ValueError("your list of taken items must have the same length as your list of items")

            self.value = 0
            self.weight = 0
            for i in range(len(self.prices)):        # calculating value and weight according to your taken items
                if self.taken[i] == 1:
                    self.value += self.items[i][0]
                    self.weight += self.items[i][1]

        else:
            raise ValueError("lists of values and prices must have the same length")

    def get_NextState(self):

        if self.index < len(self.prices) and self.taken[self.index] != 1:
            new_taken = list(self.taken)
            new_taken[self.index] = 1

            new_state = StateGenerator(self.index + 1, new_taken,
                                       self.prices, self.weights)

            return new_state

        elif self.index < len(self.prices) and self.taken[self.index] == 1:
            new_state = StateGenerator(self.index + 1, self.taken,       # if current item is taken, just increase your index
                                       self.prices, self.weights)      # and try to generate next state
            return new_state.get_NextState()

        else:
            return None


    def travers_allNextStates(self, print_taken = False):
        i = self.index
        while self.get_NextState():        # goes over all possible states that can be generated from your current state
           if print_taken:
               print(self.get_NextState().taken)
           else:
               self.get_NextState()

           self.index += 1

        self.index = i

    def travers_AllPotentialStates(self, print_taken = False):    # goes through all possible combinations from your items that can be made further from your current state
        i = self.index                                       # develops the branch you are in. It is done in DFS order
        while self.index < len(self.prices):
            next_state = self.get_NextState()
            if print_taken:
                print(next_state.taken)
            next_state.travers_AllPotentialStates(print_taken)
            self.index += 1
        self.index = i

    def print_takenItems(self):
        print("prices:", "weights:")
        for x in range(len(self.taken)):
            if self.taken[x] == 1:
                print(self.items[x][0], "    ", self.items[x][1])
        print("value:", self.value, "   weight:", self.weight)


