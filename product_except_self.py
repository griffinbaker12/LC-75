from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        left_prod = 1
        for i in range(len(nums)):
            if i == 0:
                continue
            ans[i] = left_prod * nums[i - 1]
            left_prod *= nums[i - 1]

        right_prod = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                continue
            ans[i] *= right_prod * nums[i + 1]
            right_prod *= nums[i + 1]

        return ans
