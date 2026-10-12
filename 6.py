# 超时
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        for i in range(len(nums)):
            hash_table = {}
            value = nums[i]
            j = i + 1
            while j < len(nums):
                if (0 - (value + nums[j])) in hash_table:
                    l = sorted([nums[i], nums[j], (0 - (value + nums[j]))])
                    if l not in res:
                        res.append(l)
                hash_table[nums[j]] = j
                j += 1
        return res


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            seen = set()
            j = i + 1
            while j < n:
                target = -nums[i] - nums[j]
                if target in seen:
                    res.append([nums[i], target, nums[j]])
                    while j + 1 < n and nums[j] == nums[j + 1]:
                        j += 1
                seen.add(nums[j])
                j += 1

        return res


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n - 2):
            x = nums[i]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if (x + nums[i + 1] + nums[i + 2]) > 0:
                break
            if (x + nums[n - 1] + nums[n - 2]) < 0:
                continue
            j = i + 1
            k = n - 1
            while k > j:
                s = nums[j] + nums[k] + x
                if s > 0:
                    k -= 1
                elif s < 0:
                    j += 1
                else:
                    ans.append([x, nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return ans
