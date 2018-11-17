import copy

class Vehicle:

    def __init__(self, name = "undefined"):
        self.name = name
        self.speed = 0
        self.distance = 0
        self.consumption = 0

    def acceleration(self,x):
            self.speed += x

    def deceleration(self,y):
        if self.speed - y < 0:
            print("you can't go backwards, you stand")
            self.speed = 0
        else:
            self.speed -= y

    def vehicleProperities(self):
        print(self.name)
        print("speed = ",self.speed)
        print("distance = ",self.distance)
        print("consumption = ", self.distance)
        print("\n")

    def theoreticalDistance(self):
        vehicleDeputy = copy.deepcopy(self)
        vehicleDeputy.name = "Deputy"
        theoreticalDistance = vehicleDeputy.speed * 3600                # i expect that speed is in m*s^-1
        print("your theoretical distance in one hour is:", theoreticalDistance, "m")
        del vehicleDeputy

    def __del__(self):
        print("destructor used, vehicle" ,self.name, "deleted")

class Car(Vehicle):

    def acceleration(self,x):
        if self.speed + x > 55:
            print("too fast!!\n yor max speed is 55 ms^-1 ")
            self.speed = 55
        else:
            self.speed += x

car1 = Car("test car")
car1.vehicleProperities()
car1.acceleration(20)
car1.vehicleProperities()
car1.theoreticalDistance()

class Plane(Vehicle):

    def acceleration(self, x):

        if self.speed + x > 350:
            print("too fast!!\n yor max speed is 350 ms^-1 ")
            self.speed = 350
        else:
            self.speed += x

plane1 = Plane("plane1")
plane1.acceleration(349)
plane1.vehicleProperities()
plane1.deceleration(100)
plane1.theoreticalDistance()
plane1.vehicleProperities()