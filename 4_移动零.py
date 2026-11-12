class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] == 0:
                while nums[right] == 0 and right >= 0:
                    right = right - 1
                self.swap(nums, left, right)
                right = right - 1
            left = left + 1
        return None

    def swap(self, nums: list[int], left: int, right: int):
        num = nums[left]
        nums[left] = nums[right]
        nums[right] = num


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = []
        a = 0
        for num in nums:
            if num == 0:
                a += 1
            else:
                res.append(num)
        while a > 0:
            res.append(0)
            a -= 1
        nums[:] = res
        return None


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[start],nums[i] = nums[i],nums[start]
                start += 1
        return None