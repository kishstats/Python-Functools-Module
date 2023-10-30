from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("before executing function")
        func(*args, **kwargs)
        print("after executing function")

    return wrapper


@my_decorator
def say_hello(name):
    """Say Hello

    Parameters:
    name (string)
    """
    print(f"hello, {name}")


# prints:
# before executing function
# hello, Joe Blow
# after executing function
say_hello("Joe Blow")

print(say_hello.__name__)  # say_hello

# prints:
# Say Hello

#     Parameters:
#     name (string)
print(say_hello.__doc__)
