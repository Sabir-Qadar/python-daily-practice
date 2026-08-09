def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d) ** power for d in digits)


if __name__ == "__main__":
    print(is_armstrong(153))  # True
    print(is_armstrong(123))  # False
