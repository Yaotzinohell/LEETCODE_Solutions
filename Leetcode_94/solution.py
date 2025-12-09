# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []

        ret = []
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            ret.append(curr.val)

            curr = curr.right

        return ret

# class Solution(object):
#     def inorderTraversal(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: List[int]
#         """
#         #Recursive Method
#         if not root:
#             return []
#         ret=[]
#         ret+=self.inorderTraversal(root.left)
#         ret.append(root.val)
#         ret+=self.inorderTraversal(root.right)
#         return ret