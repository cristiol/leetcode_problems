"""
Given an integer x, return true if x is a
palindrome
, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-231 <= x <= 231 - 1


Follow up: Could you solve it without converting the integer to a string?
"""

def isPalindrome(x: int):
    # x = str(x)
    # l, r = 0, len(x) - 1
    #
    # while l < r:
    #     if x[l] != x[r]:
    #         return False
    #     l += 1
    #     r -= 1
    # return True
    if x < 0:
        return False

    rev = 0
    y = x

    while y:
        rev = rev * 10 + y % 10
        y //= 10

    return rev == x


print(isPalindrome(121))
