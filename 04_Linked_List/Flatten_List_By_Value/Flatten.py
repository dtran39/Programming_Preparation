'''
Problem:
    -

----------------------------------------------------------------------------------------------------
Examples: 
       5 -> 10 -> 19 -> 28
       |    |     |     |
       V    V     V     V
       7    20    22    35
       |          |     |
       V          V     V
       8          50    40
       |                |
       V                V
       30               45

    5->7->8->10->19->20->22->28->30->35->40->45->50.
----------------------------------------------------------------------------------------------------
Solution: 
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