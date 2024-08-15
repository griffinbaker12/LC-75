class Solution:
    def hammingWeight(self, n: int) -> int:
        # the binary representation doesn't include any erroneous 1's so...
        return bin(n).count("1")


def one_bits(n):
    ct = 0
    while n > 0:
        ct += n % 2
        n = n >> 1
    return ct


def one_bits_conv(n):
    bin_r = ""
    while n > 0:
        bin_r = str(n % 2) + bin_r
        n = n >> 1
    return "0b" + bin_r


print(one_bits(20))
print(one_bits_conv(20))

print(one_bits(one_bits_conv(5)))
