from typing import List
from collections import Counter, defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        cnt_p = Counter(p)
        cnt_s = Counter()
        for right, c in enumerate(s):
            cnt_s[c] += 1
            left = right - len(p) + 1
            if left < 0:
                continue
            if cnt_p == cnt_s:
                res.append(left)
            cnt_s[s[left]] -= 1
        return res


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d = defaultdict(int)
        ans = []
        for c in p:
            d[c] -= 1

        l = 0
        for r, x in enumerate(s):
            d[x] += 1

            while d[x] > 0:
                d[s[l]] -= 1
                l += 1

            if r - l + 1 == len(p):
                ans.append(l)
        return ans

# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         res = []
#         cnt = Counter(p)
#         mp = set(p)
#         c = Counter()
#         for i in range(len(s)):
#             if s[i] in mp:
#                 c[s[i]] += 1
#             else:
#                 c.clear()
#             if c == cnt:
#                 res.append(i + 1 - len(p))
#         return res
