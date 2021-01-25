# class TreeNode():
#    def __init__(self, val):
#        self.val = val
#        self.left_ptr = None
#        self.right_ptr = None

"""
Problem: Given a Binary Tree, find the largest subtree which is also a Binary Search Tree (BST). Largest here is in terms of number of nodes

Solution: The recursive approach can be thought of as follows,
    Here every node returns the size of the largest BST in a tree with itself as root 

    A node asks its left subtree - "Are you a BST ? and Whats your entire tree size?"
    A node asks its right subtree - "Are you a BST ? and Whats your entire tree size?"
    If both its left and right subtrees are BSTs, then we can check if the node helps in combining the 2 BSTs to form a bigger BST.
    In this case all we need to do is with node as root, check if it is a BST. Now the normal way to check if a tree is a BST is to pass 
    min and max values and check that root and the largest node in the root's left subtree are smallest node in root's right subtree ALL THREE of them 
    fit in properly in the min to max window range. If yes then do repeat this recursively for left and right subtrees with appropriately changing the 
    min - max windows. 

    In this case since every node will return the largest BST, we should not rely on any min-max windows coming from the parent. Instead the child node
    will provide all the required info to the parent and the parent inturn returns all the required info to its parents and so on. Hence subtree of each node
    as root shall return 
        > If it is a BST or not
        > Size of its tree
        > The trees min and max node values
    This info is sufficient for the parent node to make the necessary decision.
    So to summarize, a node will first check if its left subtree and right subtree are BSTs. If yes, using the min max values that both the subtrees are providing
    check if node as root forms a combined BST. If yes them the new size of BST will be size of left subtree + size of right subtree + 1. 

    If node does not form a combined BST, then pass on the max of the sizes of left and right subtress as is. 
"""


def largest_BST_helper(root):
    # This will be usefull in case a node has either left or right child 
    if root == None:
        return (True, 0, -sys.maxsize-1, -sys.maxsize-1)
    
    #If it is a leaf node, then it IS a BST of size 1 with min and max as values 
    #of the leaf itself 
    if root.left_ptr == None and root.right_ptr == None:
        return (True, 1, root.val, root.val)

    l_BST, l_size, l_min, l_max = largest_BST_helper(root.left_ptr)
    r_BST, r_size, r_min, r_max = largest_BST_helper(root.right_ptr)

    # In case a node has both children then min and max values will anyway be valid
    # But in case a node has only one child, then this is to make sure the min max values 
    # are valid before they are used in comparison 
    if root.left_ptr != None and root.right_ptr == None:
        r_min = r_max = root.val
    if root.left_ptr == None and root.right_ptr != None:
        l_min = l_max = root.val

    # This check is to see if subtree starting from root is a BST    
    if l_BST and r_BST and l_max <= root.val and r_min >= root.val:
        return (True, l_size + r_size + 1, l_min, r_max)

    return (False, max(l_size, r_size), l_min, r_max)


def findLargestBST(root):
    if root == None:
        return 0

    is_BST, size, min, max = largest_BST_helper(root)
    return size
