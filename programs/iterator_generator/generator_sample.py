def gen_sample():
    yield 1
    yield 2
    yield 3


def gen_without_yield():
    print(1)
    print(2)
    print(3)

# print('1st time')
# gen_without_yield()
# print(gen_sample())
# print('2nd time')
# gen_without_yield()
# gen_sample()
# print('3rd time')
# gen_without_yield()
# gen_sample()
# print('4th time')
# gen_without_yield()
# gen_sample()

for item in gen_sample():

    print(item)

print(list(gen_sample()))

