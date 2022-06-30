def Merge(dict1,dict2):
        return(dict2.update(dict1))

dict1 = {'a':2  ,'b':6}
dict2 = {'c':4,'d':10}

print(Merge(dict1,dict2))
print(dict2)