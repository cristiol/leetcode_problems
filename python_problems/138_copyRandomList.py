"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.



Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]


Constraints:

0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.
"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __str__(self):
        next_val = self.next.val if self.next else None
        random_val = self.random.val if self.random else None
        return f"Value: {self.val}, Next: {next_val}, Random: {random_val}"


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_copy = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val)
            old_to_copy[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = old_to_copy[curr]
            copy.next = old_to_copy[curr.next]
            copy.random = old_to_copy[curr.random]
            curr = curr.next

        return old_to_copy[head]


# Helper function to convert a list with random pointers to a linked list with random pointers
def list_to_linkedlist_with_random(arr):
    if not arr:
        return None

    # Create all nodes without connections
    nodes = [Node(x[0]) for x in arr]

    # Establish next and random connections
    for i in range(len(arr)):
        if i < len(arr) - 1:
            nodes[i].next = nodes[i + 1]
        if arr[i][1] is not None:
            nodes[i].random = nodes[arr[i][1]]

    return nodes[0]


# Helper function to convert a linked list with random pointers to a list
def linkedlist_with_random_to_list(head):
    result = []
    node_map = {}
    current = head
    index = 0

    # First pass to store nodes in a map to keep track of their indices
    while current:
        node_map[current] = index
        current = current.next
        index += 1

    # Second pass to convert the linked list to the list representation
    current = head
    while current:
        random_index = node_map[current.random] if current.random else None
        result.append((current.val, random_index))
        current = current.next

    return result


# Example usage:
solution = Solution()
head = list_to_linkedlist_with_random([(7, None), (13, 0), (11, 4), (10, 2), (1, 0)])
copied_head = solution.copyRandomList(head)
print(linkedlist_with_random_to_list(copied_head))
