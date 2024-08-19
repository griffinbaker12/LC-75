from typing import List

def encode(strs: List[str]) -> str:
    return "".join(f"{len(s)}#{s}" for s in strs)

words = ["neet","code","love","you"]
ans = encode(words)
print(ans)
# 4#neet5#code

def decode(s: str) -> List[str]:
    ans = []
    i = 0
    while i < len(s):
        v = ""
        while s[i] != "#":
            v += s[i]
            i += 1
        v = int(v)
        end = i + 1 + v
        w = s[i+1:end]
        ans.append(w)
        i = end
    return ans

print(decode(ans))
