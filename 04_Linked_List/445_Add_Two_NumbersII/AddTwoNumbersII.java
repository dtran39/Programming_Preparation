/*
You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
-----------------------------------------------------------------------------------------------------------------------
Examples:
	(7 -> 2 -> 4 -> 3) 	+ (5 -> 6 -> 4) 			7 -> 8 -> 0 -> 7
	5->6->3				+ 8->4->2					1->4->0->5
	null				+ 1							1
	1 					+ null 						1
	null				+ 1->2						1->2
	1->2->3 			+ null 						1->2->3	
	null 				+ null 						null
-----------------------------------------------------------------------------------------------------------------------
Solution 
1. Reverse both lists, and calculate like normal, then reverse the list again
	- O(m + n)
2. If reversed is not allowed: 
	Push two lists in two stacks, do the same thing
*/
public class Solution {
	public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
		// Push both lists into the stack
        Stack<Integer> s1 = new Stack<Integer>();
        Stack<Integer> s2 = new Stack<Integer>();
        
        while(l1 != null) {
            s1.push(l1.val);
            l1 = l1.next;
        };
        while(l2 != null) {
            s2.push(l2.val);
            l2 = l2.next;
        }
        // Pop and add
        int sumOfCurDigits = 0;
        ListNode list = new ListNode(0);
        while (!s1.empty() || !s2.empty()) {
            if (!s1.empty()) sumOfCurDigits += s1.pop();
            if (!s2.empty()) sumOfCurDigits += s2.pop();
            list.val = sumOfCurDigits % 10;
            ListNode head = new ListNode(sumOfCurDigits / 10);
            head.next = list;
            list = head;
            sumOfCurDigits /= 10;
        }
        
        return list.val == 0 ? list.next : list;
    }	
    public ListNode addTwoNumbersWithReverse(ListNode l1, ListNode l2) {
        l1 = reverseList(l1); l2 = reverseList(l2);
        if (l1 == null && l2 == null) return null;
        if (l1 == null || l2 == null) return (l1 == null) ? l2 : l1;
        // Create head of new list and pointer
        ListNode dummy = new ListNode(0), p = dummy;
        int carry = 0;
        // Loop
        while (l1 != null || l2 != null || carry != 0) {
            // Create a new node to hold the next digit
            ListNode nextDigitNode = new ListNode(0);
            // Compute sum
            int curSumAllDigits = getValue(l1) + getValue(l2) + carry;
            // Calcualte value of next digit (sum % 10), add the digit node to the list
            nextDigitNode.val = curSumAllDigits % 10;         
            p.next = nextDigitNode;
            p = nextDigitNode;
            // Calculate carry
            carry = curSumAllDigits / 10;
            // continue iterations with the list
            l1 = (l1 == null) ? null : l1.next; 
            l2 = (l2 == null) ? null : l2.next;
        }
        return reverseList(dummy.next);
    }
    private int getValue(ListNode node) {
        return (node == null) ? 0 : node.val;
    }

    public ListNode reverseList(ListNode head) {
        // base case
        if (head == null || head.next == null) 
            return head;
        // Traverse
        ListNode ptr = head, newHead = null;
        while (ptr != null) {
            // Save reference to the current head's next
            ListNode next = ptr.next;
            // push the current node to the front of the list
            ptr.next = newHead;
            // Update new head as the current node
            newHead = ptr;
            // Continue traversal
            ptr = next;
        }
        return newHead;
    }
}