'''
Problem:
	- You are given two non-empty linked lists representing two non-negative integers.
        The digits are stored in reverse order and each of their nodes contain a single digit.
        Add the two numbers and return it as a linked list.
        You may assume the two numbers do not contain any leading zero, except the number 0 itself.

----------------------------------------------------------------------------------------------------
Examples:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
----------------------------------------------------------------------------------------------------
Solution:
- Use dummy node to catch empty list
    + Create a dummy, then starts appending to that dummy node
    + In the end, return dummy.next
        By doing this, we do not need to handle empty lists as a separate case
- Do a normal digits traversal:
    + Keep a carry outside the loop (remember to take care of carry after the loop)
    + Each iteration: add values of two digits, and the carry, called curSum
        Careful when add values: if node is empty, assume it is zero
    + Append the next digit (which is curSum % 10)
    + Update carry (which is curSum / 10)
    + Update pointers: both input lists, and the output list
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def getVal(node):
            return 0 if not node else node.val
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1 or l2:
            curSum = getVal(l1) + getVal(l2) + carry
            cur.next = ListNode(curSum % 10)
            carry = curSum / 10
            # Update pointers
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            cur = cur.next
        if carry: cur.next = ListNode(carry)
        return dummy.next
