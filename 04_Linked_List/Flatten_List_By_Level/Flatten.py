'''
Problem:
    - Given a linked list, in addition to the next pointer, 
        each node has a child pointer that can point to a separate list. 
    With the head node, flatten the list to a single-level linked list.

----------------------------------------------------------------------------------------------------
Examples: 
    1 -> 2 -> 3 -> 4
         |         |
         5 -> 6    7
         |         |
         8         9
    1   2   3   4   5   6   7  8    9
----------------------------------------------------------------------------------------------------
Solution: 
    BFS
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
def arr_to_linked_list(arr):
    dummy = ListNode(0)
    ptr = dummy
    arrLen = len(arr)
    for a_num in arr:
        ptr.next = ListNode(a_num)
        ptr = ptr.next
    return dummy.next
def to_str_linked_list(head):
    _str = ""
    while head != None:
        _str += str(head.val) + " "
        head = head.next
    return _str