'''
Problem:
    Given a linked list, swap every two adjacent nodes and return its head.
    Your algorithm should use only constant space.
    You may not modify the values in the list, only nodes itself can be changed.

----------------------------------------------------------------------------------------------------
Examples:
    Given 1->2->3->4, you should return the list as 2->1->4->3.
----------------------------------------------------------------------------------------------------
Solution:
- Two approaches: recursion or iteration (main idea is the same)
1. Recursion
    + Store cur.next in a separate variable (for easier swap)
    + cur.next = swapPairs(next.next)
    + point next.next to cur (finish swapping)
    + return next
2. Iteration: same idea
    + Use dummy pointer and prev in order to keep track the previous part of the list
    In each Iteration:
        (while cur and cur.next, because we only need to do swapping if there are more than two nodes)
        + Store next node for swap (next = cur.next)
        + Swapping:
            cur.next = next.next (point the right to cur)
            next.next = cur (swap between cur and nexts)
            prev.next = next (point the left to next)
3. Change value:
    - iterate through each list:
        while cur and cur.next: # Checking cur is only a safety precaution before checking cur.next
            temp = cur.val
            cur.val = cur.next.val
            cur.next.val = temp
            cur = cur.next.next
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def swapPairs(self, head):
        # Base case check
        if not head or not head.next: return head
        dummy = ListNode(0)
        dummy.next = head
        prev, cur = dummy, head
        while cur and cur.next:
            # Store
            next = cur.next
            # Swapping
            cur.next = next.next
            next.next = cur
            prev.next = next
            # Update ptr
            prev = cur
            cur = cur.next
        return dummy.next
    def swapPairsRec(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # edge case
        if not head or not head.next: return head
        #
        next = head.next
        head.next = self.swapPairs(head.next.next)
        next.next = head
        return next
    def swapPairsValue(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        while cur and cur.next:
            temp = cur.val
            cur.val = cur.next.val
            cur.next.val = temp
            cur = cur.next.next
        return head
