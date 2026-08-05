"""
Problem 38: Roman to Integer
Difficulty: Moderate

Convert a Roman numeral string to an integer.
"""

def roman_to_int(s):
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    total = 0
    for i, ch in enumerate(s):
        value = values[ch]
        if i + 1 < len(s) and value < values[s[i + 1]]:
            total -= value
        else:
            total += value
    return total


if __name__ == "__main__":
    print(roman_to_int("MCMXCIV"))  # 1994
    print(roman_to_int("LVIII"))    # 58
