import json
from functools import singledispatch


@singledispatch
def to_json(data):
    return json.dumps(data)


@to_json.register(set)
def _(data):
    return json.dumps(list(data))


item_1 = {"test": True}
print(to_json(item_1))

item_2 = "hello"
print(to_json(item_2))

item_3 = {"one", "two", "three"}
print(to_json(item_3))  # will error if not converted to a list
