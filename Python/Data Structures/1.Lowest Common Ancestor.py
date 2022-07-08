class Node:
    '''This class is used to make the structure of the binary tree'''

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def findpath(root, path, k):
    if root is None:  # ! If binary tree exists or not..
        return False
    # ! Store this node in path list. Root.key appended in empty list that is the extreme parent node.
    path.append(root.key)
    if root.key == k:  # ! If the cuurent parent node gets matched with the searching key value
        return True
    if((root.left != None and findpath(root.left, path, k)) or (root.right != None and findpath(root.right, path, k))):
        '''Finding if the searching value exists in the left or right sub-tree'''
        return True

    '''If the searching value doesn't exists in the tree, then return False by popping out the last element from the path list'''
    path.pop()
    return False


def findlca(root, n1, n2):
    path1 = []
    path2 = []  # ! Find paths from root to n1 and root to n2.

    condition1 = findpath(root, path1, n1)
    condition2 = findpath(root, path2, n2)

    # ! Checks if the searching values exist in the tree or not.
    if(not condition1 or not condition2):
        return -1
    i = 0
    # ! If both searching values are present...
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]  # ! Returns the lowest ancestor node.


root = Node(1)
root.left = Node(2)
root.right = Node(3)
# ! Creating the binary tree and planting the left and right nodes.
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(findlca(root, 4, 3))
