class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def findpath(root, path, k):
    if root is None:
        return False
    path.append(k)
    if root.key == k:
        return True
    if((root.left != None and findpath(root.left, path, k)) or (root.right != None and findpath(root.right, path, k))):
        return True
    path.pop()
    return False


def findlca(root, n1, n2):
    path1 = []
    path2 = []

    condition1 = findpath(root, path1, n1)
    condition2 = findpath(root, path2, n2)

    if(not condition1 or not condition2):
        return -1
    i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.right.left = Node(8)
root.left.right.right = Node(9)
root.right.right.left = Node(10)
root.right.right.right = Node(11)
root.right.right.right.left = Node(12)
findlca(root, 8, 10)
