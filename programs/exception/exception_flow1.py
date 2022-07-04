fruit = "orange"
result = []
try:
    result.append("one")
    value = 1/0
    result.append("two")
    fruit.missingmethod()
    result.append("three")
except AssertionError as ae:
    result.append("four")
except ZeroDivisionError as ze:
    result.append("five")


print(result)