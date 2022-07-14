class Student:
    school = "Telusko"   #class method
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):           #instance method
        return self.m1 + self.m2 + self.m3/3
    @classmethod
    def get_School(cls):
        return cls.school
    @staticmethod
    def info():
        return "this is student class"


s1 = Student(32,29,12)
s2 = Student(25,35,20)
print(Student.info())
print(s2.avg())
print(s1.avg())
Student.info()