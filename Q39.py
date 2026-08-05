"""
Problem 39: Anagram Check
Difficulty: Basic

Check whether two strings are anagrams of each other.
"""

from collections import Counter


def is_anagram(a, b):
    a, b = a.replace(" ", "").lower(), b.replace(" ", "").lower()
    return Counter(a) == Counter(b)


if __name__ == "__main__":
    print(is_anagram("listen", "silent"))   # True
    print(is_anagram("hello", "world"))     # False
