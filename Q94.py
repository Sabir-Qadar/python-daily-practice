def decimal_to_binary(n):
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(str(n % 2))
        n //= 2
    return "".join(reversed(digits))


def binary_to_decimal(b):
    value = 0
    for ch in b:
        value = value * 2 + int(ch)
    return value


if __name__ == "__main__":
    print(decimal_to_binary(42))         # "101010"
    print(binary_to_decimal("101010"))   # 42
