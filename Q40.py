"""
Problem 40: Kth Largest Element
Difficulty: Moderate

Find the kth largest element in an unsorted list.
"""

import heapq


def kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]


if __name__ == "__main__":
    print(kth_largest([3, 2, 1, 5, 6, 4], 2))  # 5
