from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_values = defaultdict(list)

        for s in strs:
            char_map = [0] * 26

            for c in s:
                char_map[ord(c) - ord("a")] += 1

            final_values[tuple(char_map)].append(s)

        return final_values.values()  # type: # pyright: ignore
