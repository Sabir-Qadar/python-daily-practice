def count_vowels_consonants(s):
    vowels = set("aeiouAEIOU")
    v = c = 0
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                c += 1
    return v, c


if __name__ == "__main__":
    print(count_vowels_consonants("Hello World"))  # (3, 7)
