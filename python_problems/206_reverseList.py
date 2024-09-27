"""
Easy
Topics
Companies
Given the head of a singly linked list, reverse the list, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


# Helper function to convert a list to a linked list
def list_to_linkedlist(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


# Helper function to convert a linked list to a list
def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# Test cases from docstring
if __name__ == "__main__":
    solution = Solution()

    # Example 1:
    head = list_to_linkedlist([1, 2, 3, 4, 5])
    reversed_list = solution.reverseList(head)
    print(linkedlist_to_list(reversed_list))  # Output: [5, 4, 3, 2, 1]

    # Example 2:
    head = list_to_linkedlist([1, 2])
    reversed_list = solution.reverseList(head)
    print(linkedlist_to_list(reversed_list))  # Output: [2, 1]

    # Example 3:
    head = list_to_linkedlist([])
    reversed_list = solution.reverseList(head)
    print(linkedlist_to_list(reversed_list))  # Output: []

