result = []
for x in range(5):
    if x%3 == 0:
        continue
    result.append(x)
    print(x)
else:
    result.append(10)

print(result)
