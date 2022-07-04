def function_with_except(result):
    result = []
    fruit = "orange"
    result.append("f:enter")
    try:
        fruit.missingmethod()
    except AttributeError as ae:
        result.append("f:except")

    result.append("f:return")



# def function_call_with_except():
#     result = []
#     try:
#         result.append("m:beforecall")
#         function_with_except(result)
#         result.append("m:aftercall")
#     except AttributeError as ae:
#         result.append("m:except")
