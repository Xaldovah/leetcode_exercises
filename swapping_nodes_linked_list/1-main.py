#!/usr/bin/python3

from swap_nodes import *

# Helper function to create a linked list from a list of values


def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print the linked list


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


if __name__ == "__main__":
    # Test cases
    solution = Solution()

    # Test case 1
    values1 = [1, 2, 3, 4, 5]
    k1 = 2
    head1 = create_linked_list(values1)
    print("Original linked list:")
    print_linked_list(head1)
    result1 = solution.swapNodes(head1, k1)
    print("Linked list after swapping nodes:")
    print_linked_list(result1)

    # Test case 2
    values2 = [7, 9, 6, 6, 7, 8, 3, 0, 9, 5]
    k2 = 5
    head2 = create_linked_list(values2)
    print("Original linked list:")
    print_linked_list(head2)
    result2 = solution.swapNodes(head2, k2)
    print("Linked list after swapping nodes:")
    print_linked_list(result2)
