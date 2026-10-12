from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, num in enumerate(nums):
            if target - num in hash_table:
                return [i, hash_table[target - num]]
            hash_table[nums[i]] = i
        return []
