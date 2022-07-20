def demo_generator_to_list(generator):
    return list(generator)


# def func():
#     yield 1
#     yield 2
#     return
#     yield 3
#
# print(demo_generator_to_list(func()))


def func():
    for x in range(5):
        yield x
    yield 10


print(demo_generator_to_list(func()))