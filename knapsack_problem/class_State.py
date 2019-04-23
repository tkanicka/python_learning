prices = [5, 10, 25]
weights = [5, 75, 15]

class State:

    def __init__(self, level, value, weight, taken):

        self.value = value
        self.weight = weight
        self.taken = taken
        self.level = level

    def get_nextState(self):
        if self.level < len(prices):
            if self.taken[self.level]== 0:
                add_taken = list(self.taken)
                add_taken[self.level] = 1
                first_option = State(self.level + 1, self.value + prices[self.level],
                                     self.weight + weights[self.level],
                                     add_taken)
                return first_option
            else:
                second_option = State(self.level + 1, self.value,
                                      self.weight, self.taken)

                return second_option
        else:
            return None


actual_state = State(0, 0, 0, [0]*len(prices))
while actual_state.get_nextState() != None :
    actual_state = actual_state.get_nextState()
    print(actual_state.taken)



