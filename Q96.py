def fib(n, memo=None):
    if memo is None:
        memo = {}
    if n in (0, 1):
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    print([fib(i) for i in range(10)])  # [0,1,1,2,3,5,8,13,21,34]
