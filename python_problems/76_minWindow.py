"""
Given two strings s and t of lengths m and n respectively, return the minimum window
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.


Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""
from collections import Counter


def minWindow(s, t):
    if t == "": return ""

    window, t_cnt = {}, Counter(t)
    res = [-1, -1]
    res_len = float('inf')
    have, need = 0, len(t)
    l = 0

    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)
        if c in t_cnt and window[c] == t_cnt[c]:
            have += 1

        while have == need:
            window_size = (r - l + 1)
            if window_size < res_len:
                res = [l, r]
                res_len = window_size
            window[s[l]] -= 1
            if s[l] in t_cnt and window[s[l]] < t_cnt[s[l]]:
                have -= 1
            l += 1

    l, r = res
    return s[l:r + 1] if res_len != float('inf') else ''

print(minWindow('ADOBECODEBANC', 'ABC'))
