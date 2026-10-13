from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m = 1
        t = 0
        res = []
        r = []
        for i, n in enumerate(nums):
            if n == 0:
                t += 1
                r.append(i)
            else:
                m *= n
        if t == 1:
            res.append(0)
            res *= len(nums)
            for i in r:
                res[i] = m
        elif t == 0:
            for n in nums:
                res.append(m // n)
        else:
            res.append(0)
            res *= len(nums)
        return res

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suf = [1] * n
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]

        pre = 1
        for i, x in enumerate(nums):
            # 此时 pre 为 nums[0] 到 nums[i-1] 的乘积，直接乘到 suf[i] 中
            suf[i] *= pre
            pre *= x

        return suf

