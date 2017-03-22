# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        prev, cur = dummy, head
        # Run to before m
        counter = 1
        while counter < m:
            prev.next = cur
            prev, cur = prev.next, cur.next
            counter += 1
        # reverse from m to n
        # Rename
        left_side = prev
        prev = None
        old_head = cur
        while counter <= n:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            counter += 1
        left_side.next = prev
        old_head.next = cur
        # append after n
        # return head
        return dummy.next