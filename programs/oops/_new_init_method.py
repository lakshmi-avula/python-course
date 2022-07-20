class A(object):
    __dict = dict()
    def __new__(cls):
        if 'key' in A.__dict:
            print("EXITS")
            return A.__dict['key']
        else:
            print("NEW")
            return super(A,cls).__new__(cls)

    def __init__(self):
        print("from INIT")
        A.__dict['key'] = self
        print("")


a1 = A()

a2 = A()

a3 = A()
