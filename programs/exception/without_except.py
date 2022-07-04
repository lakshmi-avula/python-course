result = []
fruit = "orange"
try:
     result.append('f:enter')
except AttributeError as ae:
     fruit.missingmethod()
     result.append('f:return')



print(result)
# try:
#     result.append("m:beforecall")
#     # function_without_except(result)
#     result.append("m:aftercall")
# except AttributeError as ae:
#     result.append("m:except")
#
# print(result)