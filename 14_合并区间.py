class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        res: list[list[int]] = []
        intervals.sort(key=lambda p: p[0])
        for x in intervals:
            if res and res[-1][1] >= x[0]:
                res[-1][1] = max(x[1], res[-1][1])
            else:
                res.append(x)
        return res


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        res: list[list[int]] = []
        intervals.sort(key=lambda p: p[0])
        left = intervals[0][0]
        right = intervals[0][1]
        for i, (k, j) in enumerate(intervals[1:]):
            if right >= k:
                right = max(right, j)
            else:
                res.append([left,right])
                left = k
                right = j

        res.append([left, right])
        return res