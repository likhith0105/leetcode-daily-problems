# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        while curr and curr.next:
            # Nodes to be swapped
            first = curr
            second = curr.next

            # Swapping pointers
            prev.next = second
            first.next = second.next
            second.next = first

            # Re-position pointers for the next pair
            prev = first
            curr = first.next

        return dummy.next