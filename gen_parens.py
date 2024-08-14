from typing import List


# not sure that backtrack is even the right name for this or what backtrack even means tbh lol
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(res, s="", l_rem=n, r_rem=n):
            if l_rem == 0 and r_rem == 0:
                res.append(s)
                return

            if l_rem > 0:
                backtrack(res, s + "(", l_rem - 1, r_rem)

            if r_rem > 0 and r_rem > l_rem:
                backtrack(res, s + ")", l_rem, r_rem - 1)

        r = []
        backtrack(r)
        return r
