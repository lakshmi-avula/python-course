from placeholders import *
def outer_func(outer_var):
    def inner_func(inner_var):
        return outer_var + inner_var
    return inner_func

f1 = outer_func(10)
# print(type(f1).__name__)
# print(f1(20))
print(len(dir(f1)))