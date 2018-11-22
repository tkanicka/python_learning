import copy
class car:
    def __init__(self,speed=0,distance=0,consumption=0):
        if speed not in range(0,201):
            print("too fast!!\n yor max speed is 200 ")
            speed = 200

        self.speed = speed
        self.distance = distance
        self.consumption = consumption

    def acceleration(self,x):
        if self.speed + x > 200:
            print("too fast!!\n yor max speed is 200 ")
            self.speed = 200
        else:
            self.speed += x

    def retardation(self,y):
        if self.speed - y < 0:
            print("you can't go backwards, you stand")
            self.speed = 0
        else:
            self.speed -= y

    def __del__(self):
        print("destructor used, car" ,self, "deleted")

    def carProperities(self):
        print(self)
        print("speed = ",self.speed)
        print("distance = ",self.distance)
        print("consumption = ", self.distance)
        print("\n")