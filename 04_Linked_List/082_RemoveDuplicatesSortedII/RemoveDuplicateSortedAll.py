'''
Problem:
	-

----------------------------------------------------------------------------------------------------
Examples:
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
----------------------------------------------------------------------------------------------------
Solution:
- Use dummy and prev (because even head can be removed)
    + Notice: don't need to point prev.next = head (not the case)
- Traverse based on  value:
    + If current node is unique (no next, or cur.val != next.val):
        valid node -> prev.next = cur
        update prev: prev = prev.next
    + Else (there are more than one nodes with value of cur.val)
        prev.next = None (because prev.next now is pointing to cur, a value duplicated node)
        move to the last node with that value
    + After conditional: update iteration (cur = cur.next)
return dummy.next
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
        dummy = ListNode(-1)
        prev, cur = dummy, head
        while cur:
            if not cur.next or cur.val != cur.next.val:
                prev.next = cur
                prev = prev.next
            else:
                prev.next = None
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
            cur = cur.next
        return dummy.next
