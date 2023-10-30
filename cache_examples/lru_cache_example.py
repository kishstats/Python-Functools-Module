from functools import lru_cache


@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    res = fibonacci(40)
    print(res)  # 102334155
    print(
        fibonacci.cache_info()
    )  # CacheInfo(hits=38, misses=41, maxsize=128, currsize=41)
    fibonacci.cache_clear()  # clears cache
