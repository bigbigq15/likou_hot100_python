from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = -999999
        l = []
        right = k - 1
        n = nums[0:k:1]
        res = max(n)
        l.append(res)
        for r in range(right + 1, len(nums), 1):
            if res == n[0]:
                n.pop(0)
                n.append(nums[r])
                res = max(n)
                l.append(res)
            else:
                n.pop(0)
                n.append(nums[r])
                res = max(res, n[right])
                l.append(res)
        return l

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        d = deque()
        for i , x in enumerate(nums):
            while d and nums[d[-1]] <= x:
                d.pop()
            d.append(i)
            if d[0] <= i - k:
                d.popleft()
            if d[-1] >= k -1:
                res.append(nums[d[0]])
        return res
