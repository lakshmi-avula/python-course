from placeholders import *

def func_invoker(func,*args):
    result = func(*args)
    if result is None:
        return "return something"
    else:
        return result


# lambda_increment = lambda x:x+1
# def nested_func(x):
#     return x+1
#
# print(func_invoker(lambda_increment , 10))
# print(func_invoker(lambda x:x+1,10))
# print(func_invoker(nested_func,10))

value = 10
print(func_invoker(lambda x:x+value,10))
