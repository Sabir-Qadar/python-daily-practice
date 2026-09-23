def compress(s):
    if not s:
        return s
    result = []
    count = 1
    for i in range(1, len(s) + 1):
        if i < len(s) and s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            count = 1
    compressed = "".join(result)
    return compressed if len(compressed) < len(s) else s


if __name__ == "__main__":
    print(compress("aabcccccaaa"))  # a2b1c5a3
    print(compress("abcd"))         # abcd (no benefit)
