def is_perfect(n):
    if n < 2:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n


if __name__ == "__main__":
    print(is_perfect(28))  # True (1+2+4+7+14=28)
    print(is_perfect(12))  # False
