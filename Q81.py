def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


if __name__ == "__main__":
    print(gcd(24, 36))  # 12
    print(lcm(4, 6))    # 12
