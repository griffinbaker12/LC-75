from typing import List

def encode(strs: List[str]) -> str:
    return "".join(f"{len(s)}#{s}" for s in strs)

words = ["neet","code","love","you"]
ans = encode(words)
print(ans)

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

class Solution2:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            val = int(s[i:j])
            end = j + val + 1
            ans.append(s[j+1:end])
            i = end
        return ans
