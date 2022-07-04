result = []
x=1
while x in range(5):
    result.append(x)
    x = x+1
    if x%4==0:
        break
else:
    result.append(10)
    

print(result)
