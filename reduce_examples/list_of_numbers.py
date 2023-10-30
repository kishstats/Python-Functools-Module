from functools import reduce

lyst = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, lyst)

assert total == 10


# using a named function
def add_it(x, y):
    return x + y


total = reduce(add_it, lyst)
assert total == 10

# TypeError: reduce() of empty iterable with no initial value
# total = reduce(lambda x, y: x + y, [])

total = reduce(lambda x, y: x + y, [], 0)
assert total == 0

max_value = reduce(lambda x, y: x if x > y else y, lyst)
assert max_value == max(lyst)
