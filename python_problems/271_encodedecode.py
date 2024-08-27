"""
String Encode and Decode
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:

Input: ["neet","code","love","you"]

Output:["neet","code","love","you"]
Example 2:

Input: ["we","say",":","yes"]

Output: ["we","say",":","yes"]
Constraints:

0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.

"""


class Solution:

    def encode(self, strs):

        res = ""

        for i in strs:
            res += str(len(i)) + "#" + i
        return res


    def decode(self, s):

        res, i = [], 0

        while i < len(s):
            if s[i] == "#":
                j = int(s[i-1])
                res.append(s[i+1:i+1+j])
                i += j
            else:
                i += 1
        return res


sol = Solution()
encode_sol = sol.encode(["we","say",":","yes"])
print(encode_sol)
print(sol.decode(encode_sol))
