class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def leftviewtree(root, level, max_level):
    '''If there is no left sub-tree, it will shift to the right.'''
    if root is None:
        # ! Level value reset to 1 as it was before if None found! Recursion broken and shifted to right
        return
    if(max_level[0] < level):
        print(root.data)
        max_level[0] = level

    leftviewtree(root.left, level+1, max_level)
    leftviewtree(root.right, level+1, max_level)


def left_view(root):
    max_level = [0]
    leftviewtree(root, 1, max_level)


root = Node(12)
root.left = Node(10)
root.right = Node(20)
root.right.left = Node(25)
root.right.right = Node(40)
left_view(root)
