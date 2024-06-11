class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructMaximumBinaryTree(nums):
    if not nums:
        return None
    
    max_index = nums.index(max(nums))
    root = TreeNode(nums[max_index])
    root.left = constructMaximumBinaryTree(nums[:max_index])
    root.right = constructMaximumBinaryTree(nums[max_index+1:])
    return root

# Example usage:
nums = [3, 2, 1, 6, 0, 5]
root = constructMaximumBinaryTree(nums)
