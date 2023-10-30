from functools import singledispatchmethod


class Math:
    def __init__(self, value) -> None:
        self.value = value

    @singledispatchmethod
    def add(self, item):
        return self.value + item

    @add.register(str)
    def _(self, item):
        return f"{self.value}, {item}"

    @add.register(list)
    def _(self, item):
        return [self.value] + item


math = Math(7)
print(math.add(3))  # 10
print(math.add("lucky"))  # 7, lucky
print(math.add([9, 11]))  # [7, 9, 11]
