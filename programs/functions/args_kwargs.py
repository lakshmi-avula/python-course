"""
def func(*args, **kwargs):
    for each in args: #list
        print(each)

    for key, value in kwargs.values()

    a = {b:1, c:2}

"""
# def myFun(*args):
#     for arg in args:
#         print(arg)
#
# myFun('hello','welcome','to','world')



# def myFun(arg1,*argv):
#     print("first argument:",arg1)
#     for arg in argv:
#         print("next argument *argv:",arg)
#
#
# myFun('hello','welcome','to','world')

#
# def myFun(arg1,**kwargs):
#     for key,value in kwargs.items():
#         print("%s == %s"%(key,value))
#
#
# myFun("hello",first='geeks',mid = 'for',last='geeks')
#
# def myFun(arg1,arg2,arg3):
#     print("arg1:",arg1)
#     print("arg2:",arg2)
#     print("arg3:",arg3)
#
# args=("geeks","for","geeks")
# myFun(*args)
#
# kwargs = {"arg1": "geeks" , "arg2" :"for","arg3":"geeks"}
# myFun(**kwargs)

def myFun(*args,**kwargs):
    print("*args:",args)
    print("**kwargs:",kwargs)

myFun('geeks','for','geeks',first = "geeks",mid = "for",last = "geeks")

