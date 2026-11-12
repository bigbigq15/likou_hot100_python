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


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = {num for num in nums}
        res = 0
        m = 0
        for num in num_set:
            if num - 1 not in num_set:
                m = 0
                while num in num_set:
                    m += 1
                    num += 1
                res = max(res, m)
        return res
