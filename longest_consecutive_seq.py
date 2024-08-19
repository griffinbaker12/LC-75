from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        processed = set()
        longest = 0
        for n in nums:
            if n not in processed and n - 1 not in seen:
                processed.add(n)
                current_num = n
                while current_num + 1 in seen:
                    current_num += 1
                longest = max(longest, current_num-n+1)
        return longest
