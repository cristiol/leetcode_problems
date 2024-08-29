"""
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.



Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
"""
from collections import Counter

# solution using set intersection
def commonChars(words):
    result_dict = {}
    list_of_dicts = [dict(Counter(word)) for word in words]

    common_keys = set.intersection(*map(set, list_of_dicts))

    for key in common_keys:
        result_dict[key] = min(d[key] for d in list_of_dicts if key in d)

    output = []

    for k,v in result_dict.items():
        output.extend([k]*v)

    return output


#solution using count
def commonChars_(words):
    cnt = Counter(words[0])

    for w in words:
        curr_w = Counter(w)
        for i in cnt:
            cnt[i] = min(cnt[i], curr_w[i])

    res = []
    for i in cnt:
        for j in range(cnt[i]):
            res.append(i)

    return res


print(commonChars(["bbddabab","cbcddbdd","bbcadcab","dabcacad","cddcacbc","ccbdbcba","cbddaccc","accdcdbb"]))
print(commonChars_(["bbddabab","cbcddbdd","bbcadcab","dabcacad","cddcacbc","ccbdbcba","cbddaccc","accdcdbb"]))

