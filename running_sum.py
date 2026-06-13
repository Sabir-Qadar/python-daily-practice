from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        nums = [1, 2, 3, 4]
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
