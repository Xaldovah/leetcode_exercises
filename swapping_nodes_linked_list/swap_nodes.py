#!/usr/bin/python3
"""ListNode class module definition for a singly-linked list"""


class ListNode(object):
    """Initialize the class instance"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    """swap the values of the kth node at the beginning and the end"""
    def swapNodes(self, head, k):
        node1 = node2 = fast = head

        k -= 1

        while(k):
            node1 = node1.next
            fast = fast.next
            k -= 1

        while(fast and fast.next):
            node2 = node2.next
            fast = fast.next

        temp = node1.val
        node1.val = node2.val
        node2.val = temp

        return head
