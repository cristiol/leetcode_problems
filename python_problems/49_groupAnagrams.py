"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]


Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
from collections import defaultdict


def groupAnagrams(strs):
    """
    The first solution uses the sort function with O(m*k*logk) and works well on leetcode,
     but for large volumes, the sort function can be a bottleneck.
    :param strs:
    :return: list
    """

    d = dict()

    for i in strs:
        s = ''.join(sorted(i))
        if d.get(s):
            d[s].extend([i])
        else:
            d[s] = [i]
    return list(d.values())

#print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))


def groupAnagrams_(strs):
    """
    The second solution and most optimal using a hashmap
    :param strs:
    :return: list
    """
    res = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        res[tuple(count)].append(s)

    return list(res.values())


print(groupAnagrams_(["eat","tea","tan","ate","nat","bat"]))

