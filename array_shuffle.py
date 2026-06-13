from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums = [2, 5, 1, 3, 4, 7]
        mid=len(nums)//2
        ans=[]
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])
        return ans