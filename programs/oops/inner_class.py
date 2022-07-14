class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop
    def show(self):
        print(self.name,self.rollno)
        self.lap.Laptop()
    class Laptop:
        def __init__(self,brand,cpu,ram):
            self.brand = brand
            self.cpu = cpu
            self.ram = ram
        def show(self):
            print(self.brand,self.cpu,self.ram)





s1 = Student("Rocky",23)
s2 = Student("Rishi",22)
s1.show()
s2.show()

