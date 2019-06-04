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


class KnapsackProblem:

    def __init__(self, capacity, prices, weights):
        self.capacity = int(capacity)
        self.prices = prices
        self.weights = weights

        self.items = sort_items(self.prices,self.weights)

    def upper_bound(self,index, ac_value, ac_weight):  # computing the highest possible value we can get from developing our state
        up_value = ac_value     # starting values for computing the upper bound are our actual value and weight and current index
        up_weight = ac_weight
        for x in range(index, len(self.items)):
            if up_weight + self.items[index][1] <= self.capacity:
                up_weight += self.items[index][1]
                up_value += self.items[index][0]

        return up_value


    def solver_optimized(self):

        if self.capacity >= sum(self.weights):

            return(StateGenerator(0, [1]*len(self.prices), self.prices, self.weights))

        max_index = len(self.prices)  # the len of items is constant, I don't want to calculate it in every loop

        root_state = StateGenerator(0, [0] * len(self.prices), self.prices, self.weights)
        best_state = StateGenerator(0, [0] * len(self.prices), self.prices, self.weights)

        stack = [root_state]
        counter = 0         # keeping track of the number of states I had to traversed, I have it here just to se if the
                            # optimalization has en effect on solving the problem
        while len(stack) > 0:
            current_state = stack.pop()
            index = current_state.index
            if current_state.value > best_state.value:
                best_state = current_state

            if index < max_index:
                if current_state.weight + self.items[index][1] <= self.capacity:        # If possible take in the item
                    next_taken = current_state.get_NextState()

                    if self.upper_bound(index + 1, next_taken.value, next_taken.weight) > best_state.value:
                        stack.append(next_taken)  # continue with developing this state only if it has a higher estimation
                                                  # than best_state's value
                    if next_taken.value > best_state.value:
                        best_state = next_taken

                next_nonTaken = StateGenerator(index+1, current_state.taken, self.prices, self.weights)

                if self.upper_bound(index + 1, next_nonTaken.value, next_nonTaken.weight) > best_state.value:
                    stack.append(next_nonTaken)

                counter += 1

        print(counter)
        return best_state



    def solver_DFS(self):

        if self.capacity >= sum(weights):

            return(StateGenerator(0, [1]*len(self.prices), self.prices, self.weights))

        best_state = StateGenerator(0, [0] * len(self.prices), self.prices, self.weights)

        max_index = len(self.prices)  # the len of items is constant, I don't want to calculate it in every loop

        root_state = StateGenerator(0, [0] * len(self.prices), self.prices, self.weights)
        stack = [root_state]
        counter = 0
        while len(stack) > 0:
            current_state = stack.pop()
            index = current_state.index

            if current_state.value > best_state.value:
                best_state = current_state

            if index < max_index:
                if current_state.weight + self.items[index][1] <= self.capacity:        # If possible take in the item
                    next_taken = current_state.get_NextState()

                    stack.append(next_taken)

                next_nonTaken = StateGenerator(index+1, current_state.taken, self.prices, self.weights)
                stack.append(next_nonTaken)     # anyway, try the next state, without taking the item

                counter += 1
        print(counter)
        return best_state

    def solver_BFS(self):   # the only difference that I always take the first item of the queue

        if self.capacity >= sum(weights):

            return(StateGenerator(0, [1]*len(self.prices), self.prices, self.weights))

        best_state = StateGenerator(0, [0] * len(self.prices), self.prices, self.weights)

        max_index = len(self.prices)  # the len of items is constant, I don't want to calculate it in every loop

        root_state = StateGenerator(0, [0] * len(self.prices), self.prices, self.weights)
        queue = [root_state]


        while len(queue) > 0:
            current_state = queue.pop(0)

            if current_state.value > best_state.value:
                best_state = current_state

            index = current_state.index

            if index < max_index:
                if current_state.weight + self.items[index][1] <= self.capacity:        # If possible take in the item
                    next_taken = current_state.get_NextState()

                    queue.append(next_taken)

                next_nonTaken = StateGenerator(index+1, current_state.taken, self.prices, self.weights)
                queue.append(next_nonTaken)     # anyway, try the next state, without taking the item


        return best_state



if __name__ == "__main__":
    prices = [5, 10, 25, 13, 42, 12, 10, 17, 25, 35]
    weights = [5, 75, 15, 10, 20, 25, 20, 15, 10, 5]

    knapsack = KnapsackProblem(60, prices, weights)
    print(knapsack.solver_DFS().print_takenItems())
    knapsack3 = KnapsackProblem(60, prices, weights)
    print(knapsack.solver_optimized().print_takenItems())


