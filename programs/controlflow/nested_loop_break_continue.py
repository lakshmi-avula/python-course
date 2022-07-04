result = []
for x in range(3):
    for y in range(1,5):
        if y%3 == 0:
            continue
        if x%2 == 1:
            break
        result.append(x)

print(result)