class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def insert(self, head, data):
            p = Node(data)
            if head is None:
                head = p
            elif head.next is None:
                head.next = p
            else:
                start = head
                while start.next is not None:
                    start = start.next
                start.next = p

            return head

    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def removeDuplicates(self, head):
        if head is None:
            raise ValueError('Invalid head for linked list')

        current = head
        while current is not None:
            current_value = current.data
            next_node = current.next
            if next_node is None:
                break

            if current_value == next_node.data:
                current.next = next_node.next
            else:
                current = next_node

        return head


mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)

head = mylist.removeDuplicates(head)
mylist.display(head)
