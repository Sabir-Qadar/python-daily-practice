"""
problems_bank.py

A bank of basic-to-moderate Python coding problems, each with a title,
difficulty, short description, and a working solution (with a small
demo/test at the bottom so the file is runnable on its own).

Add more entries any time — just give each one a unique "id".
"""

PROBLEMS = [
    {
        "id": "two_sum",
        "title": "Two Sum",
        "difficulty": "Basic",
        "description": (
            "Given a list of integers and a target, return the indices of the\n"
            "two numbers that add up to the target. Assume exactly one solution."
        ),
        "code": '''
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
    return None


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    print(two_sum([3, 2, 4], 6))        # [1, 2]
''',
    },
    {
        "id": "palindrome_check",
        "title": "Palindrome Check",
        "difficulty": "Basic",
        "description": "Check whether a given string is a palindrome, ignoring case and spaces.",
        "code": '''
def is_palindrome(s):
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    print(is_palindrome("Was it a car or a cat I saw?"))  # True
    print(is_palindrome("Hello"))                          # False
''',
    },
    {
        "id": "fizzbuzz",
        "title": "FizzBuzz",
        "difficulty": "Basic",
        "description": "Print numbers 1 to n. Multiples of 3 -> 'Fizz', of 5 -> 'Buzz', of both -> 'FizzBuzz'.",
        "code": '''
def fizzbuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


if __name__ == "__main__":
    print(fizzbuzz(20))
''',
    },
    {
        "id": "anagram_check",
        "title": "Anagram Check",
        "difficulty": "Basic",
        "description": "Check whether two strings are anagrams of each other.",
        "code": '''
from collections import Counter


def is_anagram(a, b):
    a, b = a.replace(" ", "").lower(), b.replace(" ", "").lower()
    return Counter(a) == Counter(b)


if __name__ == "__main__":
    print(is_anagram("listen", "silent"))   # True
    print(is_anagram("hello", "world"))     # False
''',
    },
    {
        "id": "matrix_transpose",
        "title": "Matrix Transpose",
        "difficulty": "Basic",
        "description": "Transpose a 2D matrix (rows become columns).",
        "code": '''
def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6]]
    print(transpose(m))  # [[1, 4], [2, 5], [3, 6]]
''',
    },
    {
        "id": "binary_search",
        "title": "Binary Search",
        "difficulty": "Basic",
        "description": "Implement iterative binary search on a sorted list; return index or -1.",
        "code": '''
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    print(binary_search(arr, 7))   # 3
    print(binary_search(arr, 4))   # -1
''',
    },
    {
        "id": "gcd_lcm",
        "title": "GCD and LCM",
        "difficulty": "Basic",
        "description": "Compute the GCD and LCM of two integers.",
        "code": '''
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b // gcd(a, b)


if __name__ == "__main__":
    print(gcd(24, 36))  # 12
    print(lcm(4, 6))    # 12
''',
    },
    {
        "id": "fibonacci_memo",
        "title": "Fibonacci with Memoization",
        "difficulty": "Moderate",
        "description": "Compute the nth Fibonacci number efficiently using memoization.",
        "code": '''
def fib(n, memo=None):
    if memo is None:
        memo = {}
    if n in (0, 1):
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


if __name__ == "__main__":
    print([fib(i) for i in range(10)])  # [0,1,1,2,3,5,8,13,21,34]
''',
    },
    {
        "id": "prime_sieve",
        "title": "Sieve of Eratosthenes",
        "difficulty": "Moderate",
        "description": "Return all prime numbers up to n using the Sieve of Eratosthenes.",
        "code": '''
def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for multiple in range(i * i, n + 1, i):
                is_prime[multiple] = False
    return [i for i, prime in enumerate(is_prime) if prime]


if __name__ == "__main__":
    print(sieve_of_eratosthenes(50))
''',
    },
    {
        "id": "string_compression",
        "title": "String Compression",
        "difficulty": "Moderate",
        "description": "Compress a string using counts of repeated characters, e.g. 'aabcccccaaa' -> 'a2b1c5a3'.",
        "code": '''
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
''',
    },
    {
        "id": "longest_common_prefix",
        "title": "Longest Common Prefix",
        "difficulty": "Basic",
        "description": "Find the longest common prefix string among a list of strings.",
        "code": '''
def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


if __name__ == "__main__":
    print(longest_common_prefix(["flower", "flow", "flight"]))  # "fl"
    print(longest_common_prefix(["dog", "racecar", "car"]))     # ""
''',
    },
    {
        "id": "merge_intervals",
        "title": "Merge Intervals",
        "difficulty": "Moderate",
        "description": "Merge all overlapping intervals in a list of [start, end] pairs.",
        "code": '''
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if merged and interval[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            merged.append(interval)
    return merged


if __name__ == "__main__":
    print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
    # [[1, 6], [8, 10], [15, 18]]
''',
    },
    {
        "id": "valid_parentheses",
        "title": "Valid Parentheses",
        "difficulty": "Basic",
        "description": "Check whether a string of brackets ()[]{} is validly matched and nested.",
        "code": '''
def is_valid(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack


if __name__ == "__main__":
    print(is_valid("()[]{}"))  # True
    print(is_valid("(]"))      # False
''',
    },
    {
        "id": "rotate_array",
        "title": "Rotate Array",
        "difficulty": "Basic",
        "description": "Rotate a list to the right by k steps.",
        "code": '''
def rotate(nums, k):
    n = len(nums)
    k = k % n
    return nums[-k:] + nums[:-k] if k else nums[:]


if __name__ == "__main__":
    print(rotate([1, 2, 3, 4, 5, 6, 7], 3))  # [5,6,7,1,2,3,4]
''',
    },
    {
        "id": "vowel_consonant_count",
        "title": "Vowel and Consonant Counter",
        "difficulty": "Basic",
        "description": "Count the number of vowels and consonants in a string.",
        "code": '''
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
''',
    },
    {
        "id": "caesar_cipher",
        "title": "Caesar Cipher",
        "difficulty": "Moderate",
        "description": "Encrypt and decrypt a message using a Caesar cipher shift.",
        "code": '''
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
''',
    },
    {
        "id": "word_frequency",
        "title": "Word Frequency Counter",
        "difficulty": "Basic",
        "description": "Count the frequency of each word in a sentence, case-insensitive.",
        "code": '''
from collections import Counter
import re


def word_frequency(text):
    words = re.findall(r"[a-zA-Z']+", text.lower())
    return dict(Counter(words))


if __name__ == "__main__":
    print(word_frequency("The cat sat on the mat. The cat was happy."))
''',
    },
    {
        "id": "flatten_nested_list",
        "title": "Flatten Nested List",
        "difficulty": "Moderate",
        "description": "Flatten an arbitrarily nested list into a single flat list.",
        "code": '''
def flatten(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


if __name__ == "__main__":
    print(flatten([1, [2, 3, [4, 5]], 6, [[7], 8]]))  # [1,2,3,4,5,6,7,8]
''',
    },
    {
        "id": "chunk_list",
        "title": "Chunk a List",
        "difficulty": "Basic",
        "description": "Split a list into chunks of a given size.",
        "code": '''
def chunk_list(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]


if __name__ == "__main__":
    print(chunk_list([1, 2, 3, 4, 5, 6, 7], 3))  # [[1,2,3],[4,5,6],[7]]
''',
    },
    {
        "id": "binary_decimal_convert",
        "title": "Binary <-> Decimal Conversion",
        "difficulty": "Basic",
        "description": "Convert a decimal integer to binary and back, without using bin()/int(x, 2).",
        "code": '''
def decimal_to_binary(n):
    if n == 0:
        return "0"
    digits = []
    while n > 0:
        digits.append(str(n % 2))
        n //= 2
    return "".join(reversed(digits))


def binary_to_decimal(b):
    value = 0
    for ch in b:
        value = value * 2 + int(ch)
    return value


if __name__ == "__main__":
    print(decimal_to_binary(42))         # "101010"
    print(binary_to_decimal("101010"))   # 42
''',
    },
    {
        "id": "digital_root",
        "title": "Digital Root",
        "difficulty": "Basic",
        "description": "Repeatedly sum the digits of a number until a single digit remains.",
        "code": '''
def digital_root(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n


if __name__ == "__main__":
    print(digital_root(942))  # 6  (9+4+2=15 -> 1+5=6)
''',
    },
    {
        "id": "armstrong_number",
        "title": "Armstrong Number Check",
        "difficulty": "Basic",
        "description": "Check whether a number is an Armstrong number (sum of digits^num_digits equals the number).",
        "code": '''
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d) ** power for d in digits)


if __name__ == "__main__":
    print(is_armstrong(153))  # True
    print(is_armstrong(123))  # False
''',
    },
    {
        "id": "perfect_number",
        "title": "Perfect Number Check",
        "difficulty": "Basic",
        "description": "Check whether a number equals the sum of its proper divisors.",
        "code": '''
def is_perfect(n):
    if n < 2:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n


if __name__ == "__main__":
    print(is_perfect(28))  # True (1+2+4+7+14=28)
    print(is_perfect(12))  # False
''',
    },
    {
        "id": "run_length_encoding",
        "title": "Run-Length Encoding",
        "difficulty": "Moderate",
        "description": "Encode and decode a string using run-length encoding, e.g. 'aaabb' <-> [('a',3), ('b',2)].",
        "code": '''
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
''',
    },
    {
        "id": "matrix_multiply",
        "title": "Matrix Multiplication",
        "difficulty": "Moderate",
        "description": "Multiply two matrices (2D lists) without using numpy.",
        "code": '''
def matrix_multiply(a, b):
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])
    if cols_a != rows_b:
        raise ValueError("Incompatible dimensions for multiplication")

    result = [[0] * cols_b for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            result[i][j] = sum(a[i][k] * b[k][j] for k in range(cols_a))
    return result


if __name__ == "__main__":
    a = [[1, 2], [3, 4]]
    b = [[5, 6], [7, 8]]
    print(matrix_multiply(a, b))  # [[19, 22], [43, 50]]
''',
    },
    {
        "id": "stack_via_queues",
        "title": "Stack Using Two Queues",
        "difficulty": "Moderate",
        "description": "Implement a LIFO stack using only two FIFO queues (collections.deque).",
        "code": '''
from collections import deque


class StackUsingQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.popleft() if self.q1 else None

    def top(self):
        return self.q1[0] if self.q1 else None

    def is_empty(self):
        return not self.q1


if __name__ == "__main__":
    s = StackUsingQueues()
    for v in (1, 2, 3):
        s.push(v)
    print(s.pop())  # 3
    print(s.top())  # 2
''',
    },
    {
        "id": "reverse_linked_list",
        "title": "Reverse a Linked List",
        "difficulty": "Moderate",
        "description": "Implement a singly linked list and reverse it in place.",
        "code": '''
class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


def build_list(values):
    head = None
    for v in reversed(values):
        head = Node(v, head)
    return head


def to_list(head):
    out = []
    while head:
        out.append(head.value)
        head = head.next
    return out


def reverse_list(head):
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev


if __name__ == "__main__":
    head = build_list([1, 2, 3, 4, 5])
    print(to_list(head))               # [1,2,3,4,5]
    print(to_list(reverse_list(head)))  # [5,4,3,2,1]
''',
    },
    {
        "id": "bubble_sort",
        "title": "Bubble Sort",
        "difficulty": "Basic",
        "description": "Implement bubble sort on a list of numbers.",
        "code": '''
def bubble_sort(arr):
    arr = arr[:]
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    print(bubble_sort([5, 2, 9, 1, 5, 6]))  # [1,2,5,5,6,9]
''',
    },
    {
        "id": "quick_sort",
        "title": "Quick Sort",
        "difficulty": "Moderate",
        "description": "Implement quick sort using the Lomuto partition scheme.",
        "code": '''
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)


if __name__ == "__main__":
    print(quick_sort([5, 2, 9, 1, 5, 6]))  # [1,2,5,5,6,9]
''',
    },
    {
        "id": "kth_largest",
        "title": "Kth Largest Element",
        "difficulty": "Moderate",
        "description": "Find the kth largest element in an unsorted list.",
        "code": '''
import heapq


def kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]


if __name__ == "__main__":
    print(kth_largest([3, 2, 1, 5, 6, 4], 2))  # 5
''',
    },
    {
        "id": "missing_number",
        "title": "Missing Number in Array",
        "difficulty": "Basic",
        "description": "Given an array containing n distinct numbers from 0 to n, find the missing one.",
        "code": '''
def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)


if __name__ == "__main__":
    print(missing_number([3, 0, 1]))        # 2
    print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8
''',
    },
    {
        "id": "majority_element",
        "title": "Majority Element (Boyer-Moore Voting)",
        "difficulty": "Moderate",
        "description": "Find the element that appears more than n/2 times, in O(n) time and O(1) space.",
        "code": '''
def majority_element(nums):
    count = 0
    candidate = None
    for n in nums:
        if count == 0:
            candidate = n
        count += 1 if n == candidate else -1
    return candidate


if __name__ == "__main__":
    print(majority_element([2, 2, 1, 1, 1, 2, 2]))  # 2
''',
    },
    {
        "id": "container_with_most_water",
        "title": "Container With Most Water",
        "difficulty": "Moderate",
        "description": "Given heights, find two lines that together with the x-axis form the container holding the most water.",
        "code": '''
def max_area(heights):
    left, right = 0, len(heights) - 1
    best = 0
    while left < right:
        h = min(heights[left], heights[right])
        best = max(best, h * (right - left))
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    return best


if __name__ == "__main__":
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
''',
    },
    {
        "id": "max_subarray_sum",
        "title": "Maximum Subarray Sum (Kadane's Algorithm)",
        "difficulty": "Moderate",
        "description": "Find the contiguous subarray with the largest sum.",
        "code": '''
def max_subarray_sum(nums):
    best = current = nums[0]
    for n in nums[1:]:
        current = max(n, current + n)
        best = max(best, current)
    return best


if __name__ == "__main__":
    print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
''',
    },
    {
        "id": "roman_to_integer",
        "title": "Roman to Integer",
        "difficulty": "Moderate",
        "description": "Convert a Roman numeral string to an integer.",
        "code": '''
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
''',
    },
    {
        "id": "group_anagrams",
        "title": "Group Anagrams",
        "difficulty": "Moderate",
        "description": "Group a list of strings into sets of anagrams.",
        "code": '''
from collections import defaultdict


def group_anagrams(words):
    groups = defaultdict(list)
    for word in words:
        key = "".join(sorted(word))
        groups[key].append(word)
    return list(groups.values())


if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
''',
    },
]
