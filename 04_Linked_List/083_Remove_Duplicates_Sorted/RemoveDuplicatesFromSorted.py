'''
Problem:
	-

----------------------------------------------------------------------------------------------------
Examples:
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
----------------------------------------------------------------------------------------------------
Solution:
    while curPtr.next and curPtr.val == curPtr.next.val:
        curPtr.next = curPtr.next.next
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curPtr = head
        while curPtr:
            while curPtr.next and curPtr.val == curPtr.next.val:
                curPtr.next = curPtr.next.next
            curPtr = curPtr.next
        return head
