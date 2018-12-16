import random


class Play:

    def __init__(self, name="Player"):
        self.name = name

    def print_name(self):

        print("your name is ", self.name)

    def TossDie(self, x=1):

        for i in range(x):
            print(random.randint(1, 6))

    def RPC(self, x=1):

        for i in range(x):
            options = ["rock", "paper", "scissors"]
            print(random.choice(options))


player1 = Play("Andula")
player1.print_name()
player1.RPC(3)
player1.TossDie(2)



