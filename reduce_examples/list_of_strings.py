from functools import reduce

# iterate through a list of characters
lyst = ["a", "b", "c", "d", "e", "f"]

result = reduce(lambda x, y: x + y, lyst)
print(f"{result=}")

assert result == "abcdef"

# iterate through a single string
lyst = "abcdef"

result = reduce(lambda x, y: x + y, lyst)
print(f"{result=}")

assert result == "abcdef"
