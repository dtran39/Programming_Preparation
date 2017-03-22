'''
Problem:
	-  Given a linked list,
        reverse the nodes of a linked list k at a time and return its modified list.
        + k is a positive integer
        and is less than or equal to the length of the linked list.
        + If the number of nodes is not a multiple of k
            then left-out nodes in the end should remain as it is.
    - You may not alter the values in the nodes, only nodes itself may be changed.
    - Only constant memory is allowed.
----------------------------------------------------------------------------------------------------
Examples:

----------------------------------------------------------------------------------------------------
Solution:
- This is the generalize version of swap nodes in pairs
    Or a more advanced version of reversed nodes
1. Initial solution:
    + One pointer to run first to check if enough nodes to make a reversed
    + If yes, starts reverse (iteratively with a counter)
    + Continue
    - Must use dummy node:
        + Because the head of the list is changed (use dummy to keep track)
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        # Print linked list
        def to_str_linked_list(head):
            _str = ""
            while head != None:
                _str += str(head.val) + " "
                head = head.next
            return _str
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Dummy
        dummy = ListNode(0)
        dummy.next = head
        listPtr = head
        leftSegment = dummy
        # Outer loop: loop until reaches the end
        while listPtr:
            # If need to reversed, then segments starts from position of listPtr before checking
            # Count to check if enough
            counter = k
            segmentPtr = listPtr
            while counter > 0:
                if not listPtr: return dummy.next
                counter -= 1
                listPtr = listPtr.next
            # Starts reversing inside the segment
            # now, we have counter = 0, segmentPtr = ptr to traverse current segment
            while counter < k - 1:
                # Storing
                next = segmentPtr.next
                # Swapping
                segmentPtr.next = next.next
                next.next = leftSegment.next
                leftSegment.next = next
                # Iteration update
                counter += 1
            # Finish reversing -> current segment becomes left segment
            leftSegment = segmentPtr
        return dummy.next
