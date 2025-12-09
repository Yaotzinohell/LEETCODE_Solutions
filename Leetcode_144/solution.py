# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        #Iterative Approach
        if not root:
            return []
        ret=[]
        stack=[root]
        while stack:
            node=stack.pop()
            if node:
                ret.append(node.val)
                #Pre-order ofc we make use of Root->Left->Right but here we are using stacks which is LIFO so left should be processed before right so we push left in the end so that left is processed first.
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return ret

# class Solution(object):
#     def preorderTraversal(self, root):
#         """
#         :type root: Optional[TreeNode]
#         :rtype: List[int]
#         """
#         #Recursive Approach
#         if not root:
#             return []
#         ret=[]
#         ret.append(root.val)
#         ret+=self.preorderTraversal(root.left)
#         ret+=self.preorderTraversal(root.right)
#         return ret