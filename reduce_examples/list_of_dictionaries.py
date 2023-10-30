from functools import reduce

order_items = [
    {"item_id": 1, "name": "hiking boots", "amount": 150.00, "qty": 1},
    {"item_id": 33, "name": "hiking poles", "amount": 95.00, "qty": 1},
    {"item_id": 1, "name": "hydration pack", "amount": 52.00, "qty": 1},
    {"item_id": 1, "name": "hiking shorts", "amount": 60.00, "qty": 2},
]

# missing intialial value will cause an error
# total_amount = reduce(lambda x, y: x + y["amount"], order_items)
# print(
#     f"{total_amount=}"
# )  # TypeError: unsupported operand type(s) for +: 'dict' and 'float'

total_amount = reduce(lambda x, y: x + y["amount"], order_items, 0)
print(f"{total_amount=}")
assert total_amount == 357.0
