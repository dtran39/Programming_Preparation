'''
Problem:
	- Given a list, rotate the list to the right by k places, where k is non-negative.

----------------------------------------------------------------------------------------------------
Examples:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
----------------------------------------------------------------------------------------------------
Solution:
- Take care base case: empty or 1 element list
- Get length (to recalculate k)
    + get tail of the list in the process of get length
- update k = k % list length
- tail.next = head
- Traverse to node number list length - k - 1
    + its next node is the new head
    + Therefore, store its next, make .next = None, and return next
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # base case
        if not head or not head.next:
            return head
        # get length
        curPtr, listLen, tail = head, 0, None
        while curPtr:
            if not curPtr.next: tail = curPtr
            listLen += 1
            curPtr = curPtr.next
        # Check k
        k = k % listLen
        # Traverse to node of length - k - 1
        curPtr, tail.next = head, head
        nodeTraversed = 0
        while nodeTraversed < listLen - k - 1:
            curPtr = curPtr.next
            nodeTraversed += 1
        # Its next node is the new head
        newHead = curPtr.next
        curPtr.next = None
        return newHead
