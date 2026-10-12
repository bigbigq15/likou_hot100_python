class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = 0
        res = 0
        n = len(height)
        while True:
            while height[right] > height[right + 1]:
                right += 1
                if (right + 1) > n - 1:
                    return res
            while height[right + 1] > height[right]:
                right += 1
                if (right + 1) > n - 1:
                    if height[right] > height[left]:
                        while left < right:
                            l = left
                            left += 1
                            res += height[l] - height[left]
                    else:
                        while left < right:
                            l = right
                            left += 1
                            res += height[l] - height[left]
                    return res
            if height[right] > height[left]:
                while left < right:
                    l = left
                    left += 1
                    res += height[l] - height[left]
            else:
                while left < right:
                    l = right
                    left += 1
                    res += height[l] - height[left]


class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        pre_max = 0
        suf_max = 0
        res = 0
        while left <= right:
            pre_max = max(pre_max, height[left])
            suf_max = max(suf_max, height[right])
            if pre_max < suf_max:
                res += pre_max - height[left]
                left += 1
            else:
                res += suf_max - height[right]
                right -= 1
        return res


class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        left = n * [0]
        pre_max = 0
        right = n * [0]
        suf_max = 0
        res = 0
        for i in range(n):
            pre_max = max(pre_max, height[i])
            left[i] = max(pre_max, height[i])
        for i in range(n - 1, -1, -1):
            suf_max = max(suf_max, height[i])
            right[i] = max(suf_max, height[i])
        for pre, suf, h in zip(left, right, height):
            res += min(pre, suf) - h
        return res
