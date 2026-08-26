def is_palindrome(s):
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    print(is_palindrome("Was it a car or a cat I saw?"))  # True
    print(is_palindrome("Hello"))                          # False
