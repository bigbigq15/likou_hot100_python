class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        res = 0
        for num in num_set:
            if num - 1 not in num_set:
                a = 0
                while num in num_set:
                    num = num + 1
                    a = a + 1
                res = max(res, a)
        return res
