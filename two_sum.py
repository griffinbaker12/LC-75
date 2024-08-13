from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = defaultdict(int)
        for i, n in enumerate(nums):
            num_dict[n] = i

        for i, n in enumerate(nums):
            v = target - n
            if v in num_dict:
                if num_dict[v] != i:
                    return [num_dict[v], i]

        return [0, 0]
