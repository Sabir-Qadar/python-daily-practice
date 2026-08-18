def caesar_encrypt(text, shift):
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return "".join(result)


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


if __name__ == "__main__":
    enc = caesar_encrypt("Hello, World!", 3)
    print(enc)                       # "Khoor, Zruog!"
    print(caesar_decrypt(enc, 3))    # "Hello, World!"
