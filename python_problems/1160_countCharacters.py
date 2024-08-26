"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.



Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.


Constraints:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
words[i] and chars consist of lowercase English letters.
"""


def countCharacters(words, chars):
    count = [0] * 26
    res = []

    for char in chars:
        index = (ord(char) - ord("a"))
        count[index] += 1

    for word in words:
        count_word = [0] * 26
        good = True

        for char in word:
            index = (ord(char) - ord("a"))
            count_word[index] += 1

        for i in range(len(count)):
            if count[i] < count_word[i]:
                good = False
                break

        if good:
            res.append(word)

    return len(''.join(res))

print(countCharacters(["cat","bt","hat","tree"],"atach"))