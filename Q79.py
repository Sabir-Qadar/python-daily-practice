def digital_root(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n


if __name__ == "__main__":
    print(digital_root(942))  # 6  (9+4+2=15 -> 1+5=6)
