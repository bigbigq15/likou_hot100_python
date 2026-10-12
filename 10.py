from typing import List
from collections import Counter


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        for start in range(len(nums)):
            sum = 0
            for end in range(start, -1, -1):
                sum += nums[end]
                if sum == k:
                    res += 1
        return res


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        mp = Counter()
        mp[0] += 1
        pre_count = 0
        for i in range(len(nums)):
            pre_count += nums[i]
            if (pre_count - k) in mp:
                res += mp[pre_count - k]
            mp[pre_count] += 1
        return res


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        mp = Counter()
        mp[0] += 1
        pre = 0
        for n in nums:
            pre += n
            if (pre - k) in mp:
                res += mp[pre - k]
            mp[pre] += 1
        return res
