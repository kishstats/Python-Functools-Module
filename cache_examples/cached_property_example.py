from functools import cached_property


class Customer:
    def __init__(self, orders) -> None:
        self._orders = orders

    @cached_property
    def recent_orders(self):
        orders = sorted(self._orders, key=lambda x: x["order_id"], reverse=True)
        return orders[:3]


if __name__ == "__main__":
    orders = [
        {"order_id": 1, "name": "hiking boots", "amount": 150.00, "qty": 1},
        {"order_id": 2, "name": "hiking poles", "amount": 95.00, "qty": 1},
        {"order_id": 3, "name": "hydration pack", "amount": 52.00, "qty": 1},
        {"order_id": 4, "name": "hiking shorts", "amount": 60.00, "qty": 2},
        {"order_id": 5, "name": "hiking shorts", "amount": 60.00, "qty": 2},
        {"order_id": 6, "name": "hiking shorts", "amount": 60.00, "qty": 2},
        {"order_id": 7, "name": "hiking shorts", "amount": 60.00, "qty": 2},
    ]
    customer = Customer(orders)
    print(customer.recent_orders)
    print(customer.recent_orders)  # from cache
