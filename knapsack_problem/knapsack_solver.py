from state_generator import StateGenerator
from state_generator import sort_items

class KnapsackProblem:

    def __init__(self, capacity, prices, weights):
        self.capacity = int(capacity)
        self.prices = prices
        self.weights = weights

        self.items = sort_items(self.prices,self.weights)

    def upper_bound(self, index, ac_value, ac_weight):  # computing the highest possible value we can get from developing our state
        up_value = ac_value     # starting values for computing the upper bound are our actual value and weight and current index
        up_weight = ac_weight
        for x in range(index, len(self.items)):
            if up_weight + self.items[index][1] <= self.capacity:
                up_weight += self.items[index][1]
                up_value += self.items[index][0]

        return up_value


    def solver_optimized(self):

        if self.capacity >= sum(self.weights):

            return(StateGenerator(0, [1]*len(self.items), self.prices, self.weights))

        max_index = len(self.prices)  # the len of items is constant, I don't want to calculate it in every loop

        root_state = StateGenerator(0, [0] * len(self.prices), self.prices, self.weights)
        best_state = root_state

        stack = [root_state]
        counter = 0        # keeping track of the number of states I had to traversed, I have it here just to se if the
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

                # anyway, try the state, where you don't take in the item and its upper bound

                if self.upper_bound(index + 1, next_nonTaken.value, next_nonTaken.weight) > best_state.value:
                    stack.append(next_nonTaken)

                counter += 1

        print(counter)
        return best_state



    def solver_DFS(self):

        if self.capacity >= sum(weights):

            return (StateGenerator(0, [1]*len(self.prices), self.prices, self.weights))

        max_index = len(self.prices)  # the len of items is constant, I don't want to calculate it in every loop

        root_state = StateGenerator(0, [0] * len(self.prices), self.prices, self.weights)
        best_state = root_state
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

    def solver_BFS(self):   # the only difference is that I always take the first item and remove it of the queue

        if self.capacity >= sum(weights):

            return (StateGenerator(0, [1]*len(self.prices), self.prices, self.weights))

        max_index = len(self.prices)  # the len of items is constant, I don't want to calculate it in every loop
        root_state = StateGenerator(0, [0] * len(self.prices), self.prices, self.weights)
        best_state = root_state
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
    print(knapsack3.solver_optimized().print_takenItems())


