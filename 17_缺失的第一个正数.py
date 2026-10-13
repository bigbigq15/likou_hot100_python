class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        for i, n in enumerate(nums):
            while 0 < n <= len(nums) and n != nums[n-1]:
                nums[i] = nums[n-1]
                nums[n-1] = n
                n = nums[i]
        for i, n in enumerate(nums):
            if n-1 != i:
                return i + 1
        return len(nums)+1
