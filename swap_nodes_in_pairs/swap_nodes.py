#!/usr/bin/python3
"""This is the ListNode module class"""


class ListNode(object):
    """Initialize the class instance"""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    """The method of the solution class"""
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next and current.next.next:
            first = current.next
            second = current.next.next

            first.next = second.next
            second.next = first
            current.next = second

            current = first

        return dummy.next
