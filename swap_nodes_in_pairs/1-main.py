#!/usr/bin/python3

from swap_nodes import ListNode, Solution

def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

if __name__ == "__main__":
    # Test cases
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))

    print("Original Linked List:")
    printLinkedList(head)

    solution = Solution()
    new_head = solution.swapPairs(head)

    print("Linked List after Swapping:")
    printLinkedList(new_head)
