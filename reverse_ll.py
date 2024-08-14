from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # [1, 2, 3]
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        prev = None
        while curr_node is not None:
            temp = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = temp
        return prev
