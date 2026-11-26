def insertion_sort(nums: list[int]) -> list[int]:
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1

        # 从已排序区末尾往前找，比 key 大的都后移
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1

        # j+1 就是 key 应该插入的位置
        nums[j + 1] = key

    return nums