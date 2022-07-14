class Car:
    wheels = 5
    def __init__(self):
        self.mil = 10
        self.com = "Audi"


c1 = Car()
c2 = Car()
c1.mil = 15
Car.wheels = 5
print(c1.com,c1.mil,c1.wheels)
print(c2.com,c2.mil)