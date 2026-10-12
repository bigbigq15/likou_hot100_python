from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        n = len(s)
        a = set()
        for i in range(n):
            for j in range(i, n):
                if s[j] not in a:
                    a.add(s[j])
                    if j == n - 1:
                        res = max(len(a), res)
                        break
                else:
                    res = max(len(a), res)
                    a = set()
                    break
        return res


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        cnt = Counter()
        left = 0
        for right, c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1:
                cnt[s[left]] -= 1
                # if cnt[s[left]] == 0:
                #     del cnt[s[left]]
                left += 1
            ans = max(ans, right - left + 1)
        return ans

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = -1
        ans = 0
        for r, c in enumerate(s):
            if c in mp:
                l = max(l, mp[c])
            mp[c] = r
            ans = max(ans, r - l)
        return ans
