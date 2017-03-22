# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
Problem:
    You are given two non-empty linked lists representing two non-negative integers. 
    The most significant digit comes first and each of their nodes contain a single digit. 
    Add the two numbers and return it as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

----------------------------------------------------------------------------------------------------
Examples: 
    [7,2,4,3]       [5,6,4] ->                  [7,8,0,7]
----------------------------------------------------------------------------------------------------
Solution: 
1. Most straight forward:
    - Reverse two lists
    - Create sum list
    - reverse sum list
    Time: O(m + n), space: O(1), although input is modified
2. Space required:
    - Store two lists in a stack
    - Popping two stacks to make addition, store in another new stack
    - Popping that stacks, store in new list
    Time: O(m + n), space: O(1)
3. Recursion
'''
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1, s2, s3 = [], [], []
        # Convert to lists to stacks
        while l1 != None:
            s1.append(l1.val)
            l1 = l1.next
        while l2 != None:
            s2.append(l2.val)
            l2 = l2.next
        # Add two stacks
        carry = 0
        while s1 or s2 or carry:
            new_num = carry
            if s1: new_num += s1.pop()
            if s2: new_num += s2.pop()
            # Update number and carry
            s3.append(new_num % 10)
            carry = new_num / 10
        # Convert to linked list
        dummy = ListNode(0)
        cur = dummy
        while s3:
            cur.next = ListNode(s3.pop())
            cur = cur.next
        return dummy.next