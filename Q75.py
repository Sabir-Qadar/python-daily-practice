from collections import Counter
import re


def word_frequency(text):
    words = re.findall(r"[a-zA-Z']+", text.lower())
    return dict(Counter(words))


if __name__ == "__main__":
    print(word_frequency("The cat sat on the mat. The cat was happy."))
