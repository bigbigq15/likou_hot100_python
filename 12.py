from collections import Counter


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




