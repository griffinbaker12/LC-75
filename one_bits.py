class Solution:
    def hammingWeight(self, n: int) -> int:
        # the binary representation doesn't include any erroneous 1's so...
        return bin(n).count("1")
