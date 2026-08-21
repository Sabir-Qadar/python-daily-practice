def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(nums)


if __name__ == "__main__":
    print(missing_number([3, 0, 1]))        # 2
    print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8
