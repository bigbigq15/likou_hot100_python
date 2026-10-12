class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        pre = 0
        max_ans = nums[0]
        for n in nums:
            pre = max(pre + n, n)
            max_ans = max(pre, max_ans)
        return max_ans



class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        for i, n in enumerate(nums[1:], start=1):
            if nums[i - 1] < 0:
                continue
            else:
                nums[i] += nums[i - 1]
        return max(nums)