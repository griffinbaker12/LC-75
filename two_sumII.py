from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:  # type: ignore
        p1 = 0
        p2 = len(numbers) - 1
        while p1 < p2:
            v = numbers[p1] + numbers[p2]
            if v == target:
                return [p1 + 1, p2 + 1]
            elif v < target:
                p1 += 1
            else:
                p2 -= 1
