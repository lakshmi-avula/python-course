# class A(object):
#     def f(self):
#         return "A:f()"
#
# class B(A):
#     def g(self):
#         return "B:g()"
#
#
# b = B()
# print(b.g())
# print(b.f())
#
# a = A()
# print(a.f())
# try:
#     print(a.g())
# except AttributeError as ex:
#     print(ex) # uncomment this line after filling up
#     pass
#
#
class A(object):
    def __init__(self):
        self.a1 = []

    def append(self, obj):
        self.a1.append(obj)

class B(A):
    def __init__(self):
        self.b1 = []


a = A()
print(getattr(a,"b1",None))
b = B()
print(getattr(a,"b1",None))


class B(A):
    def __init__(self):
        A.__init__(self)
        self.b1 = "b1"

b = B()
print(getattr(b,"b1",None))
b.append("orange")
print(b.a1)

