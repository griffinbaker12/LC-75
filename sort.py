x = [3, 2, 1]

# sorted DOES return a value
y = sorted(x)

d = {1: 3, 2: 4, 3: 8}
s = sorted(d.items(), key=lambda d: d[1], reverse=True)

k = 2
ans = [v for v, _ in s][:k]
print(ans)
