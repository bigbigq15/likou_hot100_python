from collections import Counter,defaultdict


# class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if len(t) > len(s):
#             return ""
#         res = ""
#         sm = 0
#         n = 0
#         k = 0
#         s_counter = Counter()
#         t_counter = Counter(t)
#         for i in range(len(s)):
#             if s[i] not in t_counter:
#                 continue
#             else:
#                 for j in range(i,len(s)):
#                     if s_counter[s[j]] == t_counter[s[j]]:
#                         n = 0
#                         i = j
#                         break
#                     n += 1
#                     if s[j] in t_counter:
#                         s_counter[s[j]] += 1
#                     if s_counter == t_counter:
#                         if sm < n:
#                             i = j
#                             n = 0
#                             break
#                         else:
#                             sm = n
#                             k = i
#                             i = j
#                             n = 0
#                             break
#             return s[k:k+sm]


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        t_counter = Counter(t)
        r_counter = Counter()
        left = 0
        right = 0
        n = 99999999
        for i in s:
            r_counter[i] += 1
            right += 1
            while r_counter >= t_counter:
                if n > right - left:
                    res = s[left:right]
                    n = right - left
                r_counter[s[left]] -= 1
                left += 1
        return res

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 注：defaultdict 比 Counter 快
        diff = defaultdict(int)  # 窗口每种字母个数 - t 每种字母个数
        for c in t:
            diff[c] -= 1
        kinds = len(diff)  # t 中有 kinds 种不同的字母

        ans_left, ans_right = -1, len(s)
        ge_cnt = 0  # 窗口内有 ge_cnt 种字母的出现次数 >= t 中相应字母的出现次数
        left = 0

        for right, c in enumerate(s):  # 移动子串右端点
            diff[c] += 1  # 右端点字母移入子串
            if diff[c] == 0:  # 原来窗口内 c 的出现次数比 t 的少，现在一样多
                ge_cnt += 1  # 从 < 变成 >=

            while ge_cnt == kinds:  # 涵盖：所有字母的出现次数都是 >=
                if right - left < ans_right - ans_left:  # 找到更短的子串
                    ans_left, ans_right = left, right  # 记录此时的左右端点

                x = s[left]  # 左端点字母
                if diff[x] == 0:
                    # x 移出窗口之前，检查出现次数，
                    # 如果窗口内 x 的出现次数和 t 一样，
                    # 那么 x 移出窗口后，窗口内 x 的出现次数比 t 的少
                    ge_cnt -= 1  # 从 >= 变成 <
                diff[x] -= 1  # 左端点字母移出子串
                left += 1

        return "" if ans_left < 0 else s[ans_left: ans_right + 1]

