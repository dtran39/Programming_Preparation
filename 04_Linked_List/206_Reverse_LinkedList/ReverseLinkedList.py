'''
Problem:
	-

----------------------------------------------------------------------------------------------------
Examples: 

----------------------------------------------------------------------------------------------------
Solution: 
1. Recursion
2. Iteration
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
	def reverselist(self, head):
	    # Base case
	    if not head or not head.next:
	        return head
		# Must have a prev, because need to linked cur.next = prev
		prev, cur = None, head
		while cur:
			# must store cur.next since cur.next will be poined to prev
			next = cur.next
			cur.next = prev
			# Increment pointers
			prev = cur
			cur = next
		# Since cur will eventually be None, the last element will be store in prev
		return prev
    def reverseListRec(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Base case
        if not head or not head.next:
            return head
        # Recursion/Inductive case
        next = head.next
        head.next = None
        new_head = self.reverseList(next) # Reverse from head.next to the end of list
        next.next = head
        return new_head
        
    
