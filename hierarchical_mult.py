import random
import time


def hierarchical_multiply(a, b):
    if a == 0 or b == 0:
        return 0
    if a == 1:
        return b
    if b == 1:
        return a

    n = max(a.bit_length(), b.bit_length())
    half = n // 2
    mask = (1 << half) - 1

    a_low, a_high = a & mask, a >> half
    b_low, b_high = b & mask, b >> half

    z0 = hierarchical_multiply(a_low, b_low)
    z1 = hierarchical_multiply((a_low + a_high), (b_low + b_high))
    z2 = hierarchical_multiply(a_high, b_high)

    return (z2 << (2 * half)) + ((z1 - z2 - z0) << half) + z0


def time_multiplication(func, a, b, iterations=1000):
    start = time.time()
    for _ in range(iterations):
        func(a, b)
    end = time.time()
    return end - start


# Test with various sizes of numbers
for bits in [8, 16, 32, 64, 128, 256]:
    a = random.getrandbits(bits)
    b = random.getrandbits(bits)

    hierarchical_time = time_multiplication(hierarchical_multiply, a, b)
    python_time = time_multiplication(int.__mul__, a, b)

    print(f"{bits}-bit numbers:")
    print(f"  Hierarchical: {hierarchical_time:.6f} seconds")
    print(f"  Python built-in: {python_time:.6f} seconds")
    print(f"  Ratio: {hierarchical_time / python_time:.2f}x slower\n")
