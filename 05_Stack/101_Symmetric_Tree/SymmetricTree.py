# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetricRec(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Base case
        if not root: return True
        # Must compare ll with rr and lr with rl
        return self.checkTwoBranchesEqual(root.left, root.right)
    def checkTwoBranchesEqual(self,left, right):
        # base case: both null
        if not left and not right: return True
        # Invalid case: one is null, other is not
        if not left or not right: return False
        # Normal case: both have nodes. Check equality, then call recurse with (ll, rr) and (rl, lr)
        if left.val != right.val: return False
        return self.checkTwoBranchesEqual(left.left, right.right) and self.checkTwoBranchesEqual(right.left, left.right)
    def isSymmetric(self, root):
        # Base case
        if root is None:
            return True
        # Initialize stack
        stack = [root.left, root.right]
        # Check by pairs
        while stack:
            p, q = stack.pop(), stack.pop()
            # base case: both null  -> valid
            if p is None and q is None:
                continue
            # Invalid case: one is null, other is not, or they have different values          
            if p is None or q is None or p.val != q.val:
                return False
            # Pass that -> valid pairs -> add their childs to stack
            stack.append(p.left)
            stack.append(q.right)
            #
            stack.append(p.right)
            stack.append(q.left)
            
        return True