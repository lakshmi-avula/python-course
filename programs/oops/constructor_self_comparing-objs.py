# class Computer:        #create constructor
#     pass
# c1 = Computer()
# c2 = Computer()
# print(id(c1))
# print(id(c2))

#self
class Computer:
    def __init__(self):
        self.name = "Rocky"
        self.age = 29

c1 = Computer()
c2 = Computer()
c1.name = "Rishi"
print(c1.name)
print(c2.name)
print(c2.age)
