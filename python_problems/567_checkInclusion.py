"""
Given two strings s1 and s2, return true if s2 contains a
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""
from collections import Counter


def checkInclusion(s1, s2):
    k = len(s1)
    s1_cnt = Counter(s1)
    s2_cnt = Counter(s2[:k])

    for i in range(len(s2) - k + 1):
        if s1_cnt == s2_cnt:
            return True
        s2_cnt[s2[i]] -= 1
        if i + k < len(s2):
            s2_cnt[s2[i + k]] += 1
    return False


print(checkInclusion('ab', 'eidbaooo'))
