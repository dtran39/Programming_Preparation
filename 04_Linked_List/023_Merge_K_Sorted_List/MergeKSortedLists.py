'''
Problem:
	- Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
----------------------------------------------------------------------------------------------------
Examples:
[1,4, 7]
[2, 3, 6]
[5, 8]
-> [1, 2, 3, 4, 5, 6, 7, 8]
----------------------------------------------------------------------------------------------------
Solution:
1. USE HEAP
- Use dummy node to catch empty list
    + Create a dummy, then starts appending to that dummy node
    + In the end, return dummy.next
        By doing this, we do not need to handle empty lists as a separate case
- Use a heap to determine which is the next node to be added to output list
    + Heap sorted by value, but must also keep track of the node and the list it belongs to
    + Best shot: Use tuple
- Complexity:
    + Time: O(nklog(k))     Space: O(k)

2. Divide and conquer:
    - Use merge two lists algorithm from 021
    - Use Merge sort (Divide and conquer) approach:
        + First call: merge(lists, 0, len(lists) - 1)
        + merge(lists, begin, end):
            if begin > end: return None
            if begin == end: return lists[begin]
            mergeTwoLists(merge(lists, begin, middle ), merge(lists, middle + 1, end))
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Dummy
        dummy = ListNode(0)
        cur = dummy
        smallestNodesEachList = []
        # heap
        from heapq import heappush, heappop
        for aListHead in lists:
            if aListHead:
                heappush(smallestNodesEachList, (aListHead.val, aListHead))
        while smallestNodesEachList:
            smallestVal, smallestNode = heappop(smallestNodesEachList)
            # Add new value
            cur.next = ListNode(smallestVal)
            # update pointers, add new value to list if possible
            cur = cur.next
            if smallestNode.next:
                heappush(smallestNodesEachList, (smallestNode.next.val, smallestNode.next))
        return dummy.next
class Solution2:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        def mergeTwoLists(l1, l2):
            curr = dummy = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next

        def mergeKListsHelper(lists, begin, end):
            if begin > end:     return None
            if begin == end:    return lists[begin]
            return mergeTwoLists(mergeKListsHelper(lists, begin, (begin + end) / 2), \
                                 mergeKListsHelper(lists, (begin + end) / 2 + 1, end))

        return mergeKListsHelper(lists, 0, len(lists) - 1)
