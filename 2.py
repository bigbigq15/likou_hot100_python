import collections


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        a = collections.defaultdict(list)
        res = []
        for s in strs:
            b = "".join(sorted(s))
            a[b].append(s)
        for r in a.values():
            res.append(r)

        return res