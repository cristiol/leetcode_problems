"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
"""


def generateParenthesis(n):
    stack = []
    ans = []

    def backtrack(open, close):

        if len(stack) == 2*n:
            ans.append(''.join(stack))
            return

        if open < n:
            stack.append('(')
            backtrack(open + 1, close)
            stack.pop()

        if open > close:
            stack.append(')')
            backtrack(open, close + 1)
            stack.pop()
    backtrack(0, 0)
    return ans


print(generateParenthesis(3))
