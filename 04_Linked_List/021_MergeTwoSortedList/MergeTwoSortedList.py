'''
Problem:
    - Merge two sorted linked lists and return it as a new list.
    - The new list should be made by splicing together the nodes of the first two lists.
----------------------------------------------------------------------------------------------------
Examples:

----------------------------------------------------------------------------------------------------
Solution:
- Use dummy node to catch empty list
    + Create a dummy, then starts appending to that dummy node
    + In the end, return dummy.next
        By doing this, we do not need to handle empty lists as a separate case
- Do a normal list traversal:
    Add the smaller between two nodes
    Update ptr: only the ptr of the list being added to output, and the output ptr
- If one list is already reach the end,
    add the remaining of the other list to output (more efficient)
'''
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        # Append the remaining list
        cur.next = l1 if l1 else l2
        return dummy.next
