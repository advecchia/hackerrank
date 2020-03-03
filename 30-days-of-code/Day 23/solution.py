import sys


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

    def levelOrder(self, root):
        # Write your code here
        if root is None:
            raise ValueError('Invalid tree to print.')

        out_queue = [str(root.data)]
        queue = [root.left, root.right]
        while True:
            # Validate queue
            if len(queue) == 0:
                break

            # Remove and print nodes data
            temp_queue = []
            for node in queue:
                if node is not None:
                    out_queue.append(str(node.data))
                    temp_queue.append(node.left)
                    temp_queue.append(node.right)
            queue.clear()

            # Append new nodes
            queue.extend(temp_queue)
        print(' '.join(out_queue))


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)
