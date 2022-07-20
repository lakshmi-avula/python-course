class Emp:
    def __init__(self):
        self.name = 'XYZ'
        self.salary = 40000

    def show(self):
        print(self.name)
        print(self.salary)


e1 = Emp()
print(vars(e1))