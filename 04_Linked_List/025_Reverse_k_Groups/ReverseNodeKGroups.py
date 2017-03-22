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
1. Idea:  This is the generalize version of swap nodes in pairs
    Or a more advanced version of reversed nodes
2. Algorithm:
    Outside:
        - Keep a ptr to know the exact location in the list
            + If that ptr is None -> have travesed through all the list -> return
        - How to keep track the head, since it is reversed:
            + Use dummy pointer, and return dummy.next
        - Also we needs to keep track of the last node
            of the left segment of current segment
            + That is initialized as dummy.
    Inside: Two parts
    - Part 1: Traverse to check if the current segment is reversible
        + Meaning if we can traverse k more nodes from the last nodes of its left segment
        + Use the list ptr nodes, because that is how it traverse the list from end to end
        + Before traversing, we saved the current position of list ptr
            Because current list ptr is in the beginning of the segment
                -> use that position to do reversal if necessary
        + Anytime that it reaches the end of the list before traversing k nodes:
            There is nothing else to do -> return dummy.next
        + If it can traverse k nodes -> can do traversal
            -> starts reverse segment (nothing else to do)
    - Part 2: Reverse that segment: 3 steps
        1. Store the next node: nextPtr = curPtr.next
        2. Swapping:
            + curPtr.next = nextPtr.next
            +   nextPtr.next = leftSegment.next
            and leftSegment.next = nextPtr
                (because we keep moving the next node to the beginning of the segment,
                    which is the next of the left segment)
        3. Iteration update: numOfReverse += 1
    - Part 3: Outside iteration update:
        current segment is now left segment for next iteration

3. Complexity:
    - Time: O(n)
    - Space: O(1)
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
        # Initialization
        dummy = ListNode(0)
        dummy.next, listPtr, leftSegment = head, head, dummy
        # Outer loop: loop until reaches the end
        while listPtr:
            # Check if current segment is reversable
            numOfNodesTraversed = 0
            curPtr = listPtr
            while numOfNodesTraversed < k :
                if not listPtr: return dummy.next
                numOfNodesTraversed += 1
                listPtr = listPtr.next
            # Starts reversing inside the segment
            # now, we have counter = 0, curPtr = ptr to traverse current segment
            numOfReverse = 0
            while numOfReverse < k - 1:
                # Storing
                nextPtr = curPtr.next
                # Swapping
                curPtr.next = nextPtr.next
                nextPtr.next = leftSegment.next
                leftSegment.next = nextPtr
                # Iteration update
                numOfReverse += 1
            # Finish reversing -> current segment becomes left segment
            leftSegment = curPtr
        return dummy.next
