def simple_bin(n):
    if n == 0:
        return "0b0"

    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2

    return "0b" + binary


print(simple_bin(5))
print(simple_bin(42))
