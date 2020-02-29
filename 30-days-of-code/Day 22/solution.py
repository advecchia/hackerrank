class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur

        return root

    def __getHeigthAux(self, root):
        if root is None:
            return 0

        return 1 + max(self.__getHeigthAux(root.left), self.__getHeigthAux(root.right))

    def getHeight(self, root):
        """Find the highest path length on a binary search tree.

        :param root: tree root node
        :return: highest path length
        """
        return self.__getHeigthAux(root) - 1


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root,data)

height = myTree.getHeight(root)
print(height)
