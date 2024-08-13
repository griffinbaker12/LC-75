from collections import Counter
from typing import List


# time: o(n) where n is the length of nums
# space: o(n) (where n is the amount of numbers we are storing)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  # type: ignore
        counts = Counter(nums)

        count_buckets = [[] for _ in range(len(nums) + 1)]

        for v, c in counts.items():
            count_buckets[c].append(v)

        final = []
        for buck in reversed(count_buckets):
            final.extend(buck)
            if len(final) >= k:
                return final
