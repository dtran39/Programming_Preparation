'''
Problem:
	- Given a list of 1d vectors, traverse the list in round robin style

----------------------------------------------------------------------------------------------------
Examples:
[1,2,3]
[4,5,6,7]
[8,9]
Output: [1,4,8,2,5,9,3,6,7].
----------------------------------------------------------------------------------------------------
Solution:
1. Array and pointer
    - Array to maintain list of current element ptr in each list
    - A pointer to keep track of the current list
        that is in consideration (cur_list_ptr)
    - hasNext:
        + Starts from cur_list_ptr, check if exist a list that has not ended:
            How to detemine ended:
                element pointer of that list is not -1
                and less than length of the list
        + If cannot find such a thing, return False
    - next:
        + before calling next, hasNext is called
            to move list pointer to the next available list
        + Store that current element of current list
        + Update both list ptr (cur_list_ptr)
            (because we will access next list to maintain round robin)
        and element pointer of current list
            (because we have seen this element, we need next one)
2. Queues
'''
class ZigzagIterator(object):
    def general_init(self, all_lists):
        self.all_lists = all_lists
        self.ele_ptrs_in_each_list = [0] * len(all_lists)
        self.cur_list_ptr = 0
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.general_init([v1, v2])
    def next(self):
        """
        :rtype: int
        """
        # Store next element
        cur_list = self.all_lists[self.cur_list_ptr]
        cur_ele_ptr_of_cur_list = self.ele_ptrs_in_each_list[self.cur_list_ptr]
        # Update two pointers:
            # element pointer of current list
                #(because we will need  a new element next time we come back this list)
        self.ele_ptrs_in_each_list[self.cur_list_ptr] += 1
            # current list pointer:
                #because next time we call next,
                    # we need to get element from the next list to preserve round robin
        self.cur_list_ptr = (self.cur_list_ptr + 1) % len(self.ele_ptrs_in_each_list)
        return cur_list[cur_ele_ptr_of_cur_list]

    def hasNext(self):
        """
        :rtype: bool
        """
        number_of_ended_list = 0
        num_list = len(self.all_lists)
        while number_of_ended_list < num_list:
            if self.ele_ptrs_in_each_list[self.cur_list_ptr] == -1:
                number_of_ended_list += 1
                self.cur_list_ptr = (self.cur_list_ptr + 1) % num_list
            elif self.ele_ptrs_in_each_list[self.cur_list_ptr] >= len(self.all_lists[self.cur_list_ptr]):
                self.ele_ptrs_in_each_list[self.cur_list_ptr] = -1
                self.cur_list_ptr = (self.cur_list_ptr + 1) % num_list
            else: # Have an available list
                return True
        return False



# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
