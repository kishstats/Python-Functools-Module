from functools import partial


def multiply(x, y):
    print(f"{x=}")
    print(f"{y=}")
    return x * y


double_it = partial(multiply, 2)

print(double_it)  # functools.partial(<function multiply at 0x10619cfe0>, 2)

print(double_it(5))  # 10
