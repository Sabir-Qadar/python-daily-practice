def rotate(nums, k):
    n = len(nums)
    k = k % n
    return nums[-k:] + nums[:-k] if k else nums[:]


if __name__ == "__main__":
    print(rotate([1, 2, 3, 4, 5, 6, 7], 3))  # [5,6,7,1,2,3,4]
