# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def postorderTraversal(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: List[int]
#         """
#         #Recursive Solution
#         if not root:
#             return []
#         ret=[]
#         ret+=self.postorderTraversal(root.left)
#         ret+=self.postorderTraversal(root.right)
#         ret.append(root.val)
#         return ret

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        #Recursive Solution
        if not root:
            return []
        ret=[]
        stack=[root]
        #Left->Right->Root
        #Here we'll do Root->Right->Left and return the reverse of the array
        while stack:
            node = stack.pop()
            ret.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return ret[::-1]