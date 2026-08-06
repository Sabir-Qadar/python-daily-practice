"""
Problem 43: Run-Length Encoding
Difficulty: Moderate

Encode and decode a string using run-length encoding, e.g. 'aaabb' <-> [('a',3), ('b',2)].
"""

def rle_encode(s):
    if not s:
        return []
    encoded = []
    count = 1
    for i in range(1, len(s) + 1):
        if i < len(s) and s[i] == s[i - 1]:
            count += 1
        else:
            encoded.append((s[i - 1], count))
            count = 1
    return encoded


def rle_decode(pairs):
    return "".join(ch * count for ch, count in pairs)


if __name__ == "__main__":
    enc = rle_encode("aaabbbcca")
    print(enc)              # [('a',3), ('b',3), ('c',2), ('a',1)]
    print(rle_decode(enc))  # "aaabbbcca"
